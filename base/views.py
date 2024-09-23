from django.shortcuts import render
from .serializers import RecipeSerializer, CategorySerializer, Userserializers, GroupSerializers
from .models import Category, Recipe, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


from .permissions import CustomPermission

@api_view(['GET'])
@permission_classes([AllowAny])
def group_list(request):
    
    groups_objs = Group.objects.all()
    serializer = GroupSerializers(groups_objs, many = True)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    
    password = request.data.get('password')
    hash_password = make_password(password) #encrypting the password
    request.data['password'] = hash_password #overriding value in password field

    serializer = Userserializers(data = request.data) #passes data to serializer

    if serializer.is_valid():
        serializer.save()
        return Response("User data registered")
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    email = request.data.get('email')
    password = request.data.get('password')   
    
    user = authenticate(username = email, password = password)

    if user == None:
        return Response("invalid credentials")
    else:
        token,_ = Token.objects.get_or_create(user=user)

        return Response(token.key)

class CategoryApiView(ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated, CustomPermission] #checks token, checks users group permissions
    
       
        
class RecipeApiView(GenericAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, CustomPermission] #checks token, checks users group permissions    
   
    filterset_fields = ['category']
    search_fields = ['name']

    #view all recipes
    def get(self, request):
        queryset = self.get_queryset() #gets queryset in the class #is object data
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True) #converting queryset object type to json
        data = serializer.data
        
        return Response(data)   
    
    #create new recipes
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response('Data created')
        else:
            return Response(serializer.errors)

class RecipeApiDetailView(GenericAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer 
    permission_classes = [IsAuthenticated, CustomPermission] #checks token, checks users group permissions
    

    #get specific recipe data
    def get(self, request, pk):
        queryset = self.get_object() #removes data not exists error, automatically takes pk as id
        serializer = self.serializer_class(queryset)

        data = serializer.data
        return Response(data)
    
    #update specific recipe data
    def put(self, request, pk):
        queryset = self.get_object()
        serializer = self.serializer_class(queryset, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response("Recipe updated")
        else:
            return Response(serializer.errors)
    
    #delete specific recipe data
    def delete(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response('Recipe removed')         




