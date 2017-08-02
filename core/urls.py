from django.conf.urls import url
from . import views as core_views

urlpatterns = [
	url(r'^subjects/$', core_views.subjects, name='subjects'),
]