from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django import forms

from core.managers.calculator_manager import FixedFold


class WaveForm(forms.Form):
    fold_approximated = forms.FloatField(label="misura della piega")
    interior_fold = forms.FloatField(label="piega dentro")
    awning_measure = forms.FloatField(label="misura tenda")
    cloth_measure = forms.FloatField(label="misura stoffa")



class CalcWaves(View):

    def get(self, request, *args, **kwargs):
        form = WaveForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = WaveForm(request.POST)
        if form.is_valid():

            df = FixedFold(
                form.cleaned_data.get("fold_approximated"),
                form.cleaned_data.get("interior_fold"),
                form.cleaned_data.get("awning_measure"),
                form.cleaned_data.get("cloth_measure"))

            lst = df.get_measure_list()
            form.is_valid()

            return render(request, 'base.html', {'form': form, 'result': lst})
        return render(request, 'base.html', {'form': form})
