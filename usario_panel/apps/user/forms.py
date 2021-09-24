from django import forms
from .models import User
class UserForm(forms.ModelForm):
    confirmed_pw = forms.CharField()
    class Meta:
        model = User
        fields = '__all__'


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmed_pw")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_pw does not match"
            )