from django.shortcuts import render
from .models import *
# Create your views here.

def inicio(request):
	
	context = {}
	context["todas_las_ventas"] = Venta.objects.filter(fechaVenta=None)

	return render(request, "index.html", context)

def clienteUnico(request, cliente_id):
	
	context = {}
	context["todos_los_clientes"] = Venta.objects.filter(clienteId=cliente_id)

	return render(request, "total.html", context)