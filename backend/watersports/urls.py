# from django.urls import path
#
# from . import views
#
# app_name = "watersports"
# urlpatterns = [
#     path("boats", views.BoatView, name="BoatView"),
# ]

from rest_framework import routers
from watersports import views

router = routers.DefaultRouter()
router.register(r'boats', views.BoatView, 'boat')