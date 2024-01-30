from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .views import index_view
from .views import SignupView
from .views import AccountDeleteView
app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('delete_account/', AccountDeleteView.as_view(), name='account_delete'),
    path('',index_view,name='index'),



]