from collections import OrderedDict

from rest_framework import serializers


class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'

    @classmethod
    def _set_declared_fields(cls, ordered_dict):
        if not hasattr(cls, '_declared_fields'):
            cls._declared_fields = OrderedDict()

        cls._declared_fields = ordered_dict

        return cls
