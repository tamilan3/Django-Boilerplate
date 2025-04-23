from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    A base serializer to include common logic or fields for all serializers.
    """
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        """
        Add custom validation logic that applies to all serializers.
        """
        # Example: Ensure no field contains a forbidden value
        forbidden_value = "forbidden"
        for field, value in data.items():
            if value == forbidden_value:
                raise serializers.ValidationError({field: f"{field} contains a forbidden value."})
        return data

    class Meta:
        abstract = True