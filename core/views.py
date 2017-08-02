from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core import models as core_models

@login_required
def subjects(request):

	subjects = core_models.Subject.objects.all()
	return render(request, 'core/subjects.html', {'subjects': subjects})
