"""
URLs for bike app
"""

from django.urls import path
from bike_app.views import OverviewView

urlpatterns = [
    path("", OverviewView.as_view(), name="overview"),
]
