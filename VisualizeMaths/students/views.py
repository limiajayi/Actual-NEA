from django.shortcuts import render, redirect
from home.models import StudentUser
from .models import MathsPoints, FurtherMathsPoints, Question
from .forms import QuestionForm
from random import shuffle

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

def determine_points(word):
    if word == "Easy":
        return 5
    elif word == "Medium":
        return 10
    elif word == "Hard":
        return 15
    
def addToPointsMaths(request, topic, difficulty):
    """Procedure to increment a users maths points based on the topic and difficulty"""
    user = get_user(request)
    user_in_points = MathsPoints.objects.get(username=user)
    if topic == "Quadratics":
        user_in_points.quadratics += determine_points(difficulty)
    elif topic == "Equations and Inequalities":
        user_in_points.equations_and_inequalities += determine_points(difficulty)
    elif topic == "Graphs and Transformations":
        user_in_points.graphs_and_transformations += determine_points(difficulty)
    elif topic == "Straight Line Graphs":
        user_in_points.straight_line_graphs += determine_points(difficulty)
    elif topic == "Circles":
        user_in_points.circles += determine_points(difficulty)
    elif topic == "Trigonometry":
        user_in_points.trigonometry += determine_points(difficulty)
    elif topic == "Differentiation":
        user_in_points.differentiation += determine_points(difficulty)
    elif topic == "Integration":
        user_in_points.integration += determine_points(difficulty)
    elif topic == "2D Vectors":
        user_in_points.two_d_vectors += determine_points(difficulty)
    user_in_points.save()

def addToPointsFurtherMaths(request, topic, difficulty):
    user = get_user(request)
    user_in_points = FurtherMathsPoints.objects.get(username=user)
    if topic == "Argand Diagrams":
        user_in_points.argand_diagrams += determine_points(difficulty)
    elif topic == "Volumes of Revolution":
        user_in_points.volumes_of_revolution += determine_points(difficulty)
    elif topic == "Methods In Calculus":
        user_in_points.methods_in_calculus += determine_points(difficulty)
    elif topic == "Straight Line Graphs":
        user_in_points.straight_line_graphs += determine_points(difficulty)
    elif topic == "Matrices":
        user_in_points.matrices += determine_points(difficulty)
    elif topic == "Polar Coordinates":
        user_in_points.polar_coordinates += determine_points(difficulty)
    elif topic == "Hyperbolic Functions":
        user_in_points.hyperbolic_functions += determine_points(difficulty)
    elif topic == "Differentiation":
        user_in_points.differentiation += determine_points(difficulty)
    elif topic == "Integration":
        user_in_points.integration += determine_points(difficulty)
    elif topic == "3D Vectors":
         user_in_points.three_d_vectors += determine_points(difficulty)
    user_in_points.save()

def question(request):
    subject =  request.GET.get('subject')
    topic =  request.GET.get('topic')
    difficulty =  request.GET.get('difficulty')
    number = request.GET.get('number')
    student_questions = Question.objects.filter(subject=subject, topic=topic, difficulty=difficulty)[:int(number)]

    #if a user submits their answers in the question page
    if request.method == 'POST':
        #if the subject is maths
        if subject == "Maths":
            for q in student_questions:
                #if the answer in the question table is equal to the answer entered by the user
                if q.answer == request.POST.get(q.question):
                    addToPointsMaths(request, topic, difficulty)
                    good_message = "Correct Answer!!"
                    context = {
                    'good': good_message,
                    'student_questions': student_questions,
                    }
                    return render(request, 'students/question.html', context)
                #if the answer in the question table and answer entered by the user are not equal
                else:
                    bad_message = "Incorrect Answer."
                    context = {
                    'student_questions': student_questions,
                    'bad': bad_message,
                    }
                    return render(request, 'students/question.html', context)
        #if the subject is further maths
        else:
            for q in student_questions:
                #if the answer in the question table is equal to the answer entered by the user
                if q.answer == request.POST.get(q.question):
                    addToPointsFurtherMaths(request, topic, difficulty)
                    good_message = "Correct Answer!!"
                    context = {
                    'good': good_message,
                    'student_questions': student_questions,
                    }
                    return render(request, 'students/question.html', context)

                else:
                    bad_message = "Incorrect Answer."
                    context = {
                    'student_questions': student_questions,
                    'bad': bad_message,
                    }
                    return render(request, 'students/question.html', context)
    # if a user does not submit their answers
    else:
        context = {
        'student_questions': student_questions,
        }
        return render(request, 'students/question.html', context)