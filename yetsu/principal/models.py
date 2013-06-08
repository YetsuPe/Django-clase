from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	titulo=models.CharField(max_length=30)
	portada=models.ImageField(upload_to='imgsPosts',verbose_name="portada")
	contenido=models.TextField(help_text='Ingrese su contenido')
	fecha=models.DateTimeField(auto_now=True)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	post=models.ForeignKey(Post)
	texto=models.TextField(verbose_name='Comentario')
	def __unicode__(self):
		return self.texto	