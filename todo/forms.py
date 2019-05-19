from django import forms
from django.contrib.auth.models import User
from todo.models import List

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        labels = {
            'username': '아이디',
            'password': '비밀번호',
            'email': '이메일'
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '문자, 숫자 및 @/./+/-/_ 문자만 포함될 수 있습니다.'
        self.fields['username'].error_messages['invalid'] = '올바른 아이디를 입력하십시오. 문자, 숫자 및 @/./+/-/_ 문자만 포함될 수 있습니다.'
        self.fields['username'].error_messages['unique'] = '이미 존재하는 아이디입니다.'
        self.fields['email'].error_messages['invalid'] = '올바른 이메일주소를 입력해주세요.'


class LoginForm(forms.ModelForm):
    password = forms.CharField(
        label = '비밀번호',
        strip=False,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['username'].widget.attrs['placeholder'] = 'ID'
        self.fields['password'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['password'].widget.attrs['placeholder'] = 'PASSWORD'


class TodoForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'context', 'priority', 'deadline')
        labels = {
            'title': '제목',
            'context': '내용',
            'priority': '우선순위',
            'deadline': '마감기한'
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['context'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].initial = 2
        self.fields['title'].widget.attrs['autocomplete'] = 'off'
        self.fields['deadline'].widget.attrs['autocomplete'] = 'off'
        self.fields['deadline'].error_messages['invalid'] = '올바른 날짜를 입력해주세요.'

