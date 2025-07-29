app_name = 'contacts'

from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact')
]
