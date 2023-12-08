
from django.shortcuts import render
from django.views import View

from core.forms import FixedFoldForm
from core.managers.calculator_manager import FixedFoldManager


class CalcFixedFoldView(View):

    def get(self, request, *args, **kwargs):
        form = FixedFoldForm()
        return render(request, 'fixed_fold.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FixedFoldForm(request.POST)
        if form.is_valid():
            df = FixedFoldManager(
                form.cleaned_data.get("fold_approximated"),
                form.cleaned_data.get("interior_fold"),
                form.cleaned_data.get("awning_measure"),
                form.cleaned_data.get("cloth_measure"))
            lst = df.get_measure_list()
            form.is_valid()
            context = {
                'form': form,
                'info': {
                    'awning_measure': df.awning_measure,
                    'effective_fold': round(df.effective_fold, 2),  # misura piega
                    'cloth_measure': df.cloth_measure,  # misura stoffa
                    'interior_fold': round(df.interior_fold, 2),  # piega dentro
                    'fold_count': int(df.fold_count)
                },
                'result': lst
            }
            return render(request, 'fixed_fold.html', context)
        return render(request, 'fixed_fold.html', {'form': form})


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UnderCostructionView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'under_construction.html')
