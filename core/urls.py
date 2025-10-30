from django.views.generic import TemplateView
from django.urls import path
from . import views


urlpatterns = [    
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    # path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    # path('contact/', views.contact_view, name='contact'),   

]