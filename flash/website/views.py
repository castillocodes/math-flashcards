from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'add.html', {'answer':answer})

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2
    })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})