from rest_framework import routers
from django.urls import include, re_path
from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'addtodo', views.AddTodoViewSet)


urlpatterns = [
    re_path(r"^",include(router.urls)),
]
