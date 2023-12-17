from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from core.views import CalcFixedFoldView, HomeView, UnderCostructionView, WhoWeAreView
from calc_api import views

router = SimpleRouter()
router.register(r'snippets', views.CalcFixedFoldAPIView, basename='snippet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('under_costruction/', UnderCostructionView.as_view(), name='under_costruction'),
    path('', HomeView.as_view(), name='homepage'),
    path('calcwave/', CalcFixedFoldView.as_view(), name='calcwave'),
    path('who_we_are/', WhoWeAreView.as_view(), name='who_we_are'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', views.CalcFixedFoldAPIView.as_view()),
]