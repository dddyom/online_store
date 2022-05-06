from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView

from app.models import *
from app.forms import LoginUserForm
from app.forms import RegisterUserForm


class Index(ListView):
    model = Category 
    template_name = 'app/index.html'

    context_object_name = 'categories'
    # paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Home')
        return context | c_def

    def get_queryset(self):
        return Category.objects.all()


class Categories(ListView):

    allow_empty = False
    context_object_name = 'products'

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title=str(context['products'][0].categ))
        return context | c_def

    def get_queryset(self):
        return Product.objects.filter(categ__slug=self.kwargs['cat_slug']).select_related("categ")

class RegisterUser(CreateView):

    model = Customer 

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    form_class = RegisterUserForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Register')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        login(self.request, user)
        return redirect('home')



class LoginUser(LoginView):

    model = Customer 

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    form_class = LoginUserForm
    template_name = 'app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        c_def = self.get_user_context(title='Login')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
