from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return render(request,'drinks/index.html')

def name_search(request):
    drink_name = request.POST["drink"]
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}"
    response = requests.get(url)
    data = json.loads(response.text)
    drinks = data["drinks"]


    for drink in drinks:
        ingredients = []
        measurements = []
        for key in drink:
            if "strIngredient" in key:
                if drink[key] == None:
                    continue
                else:
                    ingredients.append(drink[key])
              
            if "strMeasure" in key:
                if drink[key] == None:
                    continue
                else:
                    measurements.append(drink[key])
        drink['ingredients'] = ingredients
        drink['measurements'] = measurements
    context = {"drinks":drinks}

    return render(request, 'drinks/index.html', context)
    
    
    
    
    
    
    
    
    