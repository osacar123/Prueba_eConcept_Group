from django.urls import path
from Users import views

urlpatterns = [
    
    path('create_user',views.create),
]
