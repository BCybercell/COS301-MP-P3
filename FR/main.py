from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .FacialRecognition import AuthenticateUser, getLog


@csrf_exempt
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


@csrf_exempt
def AuthUser(request):
    if request.method == 'GET':
        lImg = request.GET['Image']
        lUserID = AuthenticateUser(lImg)
        if lUserID > 0:
            return JsonResponse({'UserID': lUserID})
        else:
            return JsonResponse({'error': 'An error has occurred'})  # TODO fix
    if request.method == 'POST':


        try:
            if 'Image' in request.POST:
                lImg = request.POST['Image']
                # return JsonResponse({'error': 'Use a file and not a parameter'})  # TODO fix
            elif 'Image' in request.FILES:
                # if 'file' in request.FILES:
                lImg = request.FILES['Image']
            elif 'file' in request.FILES:
                # if 'file' in request.FILES:
                lImg = request.FILES['file']
            else:
                return JsonResponse({'error': 'An error has occurred'})  # TODO fix
                # else:
                #
            # else:
            #     lImg = request.FILES['Image']
            lUserID = AuthenticateUser(lImg)
        except:
            return JsonResponse({'error': 'An error has occurred'})  # TODO fix
        if lUserID > 0:
            return JsonResponse({'UserID': lUserID})
        else:
            return JsonResponse({'error': 'An error has occurred'})  # TODO fix


@csrf_exempt
def Logs(request):
    if request.method == 'GET':
        return JsonResponse(getLog(request.GET['start'], request.GET['end']), safe=False)
    if request.method == 'POST':
        return JsonResponse(getLog(request.POST['start'], request.POST['end']), safe=False)
