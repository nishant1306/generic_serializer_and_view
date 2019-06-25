from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet


class CustomViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass


# field_map = {
#     'Todo': {
#         'Name': 'title',
#         'info': 'description'
#     }
# }

field_map = {
    'Todo': {
        'Name': {
            'field_name': 'title',
            'field_type': 'str'
        },
        'info': {
            'field_name': 'description',
            'field_type': 'str'
        },
        'tag': {
            'field_name': 'tag',
            'field_type': 'fk'
        }
    },
    'Tag': {
        'tag': {
            'field_name': 'name',
            'field_type': 'str'
        }
    }
}


def get_field_map(model):
    class_name = model.__name__
    return field_map[class_name]
