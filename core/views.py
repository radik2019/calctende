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
            fold_approximated = form.cleaned_data.get("fold_approximated")
            interior_fold = form.cleaned_data.get("interior_fold")
            awning_measure = form.cleaned_data.get("awning_measure")
            cloth_measure = form.cleaned_data.get("cloth_measure")
            df = FixedFoldManager(
                fold_approximated, interior_fold, awning_measure, cloth_measure)
            error_message = df.error_message()
            if error_message:
                return render(request, 'fixed_fold.html', {'form': form, 'error_message': error_message})
            lst = df.get_measure_list()
            context = {
                'form': form,
                'info': {
                    'awning_measure': df.awning_measure,
                    'effective_fold': round(df.effective_fold, 2),  # misura piega
                    'cloth_measure': df.cloth_measure,  # misura stoffa
                    'interior_fold': round(df.interior_fold, 2),  # piega dentro
                    'fold_count': int(df.fold_count),
                    'folding_overlay':  round((lst[1]['distance'] - lst[0]['distance']) / 2, 2)
                },
                'result': lst
            }
            return render(request, 'fixed_fold.html', context)
        return render(request, 'fixed_fold.html', {'form': form})


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home_page.html')


class UnderCostructionView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'under_construction.html')


class WhoWeAreView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'who_we_are.html')
