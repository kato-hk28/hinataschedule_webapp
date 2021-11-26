from django.shortcuts import render
from .models import Schedule
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from scheduleapp.modules import modules
from django.http import HttpResponse
import csv
import io


class Create(CreateView):
  template_name = 'home.html'
  model = Schedule
  fields = ('month','category',)
  success_url = reverse_lazy('list')

class CreateIndex(CreateView):
  template_name = 'index.html'
  model = Schedule
  fields = ('month','category',)
  success_url = reverse_lazy('list')

def listfunc(request):
  print("listfunc")
  context = {'list': modules.list_get(),}
  return render(request, 'list.html', context)

def csvdownload(request):
  response = HttpResponse(content_type = 'text/csv; charset=cp932' )
  filename = urllib.parse.quote(('データ.csv'))
  response['Content-Disposition'] = 'attachment; filename = "{}"'.format(filename)
  writer = csv.writer(response)
  writer.writerow(['Subject','Start Date', 'Start Time', 'End Date', 'End Time'])
  get_data_re = modules.data_get()
  writer.writerows(get_data_re)
  
  return response