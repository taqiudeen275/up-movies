from django.urls import path
from .views import tv_series


urlpatterns = [

    path('tv_series/', tv_series , name='tv_series'),
]