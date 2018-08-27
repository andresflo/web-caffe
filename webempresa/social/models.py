from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name = "Nombre clave", max_length=15)#Campo slug obliga a tener letras y numero sin caracteres especiales
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="enlace"#Nombre que se la asignamos
        verbose_name_plural="enlaces"#Nombre en plural
        ordering = ["name"]#Ordenamos por fecha de creación del mas nuevo al mas viejo por el "-"


    def __str__(self):
        return self.name