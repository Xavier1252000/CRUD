from django import forms
from django.forms import widgets
from enroll.models import User

# Create the form class.
class UserForm(forms.ModelForm):

    class Meta:
    
        model = User
    
        fields = ['name', 'email', 'phone_no', 'password']


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

# Creating a form to add an article
form = UserForm()
