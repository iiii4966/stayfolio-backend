from django.urls import path
from .views      import PickListView, PickView

urlpatterns = [
    path('', PickListView.as_view()),
    path('/<int:pick_id>', PickView.as_view()),
]
