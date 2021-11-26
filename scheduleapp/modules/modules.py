from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
import csv
import io
from scheduleapp.models import Schedule


def data_get():
  for post in Schedule.objects.all():
    year_month = post.month
    category = post.category
  if category == "all":
    url = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&dy=" + year_month
  else:
    url = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&cd=" + category + "&dy=" + year_month

  response = requests.get(url)
  bs = BeautifulSoup(response.text, "html.parser")
  ul_tag = bs.find_all(class_ = "p-schedule__list-group")
  relist = []
  year = year_month[:4]
  month = year_month[4:]
  for tag in ul_tag:
    j = 0
    sublist = tag.find_all(class_ = "c-schedule__text")
    day = tag.find("span").text
    time = tag.find_all(class_ = "c-schedule__time--list")
    for sub in sublist:
      one_sub = sub.text.replace(" ","").replace("\n","")
      one_day = year + "/" + month + "/" + day
      one_time = time[j].text.replace(" ","").replace("\n","")
      start_time = one_time.split("～")[0]
      try:
        end_time = one_time.split("～")[1]
        relist.append([one_sub,one_day,start_time,one_day,end_time])
      except:
        print("not exist end_time")
        relist.append([one_sub,one_day,start_time])
      j = j + 1
  return relist

def list_get():
  print("get list")
  for post in Schedule.objects.all():
    year_month = post.month
    category = post.category
  if category == "all":
    url = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&dy=" + year_month
  else:
    url = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&cd=" + category + "&dy=" + year_month
  list1 = []
  response = requests.get(url)
  bs = BeautifulSoup(response.text, "html.parser")
  ul_tag = bs.find_all(class_ = "p-schedule__list-group")
  for tag in ul_tag:
    sublist = tag.find_all(class_ = "c-schedule__text")
    hreflist = tag.find_all("a")
    day = tag.find("span").text
    title_list = []
    url_list = []
    for sub in sublist:
      title = sub.text.replace(" ","").replace("\n","")
      title_list.append(title)
    for href in hreflist:
      url2 = "https://www.hinatazaka46.com" + href.get("href")
      url_list.append(url2)
    u=0
    for t in title_list:
      list1.append([day,t, url_list[u]])
      u = u+1
  return list1