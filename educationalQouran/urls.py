"""educationalQouran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from lib_app.views import AuthorViewSet, ArticleViewSet, CategoryViewSet, VersesViewSet, ChapterViewSet, \
    TraditionViewSet, BookViewSet, CommentViewSet, AnswerViewSet, UserViewSet, QuestionViewSet

router = routers.DefaultRouter(trailing_slash=False)
# Article, Category, Verses, Chapter, T , Book, Comment, Answer, User, Question

router.register('authors', AuthorViewSet, 'author')
router.register('articles', ArticleViewSet, 'article')
router.register('categorys', CategoryViewSet, 'category')
router.register('versess', VersesViewSet, 'verses')
router.register('chapters',ChapterViewSet, 'chapter')
router.register('traditions', TraditionViewSet, 'tradition')
router.register('books', BookViewSet, 'book')
router.register('comments', CommentViewSet, 'comment')
router.register('answers', AnswerViewSet, 'answer')
router.register('users', UserViewSet, 'user')
router.register('Questions', QuestionViewSet, 'Question')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
