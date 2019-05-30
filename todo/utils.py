from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet


class CustomViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass


field_map = {
    'Todo': {
        'abc': 'title',
        'info': 'description'
    }
}


def get_field_map(model):
    class_name = model.__name__
    return field_map[class_name]
