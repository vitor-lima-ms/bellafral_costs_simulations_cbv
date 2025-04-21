from django import forms
from fralda.models import Fralda

class FraldaUpdateForm(forms.ModelForm):
    class Meta:
        model = Fralda
        fields = '__all__'