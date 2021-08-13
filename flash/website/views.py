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
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_ans = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = "Incorrect! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_ans) + "," + " not " + answer + "."
            color = "danger"

        return render(request, 'add.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
            })

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