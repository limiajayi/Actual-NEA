from django.shortcuts import render, redirect
from home.models import StudentUser

# Create your views here.
def get_user(request):
    """Returns the session ID corresponding to user"""
    return StudentUser.objects.get(id=request.session['user_id'])

def dash(request):
    """Returns the Student Dash"""
    if 'user_id' in request.session:
        user = get_user(request)
        context = {
            'user':user,
            }
        return render(request, 'students/dash.html', context)
    else:
        return redirect('/home/signup/')