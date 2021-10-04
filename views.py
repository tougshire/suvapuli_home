from django.shortcuts import render

def home_view(request):
    return render(request, 'suvapuli_home/suvapuli_home.html')
