from django.urls import path
from .views import PostListView,DetailView,CreateView,UpdateView,DeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
    path('mycontent/', views.mycontent, name='mycontent'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),#NOT using any templete for updaete,django does it
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('search/',views.search_Result,name='search'),
    path('searchcat/',views.search_cat,name='searchcat'),
    path('about/', views.about, name='blog-about'),
]
