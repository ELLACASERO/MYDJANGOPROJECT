from django.urls import path
from . import views  # Corrected import

urlpatterns = [
    path('', views.post_list, name='post_list'),
]