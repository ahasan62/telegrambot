from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#Create your views 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render 

import json
def write_json(data,filename='responselog.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def index(request, methods=['POST','GET']):
    print(request)
    if request.method == "GET":
   #     msg = request.get.json()
       #   data = json.loads(request.body)
        # label = data['label']
        # url = data['url']
        
        data = request.POST
        print("----------------------------")
        print(data)
        return HttpResponse(data) 

     #   return HttpResponse("Hello World! get")    
    else:    
        
        return HttpResponse("Hello World! POST")