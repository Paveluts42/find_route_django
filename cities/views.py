from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView'
)


#
# def home(request, pk=None):
#     if request.method == 'POST':
#
#     form = CityForm()
#     qs = City.objects.all()
#     lst = Paginator(qs, 2)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj, 'form': form}
#     return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy("cities:home")
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy("cities:home")
    success_message = "Город успешно отредактирован"


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy("cities:home")

    def get(self, req, *args, **kwargs):
        messages.success(req, 'Город успешно удален')
        return self.post(req, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
