from django.http import HttpResponse
from django.shortcuts import render
from django.views import View



from django import forms


class WaveForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    interval = forms.DurationField(label="sdgfdg")
# Create your views here.
class CalcWaves(View):


    def get(self, request, *args, **kwargs):
        form = WaveForm()
        return render(request, 'base.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = WaveForm()
        if form.is_valid():
            form.save()
            return redirect('calcwave')
        return render(request, 'base.html', {'form':form})


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})
 
    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
 
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


