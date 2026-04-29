"""
Simple Bike App
"""

from typing import Any

from django.views.generic import TemplateView
from bike_app.models import Bike


class OverviewView(TemplateView):
    """
    Overview over all bikes
    """

    template_name = "bike_app/oveview.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        bikes = Bike.objects.all()
        context.update({"bikes": bikes})
        return context
