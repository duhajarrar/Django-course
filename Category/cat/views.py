from django.shortcuts import render
from .models import Cat
# Create your views here.
def index(request):
   cat = Cat.objects.all()
   context = {'cat':cat}
   #return HttpResponse("Hello Django!!!")
   return render(request,'allcat.html',context)

def getCat(request,cat_id):
   cat = Cat.objects.get(pk=cat_id)
   print(cat.catName)
   print(cat.catDesc)
   context = {'cat':cat}
   return render(request,'cat.html',context)
