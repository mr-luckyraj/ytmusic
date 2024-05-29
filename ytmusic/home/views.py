from django.shortcuts import render
from pytube import YouTube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.http import HttpResponse

def search_videos(query):
    api_key = "your api key"  # Replace with your actual API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=1  # You can change this number to get more search results
    ).execute()

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
    return None

# Create your views here.
def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        url = search_videos(text)
        yt = YouTube(url)
        imgurl = yt.thumbnail_url
        man = yt.streams.filter(only_audio=True).get_by_itag(itag=251).url
        return render(request, 'final.html', {'imgrul':imgurl,'url':man})
    return render(request, 'home.html')

