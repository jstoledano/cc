from django.db import models


class Distrito(models.Model):
    cabecera = models.CharField(max_length=100)
    distrito = models.SmallIntegerField()

    def __str__(self):
        return f'{self.distrito:02d} - {self.cabecera}'
    
    class Meta:
        verbose_name_plural = "Distritos"
        ordering = ['distrito']


class DistritoLocal(models.Model):
    distrito_local = models.SmallIntegerField()
    cabecera = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.distrito_local:02d} - {self.cabecera}'
    
    class Meta:
        verbose_name_plural = "Distritos Locales"
        ordering = ['distrito_local']



class Municipio(models.Model):
    municipio = models.SmallIntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.municipio:03d} - {self.nombre}'
    
    class Meta: 
        verbose_name_plural = "Municipios"
        ordering = ['municipio']


class Seccion(models.Model):
    seccion = models.SmallIntegerField()
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    distrito_local = models.ForeignKey(DistritoLocal, on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'29-{self.distrito.distrito:02}-{self.distrito_local.distrito_local:02}-{self.municipio.municipio:03}-{self.seccion:04}'
    
    class Meta:
        verbose_name_plural = "Secciones"
        ordering = ['distrito', 'distrito_local', 'municipio', 'seccion']