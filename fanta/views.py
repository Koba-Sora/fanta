from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Photo,Review
from django.contrib.auth.decorators import login_required
from .models import Photo,Review,Like
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def index_view(request):
    return render(request,'fanta/index.html')

def sekai(request):
    return render(request, 'fanta/sekai.html')

def taiki(request):
    return render(request, 'fanta/taiki.html')

def sawanatsu(request):
    return render(request, 'fanta/sawanatsu.html')

def reiya(request):
    return render(request, 'fanta/reiya.html')

def horinatsu(request):
    return render(request, 'fanta/horinatsu.html')

def keito(request):
    return render(request, 'fanta/keito.html')

def yuse(request):
    return render(request, 'fanta/yuse.html')

def sota(request):
    return render(request, 'fanta/sota.html')

def shota(request):
    return render(request, 'fanta/shota.html')

class FantaroView(ListView):
    template_name = 'fanta/fantaro.html'
    model = Photo

class PhotoAndReviewView(DetailView):
    template_name = 'fanta/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.get_object()
        context['reviews'] = photo.review_set.all() 
        context['likes_count'] = photo.likes.count()  
        context['likes_users'] = [like.user for like in photo.likes.all()]
        return context
    
    def user_is_authenticated(self):
        return self.request.user.is_authenticated

@login_required
def toggle_like(request, photo_id):
    if request.method == 'POST':
        photo = get_object_or_404(Photo, pk=photo_id)
        user = request.user

        if user.is_authenticated:
            if photo.likes.filter(user=user).exists():
                like = photo.likes.get(user=user)
                like.delete()
                liked = False
            else:
                like = Like.objects.create(photo=photo, user=user)
                liked = True
            
            data = {'liked': liked, 'likes_count': photo.likes.count()}
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    else:
        # POST メソッド以外の場合は photo_detail.html を表示する
        photo = get_object_or_404(Photo, pk=photo_id)
        context = {'object': photo,}
        return render(request, 'photo_detail.html', context)

class CreatePhotoView(LoginRequiredMixin,CreateView):
    template_name = 'fanta/photo_create.html'
    model = Photo
    fields = ('member','photo')
    success_url = reverse_lazy('fanta:fantaro')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePhotoView(LoginRequiredMixin,DeleteView):
    template_name = 'fanta/photo_confin_delete.html'
    model = Photo
    success_url = reverse_lazy('fanta:fantaro')

class CreateReviewView(LoginRequiredMixin,CreateView):
    template_name = 'fanta/review_form.html'
    model = Review
    fields = ('photo','text',)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.get(pk=self.kwargs['photo_id'])
        return context

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fanta:detail',kwargs={'pk':self.object.photo.id})