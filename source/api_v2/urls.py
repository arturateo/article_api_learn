from django.urls import path

from api_v2.views import get_csrf_token
from api_v2.views import ArticleView
from api_v2.views import CommentView

app_name = "api_v2"

urlpatterns = [
    path("articles/", ArticleView.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticleView.as_view(), name="article"),
    path("comments/", CommentView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentView.as_view(), name="comments"),
    path("get-csrf-token/", get_csrf_token)
]
