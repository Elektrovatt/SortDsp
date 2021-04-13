from django import forms
from .models import *
from django.forms import ModelForm, TextInput



class create_thickness_ground_plate_form(ModelForm):
        class Meta:
            model = table_thickness_ground_plate_model
            fields = ['value0','value1','value2','value3','value4','value5','value6','value7','value8']
            widgets = {
                "is_customer": TextInput(attrs={'class': 'form-control','placeholder': 'Автор'}),
                "value0": TextInput(attrs={'class': 'form-control','placeholder': 'Толщина плиты, мм'}),
                "value1": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 1' }),
                "value2": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 2'}),
                "value3": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 3'}),
                "value4": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 4'}),
                "value5": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 5'}),
                "value6": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 6'}),
                "value7": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 7'}),
                "value8": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 8'})

            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class Pack_of_board_form(ModelForm):
    class Meta:
        model = Table_Pack_Board_Model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8',
                  'value9','value10','value11','value12','value13','value14','value15','value16','value17','value18',
                  'value19','value20','value21','value22']
        widgets = {
            "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
            "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
            "value6": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 6'}),
            "value7": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 7'}),
            "value8": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 8'}),
            "value9": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 9'}),
            "value10": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 10'}),
            "value11": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 11'}),
            "value12": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 12'}),
            "value13": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 13'}),
            "value14": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 14'}),
            "value15": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 15'}),
            "value16": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 16'}),
            "value17": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 17'}),
            "value18": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 18'}),
            "value19": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 19'}),
            "value20": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 20'}),
            "value21": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 21'}),
            "value22": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 22'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'