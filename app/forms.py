from django import forms
class PostForm(forms.Form):
    tirle = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())