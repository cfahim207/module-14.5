from django import forms
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class StudentForms(forms.Form):
    name=forms.CharField(max_length=20,initial='FAHIM CHOWDHURY')
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email=forms.EmailField(label="Please enter your email address",)
    agree=forms.BooleanField(initial=True)
    birthday=forms.DateField(widget=forms.NumberInput(attrs=({'type':'date'})))
    birthyear=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    day=forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    MultipleChoice=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)