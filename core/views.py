from django.shortcuts import render

# Create your views here.
from account.models import User

def index(request):
   doctors = User.objects.filter(role='doctor')
   patients = User.objects.filter(role='patient')
   context = {'doctors':doctors,'patients':patients}
   return render(request, "core/index.html" ,context)