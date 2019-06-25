from django.db import models

# Create your models here.
# class RetrieveMeta:
#     def __init__(self, model):
#         self.model = model
#
#     @staticmethod
#     def get_field_map(model):
#         class_name = model.__name__
#         return field_map[class_name]

# class BaseModel(models.Model):
#     class Meta:
#         abstract = True
#     @staticmethod
#     def get_field_map(model):
#         return field_map[model.__name__]


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        """A string representation of the model."""
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.title
