from django import forms
from django.core.validators import URLValidator
class urlForm(forms.Form):
    url = forms.CharField(
        label='',

        widget = forms.TextInput(

            attrs={
                "class":"form-control",
                "placeholder":"Enter The Url",
            }

        )
    )

    def clean(self):
        cleaned_data = super(urlForm,self).clean()
        url = cleaned_data.get("url")
        try:
            URLValidator(url)

        except:
            raise forms.ValidationError("Invalide URL")
        return url
