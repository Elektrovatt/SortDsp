from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
# Create your views here.

class MyprojectLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    success_msg = 'Пользователь успешно создан'

    def form_invalid(self, form):
        form_valid = super().form_valid(form)
        username = form.clened_data["username"]
        password = form.clened_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid




class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')