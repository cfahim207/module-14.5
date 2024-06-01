
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('Model/',views.Student_Model, name='StudentModel'),
   
]
