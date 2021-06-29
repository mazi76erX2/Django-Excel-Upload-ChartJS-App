from django.urls import path

from .views import model_form_upload, ChartView


urlpatterns = [
    path('', model_form_upload, name='form'),
    path('chart/<int:pk>/', ChartView.as_view(), name='chart'),
]
