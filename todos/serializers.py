from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(max_length=100, allow_blank=False, trim_whitespace=True)
    details = serializers.CharField(max_length=100, allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Todo
        fields = ["id", "subject", "details"]

    @staticmethod
    def _require_text(value, name):
        value = (value or "").strip()
        if not value:
            raise serializers.ValidationError(f"{name} is required")
        return value

    def validate_subject(self, value):
        return self._require_text(value, "subject")

    def validate_details(self, value):
        return self._require_text(value, "details")
