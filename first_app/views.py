from django.shortcuts import render
from .forms import StudentForms

# Create your views here.

def Student(request):
    if request.method=='POST':
        form=StudentForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form=StudentForms()
    return render(request,'first_app/forms.html',{'form':form})
