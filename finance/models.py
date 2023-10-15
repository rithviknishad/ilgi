from django.db import models, transaction

from utils.models import BaseModel


class MonetaryField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs["max_digits"] = 10
        kwargs["decimal_places"] = 2
        super().__init__(*args, **kwargs)


class Account(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    balance = MonetaryField(help_text="Balance after last transaction", default=0)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    overdraft_allowed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False, db_index=True)
    closed_on = models.DateTimeField(blank=True, null=True, default=None)
    meta = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Accounts"


class BaseTransaction(BaseModel):
    name = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)
    amount = MonetaryField()
    meta = models.JSONField(blank=True, null=True)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    debit_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="debit_transactions",
        blank=True,
        null=True,
    )
    credit_account = models.OneToOneField(
        Account,
        on_delete=models.PROTECT,
        related_name="credit_transactions",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


# class RecurringTransaction(BaseTransaction):
#     cron_expr = models.CharField(max_length=255)
#     period = DateRangeField()

#     class Meta:
#         verbose_name_plural = "Recurring Transactions"


class Transaction(BaseTransaction):
    timestamp = models.DateTimeField(db_index=True)
    approved = models.BooleanField(default=False)
    # recurring_transaction = models.ForeignKey(
    #     RecurringTransaction,
    #     on_delete=models.PROTECT,
    #     related_name="transactions",
    #     blank=True,
    #     null=True,
    # )

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.debit_account and not self.credit_account:
            raise ValueError("Either debit or credit account must be specified")
        if self.debit_account:
            self.debit_account.balance -= self.amount
            self.debit_account.save(update_fields=["balance"])
        if self.credit_account:
            self.credit_account.balance += self.amount
            self.credit_account.save(update_fields=["balance"])
        super().save(*args, **kwargs)

    @transaction.atomic
    def delete(self, *args):
        if self.debit_account:
            self.debit_account.balance += self.amount
            self.debit_account.save(update_fields=["balance"])
        if self.credit_account:
            self.credit_account.balance -= self.amount
            self.credit_account.save(update_fields=["balance"])
        super().delete(*args)

    class Meta:
        verbose_name_plural = "Transactions"


# class Milestone(BaseModel):
#     account = models.ForeignKey(
#         Account, on_delete=models.PROTECT, related_name="milestone"
#     )
#     target_amount = MonetaryField()
#     completed = models.BooleanField(default=False)
#     completed_on = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         verbose_name_plural = "Milestones"


# class Summary(BaseModel):
#     type = models.CharField(
#         max_length=255,
#         choices=(
#             ("monthly", "Monthly"),
#             ("yearly", "Yearly"),
#         ),
#     )
#     period = DateRangeField()
#     remarks = models.TextField(blank=True, null=True)
#     owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
#     total_income = MonetaryField()
#     total_expense = MonetaryField()
#     opening_balance = MonetaryField()
#     closing_balance = MonetaryField()
#     approved = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = "Summaries"


# class AccountSummary(BaseModel):
#     summary = models.ForeignKey(
#         Summary, on_delete=models.PROTECT, related_name="account_summaries"
#     )
#     account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="+")
#     opening_balance = MonetaryField()
#     closing_balance = MonetaryField()
#     total_income = MonetaryField()
#     total_expense = MonetaryField()
#     approved = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = "Monthly Account Summaries"
