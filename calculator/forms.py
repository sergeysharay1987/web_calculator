from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp
from .validators import check_if_floordiv, check_char_in_string


class ExpForm(forms.ModelForm):
    expression = forms.CharField(error_messages={'required': 'Please enter your expression'},
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}),
                                 help_text='Enter expression')
    result_of_expression = forms.CharField(required=False,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['expression', 'result_of_expression']


    def clean(self):
        cleaned_data = super(ExpForm, self).clean()
        expression = cleaned_data.get('expression')
        # result_of_expression = cleaned_data['result_of_expression']
        try:
            cleaned_data['result_of_expression'] = eval(expression, {'__builtins__': {}})
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except (NameError, SyntaxError, KeyError, IndexError, TypeError):
            raise ValidationError('You have entered invalid data')
        else:
            if check_if_floordiv(expression) or not check_char_in_string(expression):
                raise ValidationError('You have entered invalid data')
        return cleaned_data
