from django.shortcuts import render
from django.views import View

# Create your views here.

class Game_View(View):
    def get(self,request,*args,**kwargs):
        return render(request,'game/index.html')

game = Game_View.as_view()
