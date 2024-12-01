from rest_framework import serializers

from ilgi.finance.models import Account

class AccountSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id")

    class Meta:
        model = Account
        fields = "__all__"
