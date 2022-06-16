from django.shortcuts import render

usersL = [{
    "name": "Armen",
    "age": 25
},
    {
        "name": "Anna",
        "age": 23
    },
]


def home(request):
    return render(request, 'main/index.html', {'table': usersL, 'title': 'Home Page'})


def about(request):
    return render(request, 'main/about.html', {'table': usersL, 'title': 'about Page'})
