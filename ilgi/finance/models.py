from django.db import models

from utils.models import BaseModel


class Account(BaseModel):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    active = models.BooleanField(default=True)


class Transaction(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    performed_on = models.DateField()
    created_by = models.ForeignKey("users.User", on_delete=models.PROTECT)


class TransactionEntry(BaseModel):
    transaction = models.ForeignKey("finance.Transaction", on_delete=models.PROTECT, related_name="entries")
    account = models.ForeignKey(
        "finance.Account", on_delete=models.PROTECT, null=True, blank=True, related_name="transaction_entries"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("transaction", "account")
