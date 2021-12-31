# django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

# Django third party imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewUserForm(UserCreationForm):
    '''
    Form to register new user
    '''
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username", "email", "password1",
            "password2", "company_name"
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # using crispy form helper class to create
        # whole form in template
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    '''
    Form to edit profile
    '''
    class Meta:
        model = User
        fields = (
            'phone_no', 'email', 'company_name',
            'first_name', 'last_name', 'bio',
            'location', 'birth_date',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # using crispy form helper class to create
        # whole form in template
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))