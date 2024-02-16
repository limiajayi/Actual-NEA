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