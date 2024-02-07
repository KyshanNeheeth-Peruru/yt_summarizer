from django.shortcuts import render, redirect
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
# from IPython.display import YouTubeVideo

# Create your views here.

def home(request):
    if request.method == "POST":
        link= request.POST['youtubeLink']
        video_id = link.split("=")[1]
        # Need to implement a ML model to give segments which are hard coded here-
        segments = [(15, 25),(30, 45)]
        return render(request, 'home.html', {'video_id': video_id,'segments': segments})
    return render(request, 'home.html')