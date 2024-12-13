from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('first.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember
  }
  return HttpResponse(template.render(context, request))

def home(request):
  template = loader.get_template("main.html")
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template("template.html")
  context = {
    'prices': [3,4,4,'we'],
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'vegetables': ['Asparagus', 'Broccoli', 'Carrot'],
    'mycar': {
      'brand': 'Ford',
      'model': 'Mustang',
      'year': '1964',
      }
  }
  return HttpResponse(template.render(context, request))