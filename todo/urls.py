from todo.views import GeneralViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo/(?P<model>\w+)', GeneralViewSet, basename='todo')
todo_urlpatterns = router.urls
