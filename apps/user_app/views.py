from django.shortcuts import render

# Create your views here.
def home(request):
    print '**** home ****'
    # context = {
    # 'user' : []
    # }
    #
    return render(request, 'user_app/home.html')
