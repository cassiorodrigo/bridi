from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50,)
    surname = forms.CharField(label='Surname', max_length=100, )
    email = forms.EmailField(label='Email address', max_length=120,)
    enquery1 = forms.CharField(label='Query', max_length=3000, widget=forms.Textarea,)
    check = forms.BooleanField()