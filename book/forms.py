from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)