from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from . import models
from .models import Poke
from ..loginReg.models import Users
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = Users.objects.filter(pk=users_id)
        allUsers = Users.objects.exclude(pk=users_id)
        pokes = Poke.objects.all().count()
        mypokes = Users.objects.annotate(pokes=Count('thepokerpoke')).exclude(pk=users_id).order_by('-pokes')
        poke = Users.objects.annotate(pokes=Count('thepokedpoke')).exclude(pk=users_id)
        # pubs = Publisher.objects.annotate(num_books=Count('book'))
        print (50*'*')
        print pokes


        context = {
        'user': user[0],
        'allUsers': allUsers,
        'pokes': pokes,
        'poke':poke,
        'mypokes':mypokes,
        }
    return render(request, 'pokes/index.html', context)

def poke(request, id):
    whoPoked = Users.objects.get(pk=request.session['logged_user'])
    whoPoked.save()
    gotPoked = Users.objects.get(pk=id)
    gotPoked.save()

    thepoke = models.Poke(poker=whoPoked, poked=gotPoked)
    thepoke.save()



    return redirect(reverse('pokes:index'))


    # thepoke = models.Poke(poker=whoPoked, poked=gotPoked)
    # thepoke.save()
