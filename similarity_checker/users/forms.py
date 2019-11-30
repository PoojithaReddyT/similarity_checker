from django.forms import ModelForm
from django import forms
from users.models import File1,File2
class FilesCreate(ModelForm):
    class Meta:
        model=File1
        #fields={'firstfile',}
        exclude=()
        widgets={'firstfile':forms.Textarea(attrs={'cols':50,'rows':50})}