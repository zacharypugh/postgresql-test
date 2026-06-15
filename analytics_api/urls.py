from django.urls import path
from .views import sales_summary
from .views import run_analysis

urlpatterns = [
    path('sales/', sales_summary),
    path('run-analysis/', run_analysis, name='run_analysis'),
]