from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
#Aqui se crea el modelo de la BD (esqueleto)


#########################  ENTIDADES  #####################

#metodo para la creacion de la entidad marca
class Marca(models.Model):
    #creadion de ID autoincrementable y como llave primaria
    idMarca = models.AutoField(primary_key=True,db_column='idMarca')
    #creacion de atributos de entidad
    nombreMarca = models.TextField(max_length=20,db_column='nombreMarca')
    class Meta:
        db_table='Marcas'


class Color(models.Model):
    idColor = models.AutoField(primary_key=True,db_column='idColor')
    nombreColor = models.TextField(max_length=30,db_column='nombreColor')
    class Meta:
        db_table='Color'

class Talla(models.Model):
    idTalla = models.AutoField(primary_key=True,db_column='idTalla')
    nombreTalla = models.FloatField(db_column='nombreTalla')
    class Meta:
        db_table='Talla'

class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True, db_column='idUsuario')
    nombreUsuario = models.CharField(max_length=50, db_column='nombreUsuario')
    apellidoPaterno = models.TextField(max_length=50, db_column='apellidoPaterno')
    apellidoMaterno = models.TextField(max_length=50, db_column='apellidoMaterno')
    password = models.TextField(max_length=128)
    correoElectronico = models.EmailField(unique=True, db_column='correoElectronico')
    numeroTelefonico = models.IntegerField(db_column='numeroTelefonico')

    # Define un related_name único para la relación con grupos
    groups = models.ManyToManyField(Group, verbose_name='Grupos', blank=True, related_name='usuarios')

    # Define un related_name único para la relación con permisos de usuario
    user_permissions = models.ManyToManyField(Permission, verbose_name='Permisos', blank=True, related_name='usuarios')
    
    first_name = None
    last_name = None
    last_login = None
    email =None
    date_joined = None
    is_active = None
    is_staff = None
    is_superuser= None

    # Elimina la referencia a 'username' en el método __str__
    def __str__(self):
        return self.nombreUsuario  # Puedes elegir qué campo usar como representación en cadena (string) del usuario



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,db_column='idProducto')
    nombreProducto = models.TextField(max_length=50,db_column='nombreProducto')
    descripcionProducto = models.TextField(max_length=1000,db_column='descripcionProducto')
    precioProducto =models.FloatField(db_column='precioProducto')
    linkStripe= models.TextField(max_length=100,db_column='linkStripe')
    fk_marca = models.ForeignKey(Marca,on_delete=models.CASCADE,db_column='fk_marca')
    fk_talla = models.ForeignKey(Talla,on_delete=models.CASCADE,db_column='fk_talla')
    fk_color = models.ForeignKey(Color,on_delete=models.CASCADE,db_column='fk_color')
    imagen = models.ImageField(upload_to='imagenes/')

    @property
    def imagen_url(self):
        return self.imagen.url if self.imagen else ''

    class Meta:
        db_table='Producto'


class CarroCompra(models.Model):
    idCarroCompras = models.AutoField(primary_key=True,db_column='idCarroCompras')
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='fk_usuario')
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,db_column='fk_producto')
    class Meta:
        db_table='CarroCompra'


#############Formulario#######
class Formulario(models.Model):
    id_Formulario= models.AutoField(primary_key=True,db_column='id_Formulario')
    pregunta1= models.TextField(db_column='¿Qué busca en una tienda online?')
    pregunta2= models.TextField(db_column='¿Qué forma de pago desea tener en una tienda online?')
    pregunta3= models.TextField(db_column='¿En que dispositivos visita mas una tienda online?')
    pregunta4= models.TextField(db_column='En una tienda online de calzado, ¿Qué tipo de calzado busca con mas frecuencia?')
    pregunta5= models.TextField(db_column='¿Qué métodos de búsqueda prefiere para un tienda de calzado online? ')
    pregunta6= models.TextField(db_column='¿Se basa de las opiniones y calificaciones de los demás para definir si comprar o no un producto online?')
    pregunta7= models.TextField(db_column='¿Cómo prefieres la vista de productos online?')
    pregunta8= models.TextField(db_column='¿Qué le gustaría tener por el uso y compra de productos online?')
    pregunta9= models.TextField(db_column='¿Te gustaría recibir notificaciones o avisos sobre ofertas y promociones? ')
    pregunta10= models.TextField(db_column='¿Qué método de registro prefieres en tiendas online?')
    class Meta:
        db_table='Formulario'