from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView
from django.contrib import messages
from .forms import SignupForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index_view(request):
    return render(request,'fanta/index.html')

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

@method_decorator(login_required, name='dispatch')

class AccountDeleteView(DeleteView):
    model = User  # ユーザーモデルに置き換える
    template_name = 'accounts/account_delete.html'  # テンプレート名を指定
    success_url = reverse_lazy('fanta:index')  # 削除成功時のリダイレクト先

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'アカウントが正常に削除されました。')
        return super().delete(request, *args, **kwargs)