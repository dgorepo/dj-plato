from django.shortcuts import render


def index(request):
    context = {
        'sala': '35',
        'predio': 'B'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
