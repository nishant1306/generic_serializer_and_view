from todo.views import GeneralViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo/(?P<model>\w+)', GeneralViewSet, basename='todo')
router.register(r'tag/(?P<model>\w+)', GeneralViewSet, basename='tag')
todo_urlpatterns = router.urls
