from django.forms import Widget, NumberInput
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django import forms

from core.managers.calculator_manager import FixedFoldManager


class WaveForm(forms.Form):
    fold_approximated = forms.FloatField(label="Misura della piega", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6', 'style': 'margin-right: 23px'}))
    interior_fold = forms.FloatField(label="Piega dentro", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6'}))
    awning_measure = forms.FloatField(label="Misura tenda", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control col-md-6'}))
    cloth_measure = forms.FloatField(label="Misura stoffa", widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control'}))


class CalcFixedFold(View):

    def get(self, request, *args, **kwargs):
        form = WaveForm()
        return render(request, 'fixed_fold.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = WaveForm(request.POST)
        if form.is_valid():
            df = FixedFoldManager(
                form.cleaned_data.get("fold_approximated"),
                form.cleaned_data.get("interior_fold"),
                form.cleaned_data.get("awning_measure"),
                form.cleaned_data.get("cloth_measure"))
            lst = df.get_measure_list()
            form.is_valid()

            return render(request, 'fixed_fold.html', {'form': form, 'result': lst})
        return render(request, 'fixed_fold.html', {'form': form})


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UnderCostructionView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'under_construction.html')
