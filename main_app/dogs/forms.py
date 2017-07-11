from django import forms

from pagedown.widgets import PagedownWidget

from .models import Dog


class DogForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Dog
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'value', 'gender', 'breed', 'age']
