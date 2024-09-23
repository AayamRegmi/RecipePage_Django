from rest_framework.serializers import ModelSerializer
from .models import Category, Recipe, User
from django.contrib.auth.models import Group

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class Userserializers(ModelSerializer):
    class Meta: 
        model = User
        fields = ['username','email','password','contact','groups']      

class GroupSerializers(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
        