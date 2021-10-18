from django.contrib.auth.models import User, Group
from Hermodialisis.models import historiasClinicas, examenesLaboratorio, resultadoLaboratorio
from rest_framework import serializers

class HistoriasClinicasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = historiasClinicas
        fields = '__all__'

class ExamenesLaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = examenesLaboratorio
        fields = '__all__'

class ResultadoLaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    datosHistoriasCLinicas = HistoriasClinicasSerializer(source="historiasClinicas", read_only=True)
    datosExamenesLaboratorio = ExamenesLaboratorioSerializer(source="examenesLaboratorio", read_only=True)
    class Meta:
        model = resultadoLaboratorio
        fields = '__all__'