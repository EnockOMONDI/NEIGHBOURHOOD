from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Creating forms
class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'E-mail Address'
        self.fields['password1'].label = 'Account password'
        self.fields['password2'].label = 'Confirm account password'
