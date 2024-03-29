"""Dialisis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from rest_framework import routers, permissions
from Examenes_Escaneados import views as viewsDP
from Hermodialisis import views as viewsHermodialisis

from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
schema_view = get_schema_view(   
    openapi.Info(      
        title="Dialisis Peritoneal",     
        default_version='v1',      
        description="Descripcion de APIS",      
        terms_of_service="https://www.google.com/policies/terms/",      
        contact=openapi.Contact(email="contact@snippets.local"),      
        license=openapi.License(name="BSD License"),   
    ),   
    public=True,   
    permission_classes=(permissions.AllowAny,),
    )

router = routers.DefaultRouter()
router.register(r'paciente', viewsDP.PacienteViewSet)
router.register(r'examen', viewsDP.ExamenViewSet)

router.register(r'Historias Clinicas', viewsHermodialisis.HistoriasClinicasViewSet)
router.register(r'Examenes Laboratorio', viewsHermodialisis.ExamenesLaboratorioViewSet)
router.register(r'Resultados Laboratorio', viewsHermodialisis.ResultadoLaboratorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)