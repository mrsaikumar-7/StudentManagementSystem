from django import forms
from .models import facultyMember
from django.utils.translation import gettext_lazy as _

gender_list = [('Male', 'Male'),('Female','Female')]

class facultyRegister(forms.ModelForm):
    gender = forms.ChoiceField(widget = forms.RadioSelect(), choices=gender_list, required=False)
    class Meta:
        model = facultyMember
        fields = ['name','mail','branch','age','gender','password']
        # the forms are so useful in creating the user input forms
        # by using this ModelForms class we can easyly convert the pre existing models to forms
        # the WIDGETS
        # widgets is a dictionary used to modify the attributes and properties of the fields
        # every field's attributes (html attributes ex: class, id , type etc.,) can be changed using attrs which is again a dictionary 
        widgets = {
                 'name': forms.TextInput(attrs={'class': 'active form-control'}),
                 'mail': forms.TextInput(attrs={'class' : 'active text-primary form-control' , "id":'Id_email','type':'email'}),
                 'branch':forms.TextInput(attrs={'class' : 'form-control'}),
                 'age' : forms.NumberInput(attrs = { 'class': 'form-control'}),
                  'password' : forms.TextInput(attrs={'class':'form-control','type':'password'})
        }
        
        
    
    
    
    
    