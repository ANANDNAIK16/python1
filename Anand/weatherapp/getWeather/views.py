from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# Create your views here.

def getTempreture(request):
    try:
        if request.method != "GET":
            raise Exception
        try:
            city = request.GET.get('city')
            if city is None:
                return render(request,"index.html")
            try:
                cityName = request.GET.get("city")
                apiKey = "15d458110f825260aa4bca35dc1ad88a"
                url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
                hitTheApi = requests.get(url)

                if 'message' in hitTheApi.json():
                    if hitTheApi.json()['message'] == 'city not found':
                        return render(request,"noCityFound.html")
                elif hitTheApi.status_code != 200:
                    raise Exception
                
                elif hitTheApi.status_code == 200:
                    resopnse = hitTheApi.json()
                    requiredDatasetForFrontEnd = {
                        "city" : resopnse['name'],
                        "country": resopnse['sys']['country'],
                        "latitude" : resopnse['coord']['lat'],
                        "longitude" : resopnse['coord']['lon'],
                        "weatherCondtion" : resopnse['weather'][0]['description'],
                        "humidity" : resopnse['main']['humidity'],
                        "tempretureInKelvin" : int(resopnse['main']['temp']),
                        "tempretureInCelcius" : int(resopnse['main']['temp']) - 273
                    }

                    context = {"resp":requiredDatasetForFrontEnd}

                    return render(request,"index.html", context)
        
            except Exception as ex:
                print(ex)
                return ex

        except Exception as ex:
            return ex

    except Exception as ex:
        return ex