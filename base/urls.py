from django.urls import path
from .views import RecipeApiView, RecipeApiDetailView, CategoryApiView, register, login, group_list

urlpatterns = [
    path('category/', CategoryApiView.as_view({'get':'list', 'post':'create'})),
    path('catergory/<int:pk>/', CategoryApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('recipe/', RecipeApiView.as_view()),
    path('recipe/<int:pk>/', RecipeApiDetailView.as_view()),

    path('register/', register),
    path('login/',login),

    path('groups/', group_list)
]