
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('form/',views.Student, name='student'),
   
]
