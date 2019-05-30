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
            od.update({key: serializers.CharField(source=value)})

        obj = GeneralSerializer._set_declared_fields(od)
        obj.Meta.model = m

        obj.Meta.fields = tuple(get_field_map(m).keys())
        return obj
