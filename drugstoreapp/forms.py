from django import forms
from drugstoreapp.models import *


class PersonSignUpForm(forms.Form):
        username = forms.CharField(max_length=50,required=True)
        first_name = forms.CharField(max_length=50,required=True)
        last_name = forms.CharField(max_length=50,required=True)
        email = forms.EmailField(max_length=30, required=True)
        password = forms.CharField(max_length=30,required=True)
        are_you_mariz = forms.BooleanField(required=True)

class PersonLoginForm(forms.Form):
        username = forms.CharField(max_length=30,required=True)
        password = forms.CharField(max_length=15,required=True, widget=forms.PasswordInput)

class DrugNameForm(forms.Form):
        Name = forms.CharField(max_length=30, required=True)

class DrugstoreNameForm(forms.Form):
        Name = forms.CharField(max_length=30, required=True)

class ordersForm(forms.Form):
        USERNAME_FIELD = 'Email'
        Drugstore_name = forms.ModelMultipleChoiceField(queryset=DrugStore.objects.all(), required=True)
        Drug_name = forms.ModelMultipleChoiceField(queryset=Drug.objects.all(), required=True)
        Number = forms.IntegerField(required=True)

class whereISDrugForm(forms.Form):
        name = forms.ModelMultipleChoiceField(queryset=Drug.objects.all(), required=True)