from .models import Person
from django.forms import ModelForm, TextInput, Textarea

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'description']
        widgets ={
                "name":TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Введите имя'
                }),
                "description":Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание'
                }),
            }




