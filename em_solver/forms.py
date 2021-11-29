from django import forms

class InputData(forms.Form) :
    xValue = forms.CharField()
    yValue = forms.CharField()
    