from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password

AuthUser = get_user_model()


# # This is used for custom forms
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=128, required=True)
#     last_name = forms.CharField(max_length=128, required=True)
#     username = forms.CharField(max_length=128, required=True)
#     email = forms.EmailField(required=True)
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput,
#         help_text=password_validators_help_text_html()
#     )
#     password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#
#         try:
#             user = AuthUser.objects.get(username=username)
#         except AuthUser.DoesNotExist:
#             user = None
#
#         if user is not None:
#             raise forms.ValidationError('Username already taken.')
#
#         return username
#
#     def clean_password(self):
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         username = self.cleaned_data.get('username')  # in case username is not valid
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         if username is None:
#             return password
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email
#         )
#
#         validate_password(password, user=user)
#
#         return password
#
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data['password_confirmation']
#
#         if password is not None and password != password_confirmation:
#             # Check if password is None -> in this case it means password is not validated in previous method.
#             raise forms.ValidationError('Password is not confirmed!')
#
#         return password_confirmation
#
#     def save(self):
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         username = self.cleaned_data['username']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         # This method automatically saves user into database. Do not use it for register.
#         # user = AuthUser.objects.create(
#         #     first_name=first_name,
#         #     last_name=last_name,
#         #     username=username,
#         #     email=email,
#         # )
#         # user.set_password(password)
#         # user.save()
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#         )
#         user.set_password(password)
#         user.save()
#
#         return user

class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        # exclude = []
        fields = ('first_name', 'last_name', 'username', 'email')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html()
    )
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_password(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data.get('username')  # in case username is not valid
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if username is None:
            return password

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )

        validate_password(password, user=user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data['password_confirmation']

        if password is not None and password != password_confirmation:
            # Check if password is None -> in this case it means password is not validated in previous method.
            raise forms.ValidationError('Password is not confirmed!')

        return password_confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit is True:
            user.save()

        return user
