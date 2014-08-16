from django import forms

class RSSEntryListForm(forms.Form):
    title = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)