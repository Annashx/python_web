from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("biel", views.biel, name="biel"),
	path("lerigou", views.lerigou, name="lerigou"),
	path("<str:name>", views.greet, name="greet")
	]


