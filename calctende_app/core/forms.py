
from django import forms


class FixedFoldForm(forms.Form):
    fold_approximated = forms.FloatField(label="Misura della piega", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6', 'style': 'margin-right: 23px'}))
    interior_fold = forms.FloatField(label="Piega dentro", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6'}))
    awning_measure = forms.FloatField(label="Misura tenda", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6'}))
    cloth_measure = forms.FloatField(label="Misura stoffa", widget=forms.widgets.NumberInput(
        attrs={'class': "form-control col-md-6'"}))
