from django.urls import path
from .views import index,movies,about,contact


urlpatterns = [
    path('', index , name='index'),
    path('movies/', movies , name='movies'),
    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),
    # path('/movies', include('movies.urls')),
]