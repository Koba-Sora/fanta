from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include
from .views import index_view
from .views import SignupView
app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('fanta/', include('fanta.urls')),
]
