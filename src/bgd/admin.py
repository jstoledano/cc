from django.contrib import admin
from .models import Entidad, Distrito, DistritoLocal, Municipio, Seccion


admin.site.register(Entidad)
admin.site.register(Distrito)
admin.site.register(DistritoLocal)
admin.site.register(Municipio)
admin.site.register(Seccion)
