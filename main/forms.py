from django import forms
from .models import *
from django.forms import ModelForm, TextInput



class Thickness_board_form(ModelForm):
        class Meta:
            model = Thickness_board_model
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


class Thickness_pack_board_form(ModelForm):
    class Meta:
        model = Thickness_pack_board_model
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


class Thickness_unpolished_pack_board_form(ModelForm):
    class Meta:
        model = Thickness_pack_board_model
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



class Thickness_unpolished_board_form(ModelForm):
    class Meta:
        model = Thickness_unpolished_board_model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4', 'value5']
        widgets = {
                "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
                "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
                "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
                "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
                "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
                "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
                "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Number_tapes_form(ModelForm):
    class Meta:
        model = Number_tapes_model
        fields = [
                  'number_1_1_choices', 'value0',
                  'number_1_2_choices', 'value1',
                  'number_2_1_choices','value2','liner_2_1_choices',
                  'number_2_2_choices','value3','liner_2_2_choices',
                  'number_2_3_choices','value4', 'liner_2_3_choices',
                  'number_2_4_choices','value5','liner_2_4_choices']
        # # widgets = {
        # #     "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
        # #     "number_1_1_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
        # #     "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
        # #     "number_1_2_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
        # #     "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
        # #     "number_2_1_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
        # #     "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
        # #     "liner_2_1_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 6'}),
        # #     "number_2_2_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 7'}),
        # #     "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 8'}),
        # #     "liner_2_2_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 9'}),
        # #     "number_2_3_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 10'}),
        # #     "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 11'}),
        # #     "liner_2_3_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 12'}),
        # #     "number_2_4_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 13'}),
        # #     "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 14'}),
        # #     "liner_2_4_choices": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 15'}),
        #
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

