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

        if not answer:
            my_ans = "Please enter an answer below."
            color = "warning"

            return render(request, 'add.html', {
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
            'my_ans': my_ans,
            })      

        correct_ans = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_ans) + "."
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
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    num_1, num_2 = max(num_1,num_2), min(num_1,num_2)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_ans = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " - " + old_num_2 + " = " + str(correct_ans) + "."
            color = "danger"

        return render(request, 'subtract.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
            })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2
    })

def multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_ans = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " x " + old_num_2 + " = " + str(correct_ans) + "."
            color = "danger"

        return render(request, 'multiply.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
            })

    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2
    })

def divide(request):
    from random import randint

    x = randint(0,3)
    num_2 = randint(1,6)
    num_1 = x * num_2
    
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_ans = int(old_num_1) // int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " ÷ " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " ÷ " + old_num_2 + " = " + str(correct_ans) + "."
            color = "danger"

        return render(request, 'divide.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
            })

    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2
    })