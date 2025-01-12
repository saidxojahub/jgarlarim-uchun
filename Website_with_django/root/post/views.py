from django.views.generic import ListView ,CreateView
from post.models import Post , Contact


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class PostCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/'
    template_name = 'contact.html'



