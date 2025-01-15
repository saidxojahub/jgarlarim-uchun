# from django.contrib.auth import authenticate
# from django.views.generic import ListView ,CreateView ,TemplateView
# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy
# from .forms import ContactForm, RegisterForm, LoginForm
# from .models import Post, Contact
#
#
#
# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'home.html'
#
#
# class PostCreateView(CreateView):
#     model = Contact
#     fields = ['name', 'email', 'message']
#     success_url = '/'
#     template_name = 'contact.html'
#
#
# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'auth/register.html'
#     success_url = 'login'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
# class LoginView(TemplateView):
#     template_name = 'auth/login.html'
#     form_class = LoginForm
#     succes_url = reverse_lazy("home")
#
#     def form_valid(self, form):
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=username, password=password)
#         if user:
#             LoginForm(self.request, user)
#             return super().form_valid(form)
#         else:
#             form.add_error(None, "Invalid Password")


from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm, RegisterForm, LoginForm
from .models import Post, Contact


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


class PostCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/'
    template_name = 'contact.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()  # Foydalanuvchini ro‘yxatdan o‘tkazamiz
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)  # Foydalanuvchini tizimga kirgazamiz
            return super().form_valid(form)
        else:
            form.add_error(None, "Username yoki parol noto‘g‘ri")
            return self.form_invalid(form)
