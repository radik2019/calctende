
from django.contrib import admin
from django.urls import path

from core.views import CalcFixedFoldView, HomeView, UnderCostructionView, WhoWeAreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('under_costruction', UnderCostructionView.as_view(), name='under_costruction'),
    path('', HomeView.as_view(), name='homepage'),
    path('calcwave/', CalcFixedFoldView.as_view(), name='calcwave'),
    path('who_we_are/', WhoWeAreView.as_view(), name='who_we_are')

]
