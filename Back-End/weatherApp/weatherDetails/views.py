from operator import contains
from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from .models import *

class getWeatherForcast(APIView):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        day = request.GET.get('day')

        if  "S" in str(latitude):
             #latitude = -1 * (latitude[:len(latitude)-3])
             latitude = "-"+latitude[:len(latitude)-3]
             #print(latitude)
        else:
             latitude = latitude[:len(latitude)-3]
             #print(latitude)
        
        if "W" in str(longitude):
            longitude = "-"+longitude[:len(longitude)-3]
            #print(longitude)
        else:
            longitude = longitude[:len(longitude)-3]
            #print(longitude)

        
        #Check if co-ordinates already exist
        record_coordinates = coordinateWiseData.objects.filter(latitude=latitude, longitude=longitude).exists()
        if record_coordinates == True:
            record = coordinateWiseData.objects.get(latitude=latitude, longitude=longitude)

            temp = getTemperatureByDay(day, record)

            return JsonResponse({
            "status": "OK",
            "sCode": 200,
            'Day' : day,
            "Temperature" : temp
        }, status=200)

        
        url_coordinate_info = "https://api.weather.gov/points/"+str(latitude)+","+str(longitude)
        request_coordinate_info = requests.get(url_coordinate_info) 
        request_coordinate_info_json = request_coordinate_info.json()
        print(request_coordinate_info_json)
        #print(request_coordinate_info_json["properties"]["gridId"])
        #print(request_coordinate_info_json["properties"]["gridX"])
        #print(request_coordinate_info_json["properties"]["gridY"])
      

        url_forcast = request_coordinate_info_json["properties"]["forecast"]
        request_forcast_info = requests.get(url_forcast) 
        request_forcast_info_json = request_forcast_info.json()
        print(request_forcast_info_json)

        coordinateWiseData.objects.create(gridId=str(request_coordinate_info_json["properties"]["gridId"]),
                                          gridx=str(request_coordinate_info_json["properties"]["gridX"]),
                                          gridy = str(request_coordinate_info_json["properties"]["gridY"]))
        
        record = coordinateWiseData.objects.get(gridx=str(request_coordinate_info_json["properties"]["gridX"]),
                                          gridy = str(request_coordinate_info_json["properties"]["gridY"]))
        record.longitude = longitude
        record.latitude = latitude
        
        storeTempertatureByDay(request_forcast_info_json, record)
        temp = getTemperatureByDay(day, record)
        
        record.lastupdated = ""
 
        return JsonResponse({
            "status": "OK",
            "sCode": 200,
            "day" : day,
            "temperature": temp
        }, status=200)




def storeTempertatureByDay(request_forcast_info_json, record):

    for period in request_forcast_info_json["properties"]["periods"]:
            

            if "Today" in period ["name"]:

                record.today = period["temperature"]
                record.save()
            
            elif "Tonight" in period ["name"]:

                record.tonight = period["temperature"]
                record.save()

            elif "Monday Night" in period["name"]:
                
                record.monday_night = period["temperature"]
                record.save()
            
            elif "Monday" in period["name"]: 
  
                record.monday = period["temperature"]
                record.save()

            elif "Tuesday Night" in period["name"]:

                record.tuesday_night = period["temperature"]
                record.save()

            elif "Tuesday" in period["name"]:

                  record.tuesday = period["temperature"]
                  record.save()

            elif "Wednesday Night" in period["name"]:

                  record.wednesday_night = period["temperature"]
                  record.save()

            elif "Wednesday" in period["name"]:

                  record.wednesday = period["temperature"]
                  record.save()
               
            elif "Thursday Night" in period["name"]:
                 
                  record.thursday_night = period["temperature"]
                  record.save()

            elif "Thursday" in period["name"]:
                
                  record.thursday = period["temperature"]
                  record.save()

            elif "Friday Night" in period["name"]:
            
                 record.friday_night = period["temperature"]
                 record.save()

            elif "Friday" in period["name"]:

                 record.friday = period["temperature"]
                 record.save()

            elif "Saturday Night" in period["name"]:

                 record.saturday_night = period["temperature"]
                 record.save()
            
            elif "Saturday" in period["name"]:

                record.saturday = period["temperature"]
                record.save()
            
            elif "Sunday Night" in period["name"]:
                
                record.sunday_night = period["temperature"]
                record.save()

            elif "Sunday" in period["name"]:
                 
                record.sunday = period["temperature"]
                record.save()
        




def getTemperatureByDay(day, record):
                        
            if day.lower() == "today":
                temp = record.today
                return temp
            elif day.lower() == "tonight":
                temp = record.tonight
                return temp
            elif day.lower() == "monday":
                temp = record.monday
                return temp
            elif day.lower() == "monday_night":
                temp = record.monday_night
                return temp
            elif day.lower() == "tuesday":
                temp = record.tuesday
                return temp
            elif day.lower() == "tuesday_night":
                temp = record.tuesday_night
                return temp
            elif day.lower() == "wednesday":
                temp = record.wednesday
                return temp
            elif day.lower() == "wednesday_night":
                temp = record.wednesday_night
                return temp
            elif day.lower() == "thursday":
                temp = record.thursday
                return temp
            elif day.lower() == "thursday_night":
                temp = record.thursday_night
                return temp
            elif day.lower() == "friday":
                temp = record.friday
                return temp
            elif day.lower() == "friday_night":
                temp = record.friday_night
                return temp
            elif day.lower() == "saturday":
                temp = record.saturday
                return temp
            elif day.lower() == "saturday_night":
                temp = record.saturday_night
                return temp
            elif day.lower() == "sunday":
                temp = record.sunday
                return temp
            elif day.lower() == "sunday_night":
                temp = record.sunday_night
                return temp

       
