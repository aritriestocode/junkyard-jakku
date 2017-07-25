from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    print "**** index ****"
    return render(request, 'login_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
            # print 'User error'

    else:
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        messages.success(request, 'User has been created. Please log in.')
    # print 'User success'
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')

    else:
        request.session['userID'] = results['user'].id
        return redirect('/home')

def logout(request):
	request.session.flush()
	return redirect('/')
