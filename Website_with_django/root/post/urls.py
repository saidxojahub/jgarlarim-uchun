from django.urls import path
from .views import PostListView, PostCreateView, RegisterView, LoginView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('contact', PostCreateView.as_view(), name='contact'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]
