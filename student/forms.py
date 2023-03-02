from django import forms 
from .models import library

class libraryForm(forms.ModelForm):
    class Meta:
        model = library
        fields  = '__all__' 
        
        widgets ={
            'book_id' :forms.NumberInput(attrs={'class':'form-control'}),
            'book_name': forms.TextInput(attrs={'class':'form-control'}),
            'book_author':forms.TextInput(attrs={'class':'form-control'}),
            'publication_date':forms.DateInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'})
                    
        }