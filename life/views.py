from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.http import Http404

from .models import DiaryModel
from .forms import DiaryForm

class DiaryUpdateView(UpdateView):
	model = DiaryModel
	fields = ('your_day', 'adventure')
	template_name = 'home.html'

class DiaryDeleteView(DeleteView):
	model = DiaryModel
	success_url = reverse_lazy('list')
	template_name = 'life/delete.html'
	context_object_name = 'object'

def home(request):
	form = DiaryForm()
	if request.method == 'POST':
		form = DiaryForm(request.POST)
		if form.is_valid():
			var = form.save(commit=False)
			var.user = request.user
			var.save()
			return redirect('list')
		else:
			form = DiaryForm()
	return render(request, 'home.html', {'form':form})

class DiaryDetailView(DetailView):
	model = DiaryModel
	template_name = 'life/days.html'

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		try:
			instance = get_object_or_404(DiaryModel, pk=pk)
		except:
			raise Http404("Sorry..this day doesn't exist")
		return instance

	def get_context_data(self, *args, **kwargs):
		context = super(DiaryDetailView, self).get_context_data(*args, **kwargs)
		return context

class DiaryListView(ListView):
	template_name = "life/list.html"
	# queryset = DiaryModel.objects.filter(user=request.user)
	context_object_name = 'object'

	def get_queryset(self, *args, **kwargs):
		request = self.request
		queryset = DiaryModel.objects.filter(user=request.user)
		print(queryset)
		return queryset