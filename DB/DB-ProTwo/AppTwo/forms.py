from django import forms
from AppTwo.models import User

# class UserForm(forms.Form):
#     f_name = forms.CharField()
#     l_name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField()
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("EMAILE MUSZA BYC TE SAME! DAWAJ STARY, TO NIE JEST TRUDNE!!!")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'
    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("EMAILE MUSZA BYC TE SAME! DAWAJ STARY, TO NIE JEST TRUDNE!!!")