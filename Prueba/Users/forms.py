from django import forms
#validaciones pertinentes 
class UserForm(forms.Form):
	name = forms.CharField(max_length=200,required=True)
	password = forms.CharField(max_length=50,required=True)
	email = forms.EmailField(required=True)