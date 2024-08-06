from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Phone'}), max_value=999999999999,
    )
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'full_name': forms.TextInput(attrs={'class': '', 'placeholder': 'John Doe'}),
            'email': forms.TextInput(attrs={'placeholder': 'name@example.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'I need...', 'rows':'3'}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # if field_name is not 'date':
            field.widget.attrs['class'] = (field.widget.attrs.get('class') or '') + ' regular-input'
