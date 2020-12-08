
from django.urls import path
from appis.web import views as Web
app_name = 'web'
urlpatterns = [
    path('', Web.InicioWebView.as_view(), name='index'),
   
]