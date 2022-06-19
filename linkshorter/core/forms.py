from django import forms 
from .models import Link 

class ShortLinkForm(forms.ModelForm):
    original_url = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your url here ....'}
    ))

    class Meta:
        model = Link 
        
        fields = ('original_url',)