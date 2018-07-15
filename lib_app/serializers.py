#serializer in rest as form in jango
# for each model write an serializer


from rest_framework import serializers

from lib_app.models import Author, Article, Category, Verses, Chapter, Tradition, Book, Comment, Answer, User, Question


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class VersesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Verses
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Chapter
        fields = '__all__'


class TraditionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tradition
        fields = '__all__'

#for show
class BookReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer() #
    class Meta:
        model =Book
        fields = '__all__'
#for write
class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = '__all__'
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Answer
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = '__all__'
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Question
        fields = '__all__'