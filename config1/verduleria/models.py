from django.db import models

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=254)
	tipo = models.CharField(max_length=254)

	def __str__(self):
		return "Producto {}".format(self.nombre)


class Factura(models.Model):
	cliente = models.CharField(max_length=254)
	facturaNum = models.IntegerField(null=True)

	def total (self):
		total= 0
		price= 0
		c= self.compras.all()
		for a in b :
			price=a.cantidad* a.precio
			total += price
		return (total)

	def __str__(self):
		return "Cliente {}".format(self.cliente)

class Venta(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="producto")
	cantidad = models.IntegerField()
	precio = models.IntegerField(null=True) 
	fechaCompra = models.DateField()