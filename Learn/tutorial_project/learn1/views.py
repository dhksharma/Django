from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint

# Create your views here.


def index(request):
    return render(request, 'learn1/index.html')


def contact(request):
    return render(request, 'learn1/contact.html')


def about(request):
    return render(request, 'learn1/about.html')


def route_param(request):
    context = {
        "data": {
            "user_id": 1,
            "f_name": "Dharmendra",
            "l_name": "Sharma"
        }
    }
    return render(request, 'learn1/route_param.html', context)


def parameter_method(request, id, name):

    req_params = {
        'id': id,
        'name': name
    }
    pprint(req_params)
    return HttpResponse(str(req_params))


def json_data(request, json_data):

    pprint(json_data)
    return HttpResponse(json_data)


def call_get_ajax(request):
    if request.method == 'GET':
        all_request_data = request.GET.dict()
        response = {
            'code': 200,
            'status': True,
            'message': 'Data processed successfully',
            'data': all_request_data,
        }
        return JsonResponse(response, status=200)
    else:
        response = {
            'code': 422,
            'status': False,
            'message': 'Unprocessable request data',
            'data': {},
        }
        return JsonResponse(response, status=200)


def call_post_ajax(request):
    if request.method == 'POST':
        all_request_data = request.POST.dict()
        response = {
            'code': 200,
            'status': True,
            'message': 'Data processed successfully',
            'data': all_request_data,
        }
        return JsonResponse(response, status=200)
    else:
        response = {
            'code': 422,
            'status': False,
            'message': 'Unprocessable request data',
            'data': {},
        }
        return JsonResponse(response, status=200)
