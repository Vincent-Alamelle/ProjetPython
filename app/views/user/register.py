from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView

from app.forms.register import RegisterForm
from app.models import Person


class RegisterView(generic.CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
