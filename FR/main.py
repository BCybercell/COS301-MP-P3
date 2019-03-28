from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from .FacialRecognition import AuthenticateUser, getLog


def index(request):
    # return HttpResponse({'foo': 'bar'})
    return render_to_response('../index.html')

def AuthUser(request):
    if request.method =='GET':
        lImg = request.GET['Image']
        lUserID = AuthenticateUser(lImg)
        if lUserID > 0:
            return JsonResponse({'UserID': lUserID})
        else:
            return JsonResponse({'error': 'An error has occurred'})  # TODO fix
    if request.method == 'POST':
        lImg = request.body['Image']
        lUserID = AuthenticateUser(lImg)
        if lUserID > 0:
            return JsonResponse({'UserID': lUserID})
        else:
            return JsonResponse({'error': 'An error has occurred'})  # TODO fix


def Logs(request):
    return JsonResponse(getLog(request.GET['start'], request.GET['end']))

