from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image_a = forms.ImageField(
        label='Image_a', required=False, widget=CustomClearableFileInput)
    image_b = forms.ImageField(
        label='Image_b', required=False, widget=CustomClearableFileInput)
    image_c = forms.ImageField(
        label='Image_c', required=False, widget=CustomClearableFileInput)
    image_d = forms.ImageField(
        label='Image_d', required=False, widget=CustomClearableFileInput)    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_brand = [(b.id, b.get_friendly_name()) for b in brands]

    
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['brand'].choices = friendly_names_brand
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 form-fields'