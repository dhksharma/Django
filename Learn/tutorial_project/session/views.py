from django.shortcuts import render

import session

# Create your views here.


def set_session(request):

  request.session["name"] = "Dharmendra"
  # 10 is the time in second after that this session will expire from browser 
  #chrome://settings/cookies/detail?site=127.0.0.1
  request.session.set_expiry(10)  
  return render(request, 'session/set.html')


def get_session(request):
  name=request.session.get("name","session not set")
  request.session.setdefault('age','31')
  return render(request, 'session/get.html',{"name":name})


def del_session(request):
  # This will delete all session frm DB session table
  # request.session.flush()
  # request.session.clear_expired()
  if 'name' in request.session:
    del request.session["name"]
  return render(request, 'session/del.html')
