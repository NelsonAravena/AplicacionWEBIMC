from django.shortcuts import render


# Create your views here.
def comenzar(request):
    return render(request, "showstatic/comenzar.html")
    
def add (request):
    peso  = int(request.POST["peso"])
    altura = float(request.POST["altura"])
    c = (round(peso / altura **2,1)) 
    return render(request, 'showstatic/resultados.html',{"result":c})