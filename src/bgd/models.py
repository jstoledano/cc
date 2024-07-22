"""Modelos usados en la definición de la base cartográfica digital."""
from django.db import models


class Entidad(models.Model):
    """Modelo que representa una entidad federativa."""
    entidad = models.SmallIntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.entidad:02d} - {self.nombre}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """Sobreescribe el método save para asegurar que el nombre de la entidad
        esté en mayúsculas."""
        self.nombre = self.nombre.upper()
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Entidades"
        ordering = ['entidad']


class Distrito(models.Model):
    """Modelo que representa un distrito electoral federal."""
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    cabecera = models.CharField(max_length=100)
    distrito = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        """Sobreescribe el método save para asegurar que la cabecera del distrito
        esté en mayúsculas."""
        self.cabecera = self.cabecera.upper()
        super(Distrito, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.entidad.entidad:02d} - {self.distrito:02d} - {self.cabecera}'

    class Meta:
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Distritos"
        ordering = ['distrito']


class DistritoLocal(models.Model):
    """Modelo que representa un distrito electoral local."""
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    distrito_local = models.SmallIntegerField()
    cabecera = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        """Sobreescribe el método save para asegurar que la cabecera del distrito
        esté en mayúsculas."""
        self.cabecera = self.cabecera.upper()
        super(DistritoLocal, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.entidad.entidad:02d} - {self.distrito_local:02d} - {self.cabecera}'

    class Meta:
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Distritos Locales"
        ordering = ['distrito_local']


class Municipio(models.Model):
    """Modelo que representa un municipio."""
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    municipio = models.SmallIntegerField()
    nombre = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        """Sobreescribe el método save para asegurar que el nombre del municipio
        esté en mayúsculas."""
        self.nombre = self.nombre.upper()
        super(Municipio, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.entidad.entidad:02d} - {self.municipio:03d} - {self.nombre}'

    class Meta: 
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Municipios"
        ordering = ['municipio']


class Localidad(models.Model):
    """Modelo que representa una localidad."""
    localidad = models.SmallIntegerField()
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Sobreescribe el método save para asegurar que el nombre de la localidad
        esté en mayúsculas."""
        self.nombre = self.nombre.upper()
        super(Localidad, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.municipio.municipio:03d}-{self.localidad:03d} - {self.nombre}'

    class Meta:
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Localidades"
        ordering = ['municipio', 'localidad']


class Seccion(models.Model):
    """Modelo que representa una sección electoral."""
    seccion = models.SmallIntegerField()
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    distrito_local = models.ForeignKey(DistritoLocal, on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'29-{self.distrito.distrito:02}-\
        {self.distrito_local.distrito_local:02}-\
        {self.municipio.municipio:03}-{self.seccion:04}'

    class Meta:
        """Clase que define metadatos del modelo."""
        verbose_name_plural = "Secciones"
        ordering = ['distrito', 'distrito_local', 'municipio', 'seccion']
