from django.shortcuts import render, get_object_or_404
from .models import Bewerbung
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def bewerbung_list(request):
    bewerbungen = Bewerbung.objects.order_by("date_applied")
    return render(request, 'bewerbung/bewerbung_list.html', {'bewerbungen': bewerbungen})

def bewerbung_detail(request, pk):
    bewerbung = get_object_or_404(Bewerbung, pk=pk)
    return render(request, 'bewerbung/bewerbung_detail.html', {'bewerbung': bewerbung})

class BewerbungCreateView(LoginRequiredMixin,CreateView):
    model = Bewerbung
    template_name = 'bewerbung/bewerbung_form.html'
    fields = ['name', 'company', 'position', 'date_applied', 'status']
    success_url = reverse_lazy('bewerbung_list')


class BewerbungUpdateView(LoginRequiredMixin, UpdateView):
    model = Bewerbung
    template_name = 'bewerbung/bewerbung_form.html'
    fields = ['name', 'company', 'position', 'date_applied', 'status']
    success_url = reverse_lazy('bewerbung_list')


class BewerbungDeleteView(LoginRequiredMixin, DeleteView):
    model = Bewerbung
    template_name = 'bewerbung/bewerbung_confirm_delete.html'
    success_url = reverse_lazy('bewerbung_list')
    
    
@login_required
def bewerbung_list(request):
    bewerbungen = Bewerbung.objects.order_by("date_applied")
    return render(request, 'bewerbung/bewerbung_list.html', {'bewerbungen': bewerbungen})