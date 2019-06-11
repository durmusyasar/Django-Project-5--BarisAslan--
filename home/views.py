from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'name' : 'Durmuş',
        }
    else:
        context = {
            'name' : 'Misafir',
        }
    return render(request, 'home.html', context)
