from django.shortcuts import render, redirect
from home.models import StudentUser
from .models import MathsPoints, FurtherMathsPoints, Question
from .forms import QuestionForm

# Create your views here.
def get_user(request):
    """Returns the session ID corresponding to user"""
    return StudentUser.objects.get(id=request.session['user_id'])

def appendToMaths(request):
    """Adds users to the MathsPoints table."""
    user = get_user(request)
    #If the user is within MathsPoints then do nothing
    if MathsPoints.objects.filter(username=user).exists():
        return None
    #else save them in the table
    else:
        new_user = MathsPoints(username=user)
        new_user.save()

def appendToFurtherMaths(request):
    """Adds users doing further maths to FurtherMathsPoints table."""
    user = get_user(request)
    #If the user is within FurtherMathsPoints then do nothing
    if FurtherMathsPoints.objects.filter(username=user).exists():
        return None
    #Else if the user does further maths and they are not already in the table, save them in the table.
    elif user.further_maths == True:
        new_user = FurtherMathsPoints(username=user)
        new_user.save()

def dash(request):
    """Returns the Student Dash"""
    if 'user_id' in request.session:
        user = get_user(request)
        #Adds a user to either MathsPoints or FurtherMathsPoints
        appendToMaths(request)
        appendToFurtherMaths(request)
        context = {
            'user':user,
            }
        return render(request, 'students/dash.html', context)
    #If there is no user id in request.session, redirect the user to the sign up page
    else:
        return redirect('/home/signup/')
    
def logout(request):
    """URL for the user to logout"""
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/home/')

def qform(request):
    form = QuestionForm()
    if request.method == 'POST':
        subject = request.POST['subject']
        topic = request.POST['topic']
        difficulty = request.POST['difficulty']
        number = request.POST['number_of_questions']
        return redirect('/students/question/?subject=' + subject + '&topic=' + topic + '&difficulty=' + difficulty + '&number=' + number)
    
    context = {
        'form': form
    }
    return render(request, 'students/qform.html', context)

def question(request):
    subject =  request.GET.get('subject')
    topic =  request.GET.get('topic')
    difficulty =  request.GET.get('difficulty')
    student_questions = Question.objects.filter(subject=subject, topic=topic, difficulty=difficulty)

    context = {
        'student_questions': student_questions,
    }
    return render(request, 'students/question.html', context)