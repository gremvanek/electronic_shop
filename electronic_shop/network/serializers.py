from rest_framework import serializers
from .models import NetworkElement


class NetworkElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkElement
        fields = "__all__"
        read_only_fields = ("debt",)
