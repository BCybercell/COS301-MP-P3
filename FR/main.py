from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .FacialRecognition import AuthenticateUser, syncList, AddImages, checkClientOperation
from bson import BSON #added
from pprint import pprint
import json
from django.shortcuts import render

@csrf_exempt
def index(request):
    return HttpResponse("<!DOCTYPE html><html>  <head>    <meta charset='utf-8'>    <meta name='author' content='Kyle Olivier 15001319'>    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>"
    "    <link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.1.0/css/all.css' integrity='sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt' crossorigin='anonymous'>"
    "    <title>Facial Recognition</title>    <div style='background-color:black'><img src='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/First_National_Bank_Logo.svg/1200px-First_National_Bank_Logo.svg.png' alt='Connection too slow' style='width:200px;height:100px;'></div>"
    "  </head>  <body>  <div class='container'>		<br/><br/>		<section id='forms'>			<div class='row'>				<div class='col-12'>					<div class='card'>"
    "						<div class='card-header' style='font-family:Open Sans, sans-serif; font-size: 18px; font-weight: bold;'>Add photos to your account</div>						<div class='card-body'>"
    "							<form action='/upImage/' method='post' enctype='multipart/form-data'>								<fieldset>									<div class='row'>"
    "										<div class='col-4'>											<label for='userID'>User ID:</label>											<input type='text' id='userID' class='form-control' placeholder='123456789' name='userID'>"
    "										</div>										<div class='col-8'>											<label for='loginPass'>Select your images:</label>"
    "											<input type='file' id='picToUpload' class='form-control' name='picToUpload' multiple='multiple'>										</div>"
    "									</div>									<div class='row mt-5'>										<div class='col-12'>"
    "											<button type='submit' class='btn btn-dark' id='submitButton'>Upload images <i class='fa fa-angle-right'></i></button>										</div>"
    "									</div>								</fieldset>							</form>						</div>					</div>"
    "				</div>			</div>		</section>	<div>  </body></html>")
    # return render()


@csrf_exempt
def UpImage(request):
    if request.method == 'POST':
        if 'picToUpload' in request.POST:
            lImg = request.POST['picToUpload']
            #lImg2 = request.FILES['picToUpload'][1]    this attempt doesn't work
        elif 'picToUpload' in request.FILES:
            lImg = request.FILES['picToUpload']
            #lImg2 = request.FILES['picToUpload'][1]    this did not work
        else:
            return JsonResponse({'status':True, 'error': 'An error has occurred here'})  # TODO fix
        if not lImg:
            return JsonResponse({'Error': 'No image was selected'})
        lUser = request.POST['userID']
        #images =[]
        #images.append(lImg)
        #images.append(lImg2)
        tmp = AddImages(lUser, lImg)
        if tmp:
            return JsonResponse({'Status':'Success: image uploaded to userID: ' + lUser})
        else:
            return JsonResponse({'Status': 'The userID entered does not exist. UserID: ' + lUser})
    else:
        return JsonResponse({'Error': 'POST was not used'})


@csrf_exempt
def AuthUser(request):
    # if request.method == 'GET':
    #     lImg = request.GET['Image']
    #     lUserID = AuthenticateUser(lImg)
    #     if lUserID > 0:
    #         return JsonResponse({'UserID': lUserID})
    #     else:
    #         return JsonResponse({'error': 'An error has occurred'})  # TODO fix
    if request.method == 'POST':
        # try:
        if 'Image' in request.POST:
            lImg = request.POST['Image']

        elif 'Image' in request.FILES:

            # remove
            lImg = request.FILES['Image']
        elif 'file' in request.FILES:

            lImg = request.FILES['file']
        else:
            return JsonResponse({'status': False, 'Error': 'An error has occurred'})  # TODO fix
        lUserID = AuthenticateUser(lImg)
        if 'userID' in lUserID:
            tempDict = {'status': True}
        else:
            tempDict = {'status': False}
        tempDict.update(lUserID)
        return JsonResponse(tempDict)
    # except:
        return JsonResponse({'status': False, 'Exception': "Not Authenticated"})  # TODO fix

##################################
#        Endpoint for CIS
##################################
@csrf_exempt
def Clients(request):
    # if request.method == 'GET':
    #     dictionary = {
    #         'Operation': request.GET['Operation'],
    #         'ID': request.GET['ID']
    #     }
    #     return JsonResponse(syncList(dictionary), safe=False)
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        dictionary = {
            'Operation': received_json_data['Operation'],
            'ID': received_json_data['ID']
        }
        return JsonResponse(checkClientOperation(dictionary), safe=False)
    else:
        return JsonResponse({'error': 'use post'})



@csrf_exempt
def Demo(request):
    return HttpResponse("<!DOCTYPE html><html> <head> <meta charset='utf-8'> <meta name='author' content='Kyle Olivier 15001319'> <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'> <link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.1.0/css/all.css' integrity='sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt' crossorigin='anonymous'> <title>Facial Recognition</title> <div style='background-color:black'><img src='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/First_National_Bank_Logo.svg/1200px-First_National_Bank_Logo.svg.png' alt='Connection too slow' style='width:200px;height:100px;'></div></head> <body> <div class='container'><br/><br/><section id='forms'><div class='row'><div class='col-md-8 m-auto'><h1 class='text-center display-6 my-6'>Choose an image to test for authentication</h1></div></div><br/><div class='row'><div class='col-md-6 m-auto'><form action='https://cos301frocean.herokuapp.com/AuthenticateUserTest/' method='post' enctype='multipart/form-data'><div class='custom-file mb-3'><input type='file' name='Image' value='' placeholder='' class='custom-file-input'><label for='loginPass' class='custom-file-label'>Select image:</label></div><button type='submit' class='btn btn-dark btn-block' id='submitButton'>Authenticate image <i class='fa fa-angle-right'></i></button></form></div></div></section><div> </body></html>")
