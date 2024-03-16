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

def trigonometry(request):
    """Returns the trigonometry topic page"""
    return render(request, 'topics/trigonometry.html')

def differentiation(request):
    """Returns the differentiation topic page"""
    return render(request, 'topics/differentiation.html')

def integration(request):
    """Returns the integration topic page"""
    return render(request, 'topics/integration.html')

def exponents(request):
    """Returns the logarithms and exponentials topic page"""
    return render(request, 'topics/exponents.html')

def twoDVectors(request):
    """Returns the trigonometry topic page"""
    return render(request, 'topics/2DVectors.html')

def threeDVectors(request):
    """Returns the trigonometry topic page"""
    return render(request, 'topics/3DVectors.html')

def argandDiagrams(request):
    """Returns the Argand Diagrams topic page"""
    return render(request, 'topics/argandDiagrams.html')

def volumesOfRevolution(request):
    """Returns the Volumes of Revolution topic page"""
    return render(request, 'topics/volumesOfRevolution.html')

def methodsInCalculus(request):
    """Returns the Volumes of Revolution topic page"""
    return render(request, 'topics/methodsInCalculus.html')

def matrices(request):
    """Returns the Volumes of Revolution topic page"""
    return render(request, 'topics/matrices.html')

def polarCoordinates(request):
    """Returns the Polar Coordinates topic page"""
    return render(request, 'topics/polarCoordinates.html')

def hyperbolic(request):
    """Returns the Hyperbolic Functions topic page"""
    return render(request, 'topics/hyperbolic.html')

