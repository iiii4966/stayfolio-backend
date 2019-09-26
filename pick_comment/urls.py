from django.urls import path
from .views      import PickCommentView, CommentEditingView

urlpatterns = [
    path('/<int:pick_id>', PickCommentView.as_view()),
    path('/<int:pick_id>/<int:comment_id>/editing', CommentEditingView.as_view()),
]
