from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#libs
import json
#forms
from Users.forms import UserForm
#models
from Users.models import Users

#Decorador para omitir el token de seguridad
@csrf_exempt
def create(request):
	if request.method == 'POST':
		message=""
		code="0000"
		#lectura del request 
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		new_user=body['pv']['usuario']
		#Validacion del canal
		if body['pf']['canal']=="ECO":
			#Evaluacion de los datos de entrada por medio de los formularios de django
			form = UserForm(new_user)
			if form.is_valid():
				#Evaluacion de existencia del email
				count_email=len(Users.objects.filter(email=new_user['email']))
				if count_email==0:
					#Creacion de registro en la base de datos
					user=Users.objects.create(
						name=new_user['name'],
						password=new_user['password'],
						email=new_user['email']
						)
					id_user=str(user.pk)
					message="The process was satisfactory"
				else:
					message="This email is in the data base"
					code="0003"
					id_user="null"

			else:
				message=form.errors
				code="0002"
				id_user="null"
		else:
			message="The canal isn't ECO"
			code="0001"
			id_user="null"

		response={
		'app':{'code':code,
				'mensaje':message
				},
		'pv':{
			'usuario':{
				'id':id_user,
				'name':new_user['name'],
				'password':new_user['password'],
				'email':new_user['email']
				}
			}
		}
		return JsonResponse(response)
	return HttpResponse('The method sent was not a POST method')


