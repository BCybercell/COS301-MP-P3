from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .FacialRecognition import AuthenticateUser, getLog


def index(request):
    return HttpResponse("<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='author' content='Tegan "
                        "Carton-Barber'><link rel='stylesheet' "
                        "href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' "
                        "integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' "
                        "crossorigin='anonymous'><title>Facial Recognition</title></head><body><form action='#' "
                        "method='post' enctype='multipart/form-data' style='padding:4rem;'><div "
                        "class='form-group'><input type='file' name='fileToUpload' id='fileToUpload' "
                        "class='form-control'></div><input type='submit' value='Upload Image' name='submit' "
                        "class='btn btn-secondary'></form></body></html>")
    # return render()


def AuthUser(request):
    if request.method == 'GET':
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
    if request.method == 'GET':
        return JsonResponse(getLog(request.GET['start'], request.GET['end']), safe=False)
    if request.method == 'POST':
        return JsonResponse(getLog(request.body['start'], request.body['end']), safe=False)


@csrf_exempt
def test(request):
    if request.method == 'POST':
        return HttpResponse('yata')
