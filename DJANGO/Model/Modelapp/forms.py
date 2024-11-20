from django import forms
from .models import student
class studentform(forms.ModelForm):
    class Meta:#inner class for your model class
        model=student
        fields=["name","age","phno"]