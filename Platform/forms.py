from django import forms
from .models import Post, User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class PostForm(forms.ModelForm):
    text_content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'What\'s on your mind?',
                'class': 'textarea',
            }
        ),
        label='',
    )

    class Meta:
        model = Post
        exclude = ('owner', )


class MyUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.widgets.TextInput(
        attrs={
            'placeholder': 'Username',
            'class': 'textinput',
        }),
        label=''
    )
    password = forms.CharField(widget=forms.widgets.PasswordInput(
        attrs={
            'placeholder': '*********',
            'class': 'textinput',
        }),
        label='',
    )


class MyUserCreationForm(UserCreationForm):
    username = forms.RegexField(max_length=30, regex=r'^[-\w]+$',
                                help_text=_('Maximum 30 characters. Only letters, digits and underscores are allowed.'),
                                error_messages={'invalid': _("This input must contain only letters, numbers and"
                                                             " underscores.")},
                                widget=forms.widgets.TextInput(
                                    attrs={
                                        'placeholder': 'Username',
                                        'class': 'textinput',
                                    }
                                ),
                                label='',
                                )
    email = forms.EmailField(widget=forms.widgets.EmailInput(
        attrs={
            'placeholder': 'Email address',
            'class': 'textinput',
        }),
        label='',
    )

    password1 = forms.CharField(widget=forms.widgets.PasswordInput(
        attrs={
            'placeholder': '*********',
            'class': 'textinput',
        }),
        label='',
    )
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(
        attrs={
            'placeholder': '*********',
            'class': 'textinput',
        }),
        label='Confirm password',
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )


