from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Title placeholder"}))
    description = forms.CharField(  required=False, 
                                    widget=forms.Textarea(
                                            attrs={
                                                "class": "new_class_name two",
                                                "id": "my-id-for-textarea",
                                                "rows": 10,
                                                "columns": 5,
                                                "placeholder":"description placeholder"
                                            }
                                    ))
    price       = forms.DecimalField(initial=199.99)