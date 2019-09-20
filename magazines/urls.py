from django.urls import path
from .views import *


urlpatterns = [
    path('', MagazinesView.as_view()),
    path('/<slug:identifier>', MagazineDetailView.as_view())
]
