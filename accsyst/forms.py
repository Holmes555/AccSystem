from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import *


class BillForm(forms.ModelForm):
    salary = forms.IntegerField(help_text='Set the salary.', required=True)
    hours = forms.IntegerField(help_text='Working hours.', required=False)

    class Meta:
        model = Bill
        fields = '__all__'


class CardForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget, initial=timezone.now(), help_text='Set the date.')
    working_hours = forms.IntegerField(help_text='Set working hours.')
    rate = forms.IntegerField(help_text='Set the rate.', required=False)
    fix_salary = forms.IntegerField(help_text='Set fix salary.', required=False)
    payment = forms.ChoiceField(help_text='Set the payment.', choices=Card.PAYMENT_CHOICE)

    class Meta:
        model = Card
        exclude = ['extra_hours', 'day_hours', 'extra_coeff']

    def clean(self):
        cleaned_data = super(CardForm, self).clean()
        rate = cleaned_data.get('rate')
        fix_salary = cleaned_data.get('fix_salary')
        cleaned_data = super(CardForm, self).clean()
        working_hours = cleaned_data.get('working_hours')
        if working_hours < 0 or working_hours > 24:
            raise forms.ValidationError('Enter correct working hours')
        if rate and fix_salary:
            raise forms.ValidationError('Choose only one way')
        if not (rate or fix_salary):
            raise forms.ValidationError('Choose at least one way')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ['accountants']


class AdminReportForm(forms.ModelForm):
    class Meta:
        model = AdminReport
        exclude = ['accountants', 'admin']


class UserInfoForm(forms.ModelForm):
    name = forms.CharField(help_text='Enter name.')
    surname = forms.CharField(help_text='Enter surname.')
    age = forms.IntegerField(help_text='Enter age.')
    address = forms.CharField(help_text='Enter address.')
    picture = forms.ImageField(help_text='Enter picture (optionally).', required=False)

    class Meta:
        model = UserInfo
        fields = '__all__'
