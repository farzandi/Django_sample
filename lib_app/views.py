from rest_framework import viewsets, permissions

from lib_app.models import Author, Article, Category, Verses, Chapter, Tradition, Book, Comment, Answer, User, Question
from lib_app.serializers import AuthorSerializer, ArticleSerializer, CategorySerializer, VersesSerializer, \
    ChapterSerializer, TraditionSerializer, BookReadSerializer, CommentSerializer, AnswerSerializer, UserSerializer, \
    QuestionSerializer, BookWriteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset =Category.objects.all()
    serializer_class =CategorySerializer

class VersesViewSet(viewsets.ModelViewSet):
    queryset =Verses.objects.all()
    serializer_class =VersesSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset =Chapter.objects.all()
    serializer_class =ChapterSerializer

class TraditionViewSet(viewsets.ModelViewSet):
    queryset =Tradition.objects.all()
    serializer_class =TraditionSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset =Book.objects.all()
    # only book with existing category:
       # Book.objects.filter(category__isnull=False)
    #only book with alive author :
       #        # Book.objects.filter(author__isalive=False)
    #tow underline is  for forign key of book
    #all book exept category is not null
    # Book.objects.exclude(category__isnull=False)

    # serializer_class =BookReadSerializer
    #when read and wirte ??
    def get_serializer_class(self):
        #request is jango request with method
        if self.request.method in permissions.SAFE_METHODS:
            return BookReadSerializer
        #safe method: get option  head
        else :
            return BookWriteSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class =CommentSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset =Answer.objects.all()
    serializer_class =AnswerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class =UserSerializer
class QuestionViewSet(viewsets.ModelViewSet):
    queryset =Question.objects.all()
    serializer_class =QuestionSerializer