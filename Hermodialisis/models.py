from django.db import models

# Create your models here.
class historiasClinicas(models.Model):
    hi_autase = models.CharField(max_length=15)
    hi_nombre = models.CharField(max_length=40)
    hi_fec_nac = models.DateField(null=True, blank=True)
    hi_sexo = models.CharField(max_length=1)
    hi_tdocum = models.CharField(max_length=1)
    hi_ndocum = models.CharField(max_length=10)
    hi_estciv = models.CharField(max_length=1)
    hi_indact = models.CharField(max_length=1)
    hi_factrh = models.CharField(null=True, max_length=1) 
    fecha_reg = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.hi_nombre

class examenesLaboratorio(models.Model):
    ex_codigo = models.CharField(max_length=7)
    ex_descrip = models.CharField(max_length=40)
    ex_abrev = models.CharField(max_length=10)
    ex_unidad = models.CharField(max_length=10)
    ex_valinih = models.IntegerField()
    ex_valfinh = models.IntegerField()

    def __str__(self):
        return self.ex_descrip

class resultadoLaboratorio(models.Model):
    lb_autase = models.CharField(max_length=15)
    lb_fecha = models.DateField(null=True, blank=True)
    lb_codexa = models.CharField(max_length=7)
    lb_resul = models.CharField(max_length=10)
    lb_orden = models.CharField(max_length=8, null=True)
    lb_fecproc = models.DateField(null=True, blank=True)
    lb_horproc = models.CharField(max_length=5)
    historiasClinicas = models.ForeignKey(historiasClinicas, null=True, on_delete=models.CASCADE)
    examenesLaboratorio = models.ForeignKey(examenesLaboratorio,null=True,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lb_resul