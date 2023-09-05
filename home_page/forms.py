
from django import forms
from .models import Review

class ReviewFrom(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ratting','comment']
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['ratting'].widget.attrs.update({'class':'form-control'})
        self.fields['comment'].widget.attrs.update({'class':'form-control'})
