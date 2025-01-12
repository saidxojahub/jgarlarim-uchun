from django.urls import path
from post.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('Contact/', PostCreateView.as_view(), name = 'Contact'),
]
