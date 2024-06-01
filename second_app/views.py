from django.shortcuts import render
from .import forms
# Create your views here.
def Student_Model(request):
    student_form=forms.StudentForm()
    return render(request,'second_app/model_form.html',{'form':student_form})
