from django.shortcuts import render
from Hermodialisis.models import historiasClinicas, examenesLaboratorio, resultadoLaboratorio
from rest_framework import viewsets, permissions, filters
from Hermodialisis.serializers import HistoriasClinicasSerializer, ExamenesLaboratorioSerializer, ResultadoLaboratorioSerializer

# Create your views here.
class HistoriasClinicasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = historiasClinicas.objects.all()
    serializer_class = HistoriasClinicasSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['hi_nombre']
    
class ExamenesLaboratorioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = examenesLaboratorio.objects.all()
    serializer_class = ExamenesLaboratorioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['ex_descrip']    

class ResultadoLaboratorioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = resultadoLaboratorio.objects.all()
    serializer_class = ResultadoLaboratorioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['lb_autase', '=historiasClinicas__id', '=examenesLaboratorio__ex_codigo']