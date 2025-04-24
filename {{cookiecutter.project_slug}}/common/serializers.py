from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    A base serializer to include common logic or fields for all serializers.
    """
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        abstract = True