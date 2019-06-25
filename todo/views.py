# Create your views here.
from collections import OrderedDict

from rest_framework import serializers

from todo.models import *
from todo.serializers import GeneralSerializer
from todo.utils import CustomViewSet, get_field_map


class GeneralViewSet(CustomViewSet):

    def get_queryset(self):
        model = self.kwargs.get('model')
        m = eval(model)
        return m.objects.all()

    def get_serializer_class(self):
        model = self.kwargs.get('model')
        m = eval(model)
        od = OrderedDict()

        data = get_field_map(m)

        for key, value in data.items():
            if value['field_type'] == 'str':
                od.update({key: serializers.CharField(source=value['field_name'])})
            elif value['field_type'] == 'fk':
                od.update({key: serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all())})
            # od.update({key: serializers.CharField(source=value)})

        obj = GeneralSerializer._set_declared_fields(od)
        obj.Meta.model = m

        # If we modify field map structure we've to change setting Meta fields logic here
        obj.Meta.fields = tuple(get_field_map(m).keys())
        return obj
