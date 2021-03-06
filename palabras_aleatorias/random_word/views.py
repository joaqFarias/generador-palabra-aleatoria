from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def root(request):
    return redirect('/random_word')

def random_word(request):
    if 'contador' not in request.session:
        request.session['contador'] = 0
        request.session.save()
    else:
        request.session['contador'] = int(request.session['contador']) + 1
        request.session.save()
    if int(request.session['contador'])  == 0:
        palabra = ''
    else:
        palabra = get_random_string(length=32)
    context = {
        'palabra_random': palabra
    }
    return render(request, 'index.html', context)

def reset(request):
    del request.session['contador']
    return redirect('/random_word')