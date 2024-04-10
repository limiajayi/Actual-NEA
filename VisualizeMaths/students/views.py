from django.shortcuts import render, redirect
from home.models import StudentUser
from .models import MathsPoints, FurtherMathsPoints, Question
from .forms import QuestionForm
import plotly.graph_objects as go
import datetime

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

def total_points_maths(request):
    """Adds up the points a user has in maths"""
    user = get_user(request)
    user_in_maths = MathsPoints.objects.get(username=user)
    fields = [f for f in MathsPoints._meta.get_fields() if f.name not in  ['id', 'username']]
    total = 0

    for f in fields:
        value = getattr(user_in_maths, f.name)
        total += value
    return total

def total_points_fmaths(request):
    """Adds up the points a user has in further maths"""
    user = get_user(request)

    #checks if the user is doing further maths
    if user.further_maths == True:
        user_in_fmaths = FurtherMathsPoints.objects.get(username=user)
        fields = [f for f in FurtherMathsPoints._meta.get_fields() if f.name not in  ['id', 'username']]
        total = 0

        for f in fields:
            value = getattr(user_in_fmaths, f.name)
            total += value
        return total
    else:
        return 0
    
def totalPoints(request):
    """Adds up the total amount of points a user has"""
    value = total_points_fmaths(request) + total_points_maths(request)
    return value
    
def recommendMaths(request):
    """Works out the topic with the lowest value in MathsPoints for a user and returns the name of the topic"""
    user = get_user(request)
    user_in_maths = MathsPoints.objects.get(username=user)
    fields = [f for f in MathsPoints._meta.get_fields() if f.name not in  ['id', 'username']]
    lowest_value = float('inf')
    
    for f in fields:
        value = getattr(user_in_maths, f.name)
        if value < lowest_value:
            lowest_value = value
            lowest_value_field = f.name
    return lowest_value_field
        
def recommendFurtherMaths(request):
    """Works out the topic with the lowest value in FurtherMathsPoints for a user and returns the name of the topic"""
    user = get_user(request)

    #Initially checks if the user is doing further maths
    if user.further_maths == True:
        user_in_fmaths = FurtherMathsPoints.objects.get(username=user)
        fields = [f for f in FurtherMathsPoints._meta.get_fields() if f.name not in  ['id', 'username']]
        lowest_value = float('inf')

        for f in fields:
            value = getattr(user_in_fmaths, f.name)
            if value < lowest_value:
                lowest_value = value
                lowest_value_field = f.name
        return lowest_value_field
    else:
        return None

def isItMonday():
    """Returns True if it is Monday."""
    today = datetime.datetime.today()
    if today.weekday() == 0:
        return True
    else:
        return False

def dash(request):
    """Returns the Student Dash"""
    if 'user_id' in request.session:
        user = get_user(request)
        #Adds a user to either MathsPoints or FurtherMathsPoints
        appendToMaths(request)
        appendToFurtherMaths(request)

        #save the total points for a user in these variables
        progressMaths = total_points_maths(request)
        progressFurtherMaths = total_points_fmaths(request)

        #saves the lowest value topics for a user in these variables
        mathsTopic = recommendMaths(request)
        furtherMathsTopic = recommendFurtherMaths(request)

        #variable that determines when weekly assessments link should be shown
        week = isItMonday()
        context = {
            'user':user,
            'progressMaths': progressMaths,
            'progressFurtherMaths': progressFurtherMaths,
            'mathsTopic': mathsTopic,
            'furtherMathsTopic': furtherMathsTopic,
            'week': week,
            }
        return render(request, 'students/dash.html', context)
    #If there is no user id in request.session, redirect the user to the sign up page
    else:
        return redirect('/home/signup/')
        
def userSettings(request):
    """Returns a page that allows users to change their password or delete their account."""
    total = totalPoints(request)
    context = {
        'total': total,
    }
    return render(request, 'students/userSettings.html', context)

def changePassword(request):
    """Returns a page that allows users to change their account."""
    user = get_user(request)
    if request.method == 'POST':
        passsword = request.POST.get('password', 'Something Else.');
        user.password = passsword
        user.save()
        message = "Password changed successfully!"
        total = totalPoints(request)
        context = {
            'message': message,
            'total': total,
        }
        return render(request, 'students/userSettings.html', context)
    else:
        context = {}
        return render(request, 'students/changePassword.html', context)
    
def deleteAccount(request):
    """Deletes the users account"""
    user = get_user(request)
    user.delete()
    return redirect('/home/signup/')

def mathsAssessment(request):
    """This function creates a bar chart using plotly graph objects and renders the bar chart in the maths assessment page."""
    user = get_user(request)
    user_in_maths = MathsPoints.objects.get(username=user)
    topics = ['Quadratics', 'Equations and Inequalities', 'Graphs and Transformations', 'Straight Line Graphs', 
            'Circles', 'Trigonometry', 'Differentiation', 'Integration', 'Exponentials and Logarithms', '2D Vectors']
    values = [user_in_maths.quadratics,  user_in_maths.equations_and_inequalities,  user_in_maths.graphs_and_transformations,  user_in_maths.straight_line_graphs,  
              user_in_maths.circles,  user_in_maths.trigonometry,  user_in_maths.differentiation, user_in_maths.integration,  user_in_maths.exponents,  user_in_maths.two_d_vectors]
    chart = go.Figure(data=go.Bar(x=topics, y=values, marker_color='rgb(168, 223, 156)', 
                                      marker_line_color='rgb(31, 31, 31)', marker_line_width=2, 
                                      marker_pattern_shape='/'))
    bar_chart = chart.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgb(255, 253, 242)", 
                                    xaxis_title="Topics", yaxis_title="Points Gained", font_size=18, font_color="Black")
    mathsChart = bar_chart.to_html(full_html=False)
    context = {
        'mathsChart': mathsChart
        }
    return render(request, 'students/mathsAssessment.html', context)

def furtherMathsAssessment(request):
    """This function creates a bar chart using plotly graph objects and renders the bar chart in the further maths assessment page."""
    user = get_user(request)
    user_in_fmaths = FurtherMathsPoints.objects.get(username=user)
    topics = ['Differentiation', 'Integration', 'Argand Diagrams', 'Volumes of Revolution', 'Methods In Calculus', 
                  'Matrices', '3D vectors', 'Polar Coordinates', 'Hyperbolic Functions']
    values = [user_in_fmaths.differentiation, user_in_fmaths.integration, user_in_fmaths.argand_diagrams, user_in_fmaths.volumes_of_revolution,
                  user_in_fmaths.methods_in_calculus, user_in_fmaths.matrices, user_in_fmaths.three_d_vectors, user_in_fmaths.polar_coordinates, user_in_fmaths.hyperbolic_functions]
    chart = go.Figure(data=go.Bar(x=topics, y=values, marker_color='rgb(168, 223, 156)', 
                                      marker_line_color='rgb(31, 31, 31)', marker_line_width=2, 
                                      marker_pattern_shape='/'))
    bar_chart = chart.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgb(255, 253, 242)", 
                                        xaxis_title="Topics", yaxis_title="Points Gained", font_size=18, font_color="Black")
    fmathsChart = bar_chart.to_html(full_html=False)
    context = {
        'fmathsChart': fmathsChart,
        }
    return render(request, 'students/fmathsAssessment.html', context)
 
def logout(request):
    """URL for the user to logout"""
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/home/')

#this is where the relevant functions in future sections will be added

def graph(request):
    """Returns the graphing calculator"""
    if 'user_id' in request.session:
        return render(request, 'students/graph.html')
    
    #If there is no user id in request.session, redirect the user to the sign up page
    else:
        return redirect('/home/signup/')

def testQform(subject, topic):
    "Returns false for topics and subjects that cannot be used as filters."
    if subject == "Maths" and topic == "Argand Diagrams":
        return False
    elif subject == "Maths" and topic == "Volumes of Revolution":
        return False
    elif subject == "Maths" and topic == "Methods In Calculus":
        return False
    elif subject == "Maths" and topic == "Matrices":
        return False
    elif subject == "Maths" and topic == "Polar Coordinates":
        return False
    elif subject == "Maths" and topic == "Hyperbolic Functions":
        return False
    elif subject == "Further Maths" and topic == "Quadratics":
        return False
    elif subject == "Further Maths" and topic == "Equations and Inequalities":
        return False
    elif subject == "Further Maths" and topic == "Graphs and Transformations":
        return False
    elif subject == "Further Maths" and topic == "Straight Line Graphs":
        return False
    elif subject == "Further Maths" and topic == "Circles":
        return False
    elif subject == "Further Maths" and topic == "Trigonometry":
        return False
    elif subject == "Further Maths" and topic == "2D Vectors":
        return False
    else:
        return True

def qform(request):
    """Collects the subject, topic, difficulty and number of questions a user wants to do and redirects them to the question page."""
    form = QuestionForm()

    #if a user submits the form
    if request.method == 'POST':
        subject = request.POST['subject']
        topic = request.POST['topic']
        difficulty = request.POST['difficulty']
        examBoard = request.POST['exam_board']
        number = request.POST['number_of_questions']

        #if testQform() is false, return an error message to users
        if testQform(subject, topic) == False:
            message = "There are no " + topic + " questions in " + subject + "."
            context = {
                'message': message,
            }
            return render(request, 'students/qform.html', context)
        #else redirect the user to the appropriate question page
        elif subject == "Maths":
            return redirect('/students/questionMaths/?subject=' + subject + '&topic=' + topic + '&difficulty=' + difficulty + '&number=' + number + '&exam_board=' + examBoard)
        
        elif subject == "Further Maths":
            return redirect('/students/questionFurtherMaths/?subject=' + subject + '&topic=' + topic + '&difficulty=' + difficulty + '&number=' + number + '&exam_board=' + examBoard)
        
    #if the form hasn't been submitted yet
    context = {
        'form': form,
    }
    return render(request, 'students/qform.html', context)

def determine_points(word):
    """Returns the number of points to be added to a users topics depending on the difficulty."""
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
    elif topic == "Exponentials and Logarithms":
        user_in_points.exponents += determine_points(difficulty)
    elif topic == "2D Vectors":
        user_in_points.two_d_vectors += determine_points(difficulty)
    elif topic == "3D Vectors":
         user_in_points.three_d_vectors += determine_points(difficulty)
    user_in_points.save()

def addToPointsFurtherMaths(request, topic, difficulty):
    """Procedure to increment a users further maths points based on the topic and difficulty"""
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

def testUserInput(input):
    """Tests if the user entered nothing."""
    response = "Please enter an answer."
    if input == "":
        return response
    else:
        return True

def questionMaths(request):
    """Returns the maths question page."""
    subject =  request.GET.get('subject')
    if subject == "Maths":
        topic =  request.GET.get('topic')
        difficulty =  request.GET.get('difficulty')
        number = request.GET.get('number')
        examBoard = request.GET.get('exam_board')
        student_questions = Question.objects.filter(subject="Maths", topic=topic, difficulty=difficulty, exam_board=examBoard)[:int(number)]

        #if a user submits their answers in the question page
        if request.method == 'POST':
                for q in student_questions:

                    #if the user has entered something
                    if testUserInput(request.POST.get(q.question)) == True:
                    #if the answer in the question table is equal to the answer entered by the user
                        if q.answer == request.POST.get(q.question):
                            addToPointsMaths(request, topic, difficulty)
                            good_message = "Correct Answer!!"
                            context = {
                            'good': good_message,
                            'student_questions': student_questions,
                            }
                            return render(request, 'students/questionMaths.html', context)
                #if the answer in the question table and answer entered by the user are not equal
                        else:
                            bad_message = "Incorrect Answer."
                            context = {
                            'student_questions': student_questions,
                            'bad': bad_message,
                            }
                            return render(request, 'students/questionMaths.html', context)
                    #If the answer entered by the user is blank
                    else:
                        message = testUserInput(request.POST.get(q.question))
                        context = {
                            'student_questions': student_questions,
                            'message': message,
                        }
                        return render(request, 'students/questionMaths.html', context)
       
        # if a user has not yet submit their answers
        else:
            context = {
            'student_questions': student_questions,
            }
            return render(request, 'students/questionMaths.html', context)
    
def questionFurtherMaths(request):
    """Returns the further maths question page."""
    subject =  request.GET.get('subject')
    if subject == "Further Maths":
        topic =  request.GET.get('topic')
        difficulty =  request.GET.get('difficulty')
        number = request.GET.get('number')
        examBoard = request.GET.get('exam_board')
        student_questions = Question.objects.filter(subject="Further Maths", topic=topic, difficulty=difficulty, exam_board=examBoard)[:int(number)]

        if request.method == 'POST':
            for q in student_questions:

                if testUserInput(request.POST.get(q.question)) == True:

                    #if the answer in the question table is equal to the answer entered by the user
                    if q.answer == request.POST.get(q.question):
                        addToPointsFurtherMaths(request, topic, difficulty)
                        good_message = "Correct Answer!!"
                        context = {
                        'good': good_message,
                        'student_questions': student_questions,
                        }
                        return render(request, 'students/questionFurtherMaths.html', context)
                    #if the answer in the question table and the answer entered by the user are not equal
                    else:
                        bad_message = "Incorrect Answer."
                        context = {
                        'student_questions': student_questions,
                        'bad': bad_message,
                        }
                        return render(request, 'students/questionFurtherMaths.html', context)
                #If the answer entered by the user is blank
                else:
                    message = testUserInput(request.POST.get(q.question))
                    context = {
                        'student_questions': student_questions,
                        'message': message,
                        }
                    return render(request, 'students/questionFurtherMaths.html', context)
                
        # if a user has not yet submit their answers
        else:
            context = {
            'student_questions': student_questions,
            }
            return render(request, 'students/questionFurtherMaths.html', context)