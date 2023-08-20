from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleModelSerializer
from webapp.models import Article

from api_v2.serializers import CommentModelSerializer
from webapp.models import Comment


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticleView(APIView):
    serializer_class = ArticleModelSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            article = get_object_or_404(Article, pk=pk)
            article_data = self.serializer_class(article).data
            return Response(article_data)
        else:
            articles = Article.objects.order_by("-created_at")
            article_data = self.serializer_class(articles, many=True).data
            return Response(article_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response(self.serializer_class(article).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response(self.serializer_class(article).data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article_name = article.title
        article.delete()
        return Response({'answer': f'Статья {article_name} удалена'}, status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    serializer_class = CommentModelSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            comment = get_object_or_404(Comment, pk=pk)
            article_data = self.serializer_class(comment).data
            return Response(article_data)
        else:
            comments = Comment.objects.order_by("-created_at")
            article_data = self.serializer_class(comments, many=True).data
            return Response(article_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(self.serializer_class(comment).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=comment)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(self.serializer_class(comment).data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        article_name = comment.text
        comment.delete()
        return Response({'answer': f'Статья {article_name} удалена'}, status=status.HTTP_204_NO_CONTENT)
