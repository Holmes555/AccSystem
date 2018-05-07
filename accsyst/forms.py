from django import forms

from .models import *


class BillForm(forms.ModelForm):
    salary = forms.IntegerField(help_text='Set the salary.', required=True)
    hours = forms.IntegerField(help_text='Working hours.', required=False)

    class Meta:
        model = Bill
        fields = '__all__'


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['extra_hours', 'day_hours', 'extra_coeff']

    def clean_working_hours(self):
        cleaned_data = super(CardForm, self).clean()
        working_hours = cleaned_data.get('working_hours')
        if working_hours < 0 or working_hours > 24:
            raise forms.ValidationError('Enter correct working hours')


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'
