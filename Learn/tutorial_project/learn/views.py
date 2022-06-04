from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
  # return HttpResponse("<h1>Hello world</h1>")
  context = {
      'name': 'Dharmendra',
      'data': {
          'm_name': 'Kumar',
          'l_name': 'Sharma',
      },
      'backend_lang': [
          'php', 'node', 'python', 'jquery', 'html'
      ],
      'percentage': {
          'TENTH': 71,
          'TWELVETH': 69,
          'BTECH': 78,
      }
  }
  return render(request, 'learn/home.html', context)
