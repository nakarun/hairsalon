from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomerUser


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # placeholderにフィールドのラベルを入れる
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = CustomerUser
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # placeholderにフィールドのラベルを入れる
            field.widget.attrs['placeholder'] = field.label