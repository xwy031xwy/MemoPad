from django import forms
from memo.models import Memo
class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['id', 'content', 'created_at']
    content = forms.CharField(
    label="Content",
     max_length=30,
    required=True,
    widget=forms.TextInput(attrs={'size': '30'}),
    )
    created_at = forms.DateField(
    label='Created at',
    required=False,
    input_formats=['%Y-%m-%d'],
    widget=forms.TextInput(attrs={'size': '12'}),
 )