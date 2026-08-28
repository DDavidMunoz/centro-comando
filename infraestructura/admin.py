from django.contrib import admin
from .models import NodoServidor, RegistroAuditoria

@admin.action(description="Activar Produccion masiva")
def marcar_como_produccion(modeladmin, request,queryset):
    cantidad = queryset.update(en_produccion=True)
    modeladmin.message_user(
        request,
        f"{cantidad} nodos fueron marcados como producción."
    )

@admin.action(description="Poner en Mantenimiento")
def marcar_como_mantenimiento(modeladmin, request, queryset):
    cantidad = queryset.update(en_produccion=False)

    modeladmin.message_user(
        request,
        f"{cantidad} nodos fueron puestos en mantenimiento."
    )


@admin.register(NodoServidor) 
class NodoServidorAdmin(admin.ModelAdmin): 
    # Columnas que se mostrarán en la tabla principal 
    list_display = ('nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', 'en_produccion') 

    # Filtros laterales para hacer búsquedas rápidas 
    list_filter = ('motor_contenedores', 'proxy_inverso', 'en_produccion')

    # Barra de búsqueda superior 
    search_fields = ('nombre_host', 'direccion_ip') 

    # Orden por defecto 
    ordering = ('-fecha_despliegue',)

    # Acciones Masivas
    actions = [
        marcar_como_produccion,
        marcar_como_mantenimiento,
    ]

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('servidor','detalles','fecha_evento')

    list_filter = ('fecha_evento',)

    search_fields = ('servidor_nombre_host', 'detalles')

    ordering = ('-fecha_evento',)


