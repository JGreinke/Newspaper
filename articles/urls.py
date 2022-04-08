from django.urls import path
from .views import(
    ArticleDetailView, 
    ArticleCreateView
)

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'), 
    path('new/', ArticleCreateView.as_view(), name='articles_new'), 
]