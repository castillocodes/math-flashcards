from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'points' not in request.session:
        request.session['points'] = 0
    return render(request, 'index.html', {})

def reset(request):
    request.session.clear()
    return redirect('/')

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)
    pointsThisTurn = randint(2,5)

    if request.method == "POST":
        myPoints = request.session['points']
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
            my_ans = answer + " is correct! " + old_num_1 + " + " + old_num_2 + " = " + answer + ". You get " + str(pointsThisTurn) + " points!"
            color = "success"
            myPoints += pointsThisTurn
            request.session['points'] = myPoints
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " + " + old_num_2 + " = " + str(correct_ans) + ". You lost " + str(pointsThisTurn) + " points."
            color = "danger"
            myPoints -= pointsThisTurn
            request.session['points'] = myPoints
        
        return render(request, 'add.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,
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
    pointsThisTurn = randint(5,10)

    num_1, num_2 = max(num_1,num_2), min(num_1,num_2)

    if request.method == "POST":
        myPoints = request.session['points']
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            my_ans = "Please enter an answer below."
            color = "warning"

            return render(request, 'subtract.html', {
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,
            'color': color,
            'my_ans': my_ans,
            })

        correct_ans = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " - " + old_num_2 + " = " + answer + ". You get " + str(pointsThisTurn) + " points!"
            color = "success"
            myPoints += pointsThisTurn
            request.session['points'] = myPoints
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " - " + old_num_2 + " = " + str(correct_ans) + ". You lost " + str(pointsThisTurn) + " points."
            color = "danger"
            myPoints -= pointsThisTurn
            request.session['points'] = myPoints

        return render(request, 'subtract.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,            
            'color': color
            })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
        'pointsThisTurn': pointsThisTurn
    })

def multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)
    pointsThisTurn = randint(10,20)

    if request.method == "POST":
        myPoints = request.session['points']
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            my_ans = "Please enter an answer below."
            color = "warning"

            return render(request, 'multiply.html', {
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,
            'color': color,
            'my_ans': my_ans,
            })

        correct_ans = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " x " + old_num_2 + " = " + answer + ". You get " + str(pointsThisTurn) + " points!"
            color = "success"
            myPoints += pointsThisTurn
            request.session['points'] = myPoints
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " x " + old_num_2 + " = " + str(correct_ans) + ". You lost " + str(pointsThisTurn) + " points."
            color = "danger"
            myPoints -= pointsThisTurn
            request.session['points'] = myPoints

        return render(request, 'multiply.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,           
            'color': color
            })

    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2,
        'pointsThisTurn': pointsThisTurn
    })

def divide(request):
    from random import randint

    x = randint(0,3)
    num_2 = randint(1,6)
    num_1 = x * num_2
    pointsThisTurn = randint(20,50)
    
    if request.method == "POST":
        myPoints = request.session['points']
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            my_ans = "Please enter an answer below."
            color = "warning"

            return render(request, 'divide.html', {
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,
            'color': color,
            'my_ans': my_ans,
            })

        correct_ans = int(old_num_1) // int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = answer + " is correct! " + old_num_1 + " ÷ " + old_num_2 + " = " + answer + ". You get " + str(pointsThisTurn) + " points!"
            color = "success"
            myPoints += pointsThisTurn
            request.session['points'] = myPoints
        else:
            my_ans = answer + " is incorrect! " + old_num_1 + " ÷ " + old_num_2 + " = " + str(correct_ans) + ". You lost " + str(pointsThisTurn) + " points."
            color = "danger"
            myPoints -= pointsThisTurn
            request.session['points'] = myPoints

        return render(request, 'divide.html', {
            'answer':answer,
            'my_ans':my_ans,
            'num_1': num_1,
            'num_2': num_2,
            'pointsThisTurn': pointsThisTurn,           
            'color': color
            })

    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2,
        'pointsThisTurn': pointsThisTurn,           
    })