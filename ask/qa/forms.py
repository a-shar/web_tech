# coding=utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=1024, label="Заголовок вопроса")
    text = forms.CharField(widget=forms.Textarea, label="Текст вопроса")

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError(u'Заголовок не может быть пустым', code=12)
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(u'Вопрос не может быть пустым', code=13)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self.author
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question')
        widgets = {
            "question" : forms.HiddenInput(),
        }
    # text = forms.CharField(widget=forms.Textarea, label="Текст ответа")
    # question = forms.IntegerField(widget=forms.HiddenInput(), label=None)
    #
    # def clean_question(self):
    #     return self.cleaned_data["question"]
    #
    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     if not text:
    #         raise forms.ValidationError(u'Ответ не может быть пустым', code=13)
    #     return text
    #
    # def save(self):
    #     answer = Answer(**self.cleaned_data)
    #     answer.author = User.objects.get(pk=1)
    #     answer.save()
    #     return answer


class SignupForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email",)

    def save(self, commit=True):
        user = super(forms.ModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
