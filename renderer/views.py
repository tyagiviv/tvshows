from django.shortcuts import render
from .models import Poster, Favorite
from django.views.generic import ListView


# Create your views here.
def favorite(request):
    # poster = Poster.objects.last()
    # favorite_posters = Poster.objects.filter(id__in=Favorite.objects.values('poster_id'))
    favorite_posters = Poster.objects.filter(id__in=Favorite.objects.filter(user=request.user).values('poster_id'))
    return render(request, 'favorite.html', {'posters': favorite_posters})
#    return render(
#        request, 'favorite.html', {'poster': poster})


class Top(ListView):
    template_name = 'top.html'
    model = Poster
    context_object_name = 'posters'

    def get_queryset(self):
        size = self.request.GET.get('size', 5)
        return Poster.objects.all().order_by('-id')[:int(size)]

