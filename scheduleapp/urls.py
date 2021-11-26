from django.urls import path
from .views import Create, CreateIndex, listfunc,csvdownload

urlpatterns = [
  path('home/', Create.as_view(), name = 'home'),
  path('list/', listfunc, name = 'list'),
  path('csv/', csvdownload, name='csv'),
  path('', CreateIndex.as_view(), name='index'),
]