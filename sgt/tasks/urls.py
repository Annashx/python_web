from django.contrib import admin
from . import views

urlpartterns = [ 
    path("", views.index, name="index")
]
