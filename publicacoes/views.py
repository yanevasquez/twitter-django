from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from perfis import models as perfis_models
from publicacoes import forms
from publicacoes import models


# Create your views here.
@login_required()
@require_GET
def index(request):
    # return HttpResponse('Esta é a página inicial')
    tweets = models.Tweet.objects.all().order_by('-publicado_em')
    #query sets
    perfil = request.user.perfil_set.first()
    form = forms.TweetAddForm(request=request, initial={'autor': perfil})
    return render(request,
                  template_name='index.html',
                  context={
                      'tweets': tweets,
                      'form': form,
                  }
                  )


@login_required
def like(request, tweet_id):
    tweet = get_object_or_404(models.Tweet, id=tweet_id)
    # consulta direta abaixo ou inves do object_404
    # tweet = models.Tweet.objects.get(id=tweet_id)
    perfil = request.user.perfil_set.first()
    if tweet.likes.filter(id=perfil.id).exists():
        tweet.likes.remove(perfil)
    else:
        tweet.likes.add(perfil)
    if 'next' in request.GET:
        url = request.GET['next']
    else:
        url = reverse('index')
    return redirect(reverse('index'))


@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(models.Tweet, id=tweet_id)
    return render(request, template_name='tweet_detail.html', context={'tweet': tweet})


@login_required
@require_POST
def tweet_add(request):
    tweets = models.Tweet.objects.all().order_by('-publicado_em')
    form = forms.TweetAddForm(data=request.POST, request=request)

    if form.is_valid():
        form.save()
        return redirect(reverse('index'))

    return render(
        request,
        template_name='index.html',
        context={
            'tweets': tweets,
            'form': form,
        }
    )

# perfil = perfis_models.Perfil.objects.filter(usuario=request.user).first()
