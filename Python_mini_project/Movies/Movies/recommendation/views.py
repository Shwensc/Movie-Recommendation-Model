from django.shortcuts import render
from django.http import JsonResponse
from . import movie_recommendation_logic
# Create your views here.

def startPage(request):
    return render(request, 'startPage.html')

def mainPage(request):
    return render(request, 'project.html')

def get_recommendations(request):
    movie_name = request.GET.get('movie_name')
    # Call your movie recommendation logic and get recommendations based on the movie_name
    recommendations = movie_recommendation_logic.get_recommendations(movie_name)
    return JsonResponse(recommendations, safe=False)