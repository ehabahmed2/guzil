from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image', 'stock', 'is_best_seller', 'is_available']
        widgets = {
            'is_best_seller': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_best_seller'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_available'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})