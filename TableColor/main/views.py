from django.shortcuts import render
from .models import Table


def home(request):
    table = Table.usersL
    return render(request, 'main/index.html', {'table': table})
