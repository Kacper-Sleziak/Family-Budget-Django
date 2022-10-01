from rest_framework import serializers


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields


class QuerySerializerMixin:
    """
    Mixin class allowing serializer to prefetch relation data defined in class fields.
    """

    PREFETCH_FIELDS = []
    RELATED_FIELDS = []

    @classmethod
    def get_related_queries(cls, queryset):
        """
        Method prefetching relation data from class fields.
        """
        if cls.RELATED_FIELDS:
            queryset = queryset.select_related(*cls.RELATED_FIELDS)
        if cls.PREFETCH_FIELDS:
            queryset = queryset.prefetch_related(*cls.PREFETCH_FIELDS)
        return queryset
