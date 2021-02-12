from django import forms
from .models import table_thickness_ground_plate_model
from django.forms import ModelForm, TextInput, DateTimeInput, DateTimeField



class create_thickness_ground_plate_form(ModelForm):
        class Meta:
            model = table_thickness_ground_plate_model
            fields = '__all__'
            widgets = {
                "number_shift":TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Номер смены'
                }),
                # "date_created": DateTimeInput(attrs={
                #     'class': 'form-control',
                #     'placeholder': 'Дата'
                # }),
                "value0": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Толщина плиты, мм'
                }),
                "value1": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 1'
                }),
                "value2": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 2'
                }),
                "value3": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 3'
                }),
                "value4": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 4'
                }),
                "value5": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 5'
                }),
                "value6": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 6'
                }),
                "value7": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 7'
                }),
                "value8": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Значение 8'
                })

            }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'