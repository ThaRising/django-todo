from django.urls import path
from rest_framework import routers
from . import views


router = routers.SimpleRouter()

urlpatterns = [
    path("", views.index)
]

urlpatterns += router.urls