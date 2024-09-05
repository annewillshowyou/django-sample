from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import BbForm

from .models import Bb, Rubric

def index(request):
	bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	context = {'bbs':bbs, "rubrics":rubrics}
	return render(request, 'bboard/index.html', context)

def rubric_bbs(request, rubric_id):
	bbs = Bb.objects.filter(rubric=rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk = rubric_id)
	context = {"bbs":bbs, "rubrics":rubrics, "current_rubric":current_rubric}
	return render(request, 'bboard/rubric_bbs.html', context)

class BbCreateView(CreateView):
		template_name = 'bboard/bb_create.html'
		form_class = BbForm
		success_url = '/bboard/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

	"""Генерирует словарь рубрик, который будет использоваться на каждой странице"""