from rest_framework.viewsets import ModelViewSet

class BaseViewSet(ModelViewSet):
    """
    BaseViewSet is a custom implementation of Django REST Framework's ModelViewSet
    that provides additional functionality for automatically populating `created_by`
    and `updated_by` fields in the model during create and update operations.

    Methods:
        perform_create(serializer):
            Overrides the default `perform_create` method to include extra fields
            (e.g., `created_by`) before saving the serializer.

        perform_update(serializer):
            Overrides the default `perform_update` method to include extra fields
            (e.g., `updated_by`) before saving the serializer.

        get_extra_fields(serializer, created=False):
            Determines and returns a dictionary of extra fields to be passed to the
            serializer's `save` method. This includes `created_by` and `updated_by`
            fields if they are defined in the model and the request user is available.

    Attributes:
        None specific to this class, but it assumes the presence of `request` and
        `request.user` in the view context for determining the user performing the
        operation.
    """
    def perform_create(self, serializer):
        extra_fields = self.get_extra_fields(serializer, created=True)
        serializer.save(**extra_fields)

    def perform_update(self, serializer):
        extra_fields = self.get_extra_fields(serializer, created=False)
        serializer.save(**extra_fields)

    def get_extra_fields(self, serializer, created=False):
        extra_fields = {}
        if hasattr(serializer, 'Meta') and hasattr(serializer.Meta, 'model'):
            if created and hasattr(serializer.Meta.model, 'created_by') and self.request and self.request.user:
                extra_fields['created_by'] = self.request.user
            if hasattr(serializer.Meta.model, 'updated_by') and self.request and self.request.user:
                extra_fields['updated_by'] = self.request.user
            return extra_fields
        return {}