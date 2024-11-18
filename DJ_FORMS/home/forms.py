from django import forms

class Studentform(forms.Form):
    
    name = forms.CharField(max_length=20)
    usn = forms.CharField(max_length=10)
    mobile = forms.CharField(max_length=10)
    course = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows': 5, 'cols':20}))
    

    