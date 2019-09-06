from django import forms
from .models import Goods

class GoodsForm(forms.ModelForm):
    
    class Meta:
        model = Goods

        fields = (
            "nameGoods",
            "descriptionGoods",
            "typeGoods",
            "conditionGoods",
            "priceGoods",
            "imagesGoods"
        )

        labels = {
            "nameGoods" : "Nama ",
            "descriptionGoods" : "Deskripsi ",
            "typeGoods" : "Tipe ",
            "conditionGoods" : "Kondisi ",
            "imagesGoods" : "Gambar Barang ",
        }

        choicesTypeGoods = [
            ('keyboard', 'Keyboard'),
            ('laptop', 'Laptop'),
            ('partComputer', 'Part Computer'),
            ('monitor', 'Monitor'),
            ('mouse', 'Mouse'),            
        ]

        choicesConditionGoods = [
            ('new', 'Baru'),
            ('used', 'Bekas')
        ]

        widgets = {
            'nameGoods':forms.TextInput(
                attrs = {
                    'class':'nameGoods',
                    'id':'nameGoods',
                    'max_length':50
                }
            ),
            'descriptionGoods':forms.Textarea(
                attrs = {
                    'class':'descriptionGoods',
                    'id':'descriptionGoods'
                }
            ),
            'typeGoods':forms.Select(
                choices = choicesTypeGoods,
                attrs = {
                    'class':'typeGoods',
                    'id':'typeGoods'
                }
            ),
            'conditionGoods':forms.RadioSelect(
                choices = choicesConditionGoods,
                attrs = {
                    'class':'conditionGoods',
                    'id':'conditionGoods'
                }
            ),
            'priceGoods':forms.NumberInput(
                attrs = {
                    'class':'priceGoods',
                    'id':'conditionGoods'
                }
            ),
            'imagesGoods':forms.FileInput(
                 attrs = {
                     'class':'imagesGoods',
                     'id':'imagesGoods'
                 }
             )
        }


class RegisterForm(forms.Form):
    username        = forms.CharField(
        max_length = 50,
        widget = forms.TextInput,
        label = "Username "
    )

    email           = forms.EmailField(
        widget = forms.EmailInput,
        label = "Email "
    )

    password        = forms.CharField(
        max_length = 40,
        widget = forms.PasswordInput,
        label = "Password "
    )
    passwordrepeat  = forms.CharField(
        max_length = 40,
        widget = forms.PasswordInput,
        label = "Ulangi Password "
    )
    firstname       = forms.CharField(
        max_length = 20,
        widget = forms.TextInput,
        label = "Nama Depan "
    )
    lastname        = forms.CharField(
        max_length = 20,
        widget = forms.TextInput,
        label = "Nama Akhir "
    )
