from rest_framework import serializers
from rest_framework.serializers import ValidationError

from finance import models


class AccountSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", format="hex", read_only=True)
    balance = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
        source="last_transaction__balance",
    )

    class Meta:
        model = models.Account
        exclude = ("deleted", "owner")
        read_only_fields = ("closed", "closed_on", "created_on", "modified_on")


class CreateAccountSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", format="hex", read_only=True)
    opening_balance = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        allow_null=False,
    )

    class Meta:
        model = models.Account
        fields = ("name", "description", "overdraft", "meta")

    def validate(self, attrs):
        validated = super().validate(attrs)

        overdraft = validated.get("overdraft", False)
        opening_balance = validated.get("opening_balance", 0)

        if not overdraft and opening_balance < 0:
            raise ValidationError("Cannot open account with negative balance")

        return validated


class AccountTransactionSerializer:
    id = serializers.UUIDField(source="external_id", format="hex", read_only=True)
    account = AccountSerializer()

    class Meta:
        model = models.AccountTransaction
        fields = ("account", "balance")


class TransactionSerializer(serializers.ModelSerializer):
    debit = AccountTransactionSerializer(read_only=True)
    credit = AccountTransactionSerializer(read_only=True)

    class Meta:
        model = models.Transaction
        exclude = ("deleted", "owner")
        read_only_fields = ("", "created_on", "modified_on")
