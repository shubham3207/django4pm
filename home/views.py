from django.shortcuts import render
from django.views import View
from .models import *
class Base(View):
    
    views={}
# Create your views here.
class HomeView(Base):
    def get(self,request):
        self.views['categories']=Category.objects.all()
        self.views['brands']=Brand.objects.all()
        return render(request,'index.html',self.views)

    

