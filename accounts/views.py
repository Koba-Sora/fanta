from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from fanta.views import index_view

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('fanta:index')

