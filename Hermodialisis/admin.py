from django.contrib import admin
from Hermodialisis.models import historiasClinicas, examenesLaboratorio, resultadoLaboratorio

# Register your models here.

class historiasClinicasAdmin(admin.ModelAdmin):
    list_display = ('hi_autase', 'hi_nombre', 'hi_fec_nac', 'hi_sexo', 'hi_tdocum', 'hi_ndocum', 'hi_estciv', 'hi_indact', 'hi_factrh', 'fecha_reg')

class examenesLaboratorioAdmin(admin.ModelAdmin):
    list_display = ('ex_codigo', 'ex_descrip', 'ex_abrev', 'ex_unidad', 'ex_valinih', 'ex_valfinh')

class resultadoLaboratorioAdmin(admin.ModelAdmin):
    list_display = ('lb_autase', 'lb_fecha', 'lb_codexa', 'lb_resul', 'lb_fecproc', 'lb_horproc', 'historiasClinicas', 'examenesLaboratorio')
    search_fields = ('examenesLaboratorio__ex_codigo','examenesLaboratorio__ex_descrip', 'historiasClinicas__hi_nombre')

admin.site.register(historiasClinicas, historiasClinicasAdmin)
admin.site.register(examenesLaboratorio, examenesLaboratorioAdmin)
admin.site.register(resultadoLaboratorio, resultadoLaboratorioAdmin)