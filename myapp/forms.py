from django import forms

class Email(forms.Form):
    name=forms.CharField(max_length=20, required=False)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea() )
    
