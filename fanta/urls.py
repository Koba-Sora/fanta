from django.urls import path,include
from . import views

app_name = 'fanta'
urlpatterns = [
    path('',views.index_view,name='index'),
    path('sekai/', views.sekai, name='sekai'), 
    path('taiki/', views.taiki, name='taiki'), 
    path('sawanatsu/', views.sawanatsu, name='sawanatsu'), 
    path('reiya/', views.reiya, name='reiya'), 
    path('horinatsu/', views.horinatsu, name='horinatsu'), 
    path('keito/', views.keito, name='keito'), 
    path('yuse/', views.yuse, name='yuse'), 
    path('sota/', views.sota, name='sota'), 
    path('shota/', views.shota, name='shota'), 
    path('fantaro/', views.FantaroView.as_view(), name='fantaro'), 
    path('fantaro/<int:pk>/detail/',views.PhotoAndReviewView.as_view(),name='detail'),
    path('fantaro/create/',views.CreatePhotoView.as_view(),name='create'),
    path('fantaro/<int:pk>/detail/delete/',views.DeletePhotoView.as_view(),name='delete'),
    path('fantaro/<int:photo_id>/review/',views.CreateReviewView.as_view(),name='review'),


]