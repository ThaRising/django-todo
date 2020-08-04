from django.urls import path
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r"todo", views.TodoViewset)

urlpatterns = [
    path("index/", views.IndexView.as_view()),
]

urlpatterns += router.urls
