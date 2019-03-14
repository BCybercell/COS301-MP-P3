from django.http import HttpResponse
from django.http import JsonResponse
from .FacialRecognition import AuthenticateUser, getLog


def index(request):
    return JsonResponse({'foo': 'bar'})


def AuthUser(request):
    lImg = request.GET['Image']
    lUserID = AuthenticateUser(lImg)
    if lUserID > 0:
        return JsonResponse({'UserID': lUserID})
    else:
        return JsonResponse({'error': 'No user ID found'})


def Logs(request):
    return getLog(request.GET['start'], request.GET['end'])
