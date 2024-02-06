from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if request.method == "POST":
        link= request.POST['youtubeLink']
        return render(request, 'home.html', {'ytlink': link})
    return render(request, 'home.html')