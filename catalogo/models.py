from django.db import models
from core.models import User, Person

# Create your models here.


class Mesa(models.Model):

    piso = models.CharField(max_length=100)
    maxPersonas = models.CharField(max_length=60)
    numMesa = models.CharField(max_length=60)
    libre = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"

    def __str__(self):
        return '%s (%s) (%s) (%s)' % (self.piso, self.maxPersonas, self.numMesa, self.libre,)


class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    tipoProducto = models.CharField(max_length=15)
    uniMedida = models.CharField(max_length=15)
    cantidad = models.CharField(max_length=60)
    precio = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s) (%s) (%s) (%s)' % (self.nombre, self.tipoProducto, self.cantidad, self.cantidad, self.precio,)


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apePaterno = models.CharField(max_length=60)
    apeMaterno = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s (%s) (%s)' % (self.nombre, self.apePaterno, self.apeMaterno)


class Menu(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return '%s (%s),' % (self.nombre, self.precio,)


class Pedido(models.Model):

    menu = models.ForeignKey(Menu)
    pagado = models.CharField(max_length=10)
    confirmado = models.CharField(max_length=10)
    servido = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente)
    mesa = models.ForeignKey(Mesa)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return '%s (%s) (%s) (%s)' % (self.fecha, self.pagado, self.confirmado,  self.servido,)


class Reserva(models.Model):

    cliente = models.ForeignKey(Cliente)
    mesa = models.ForeignKey(Mesa)
    finalizada = models.CharField(max_length=2)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return '%s' % (self.fecha)


class detalleMenu(models.Model):

    Menu = models.ForeignKey(Menu)
    cantidad = models.CharField(max_length=15)
    precioUni = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "detalleMenu"
        verbose_name_plural = "detalleMenus"

    def __str__(self):
        return '%s (%s)' % (self.cantidad, self.precioUni,)


class Venta(models.Model):

    Menu = models.ForeignKey(Menu)
    cantidad = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    precioTotal = models.FloatField(default=0.0)
    servida = models.CharField(max_length=15)
    confirmada = models.CharField(max_length=15)
    Producto = models.ForeignKey(Producto)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s (%s) (%s) (%s) (%s)' % (self.cantidad, self.nombre, self.precioTotal, self.servida, self.confirmada,)



