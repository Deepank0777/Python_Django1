from django import forms

# valid form for ulpad data
class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100)
    description = forms.CharField(max_length = 100)
    share1 = forms.CharField(max_length=100)
    share2 = forms.CharField(max_length=100)
    picture = forms.FileField()