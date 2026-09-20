from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea
    )
    rating = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=5
    )
    screenshot = forms.ImageField(required=False)