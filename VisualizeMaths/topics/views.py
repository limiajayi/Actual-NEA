from django.shortcuts import render, redirect
from students.views import get_user

# Create your views here.
def subject(request):
    """Returns the subject page"""
    #initially checks if the user exists 
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'topics/subject.html', {'user': user})
    #if not the client requesting for this page is redirected to the sign up page
    else:
        return redirect('/home/signup/')
    
def quadratics(request):
    """Returns the quadratics topic page"""
    return render(request, 'topics/quadratics.html')

def quadraticsQuestions(request):
    """Returns the existing question page for maths with the appropriate parameters"""
    return redirect('/students/questionMaths/?subject=Maths&topics=Quadratics&difficulty=Easy&number=5')

def inequalities(request):
    """Returns the equations and inequalities topic page"""
    return render(request, 'topics/inequalities.html')

def graphsTransformations(request):
    """Returns the graphs and transformations topic page"""
    return render(request, 'topics/transformations.html')

def straightLineGraphs(request):
    """Returns the straight line graphs topic page"""
    return render(request, 'topics/straightLineGraphs.html')

def circles(request):
    """Returns the circles topic page"""
    return render(request, 'topics/circles.html')