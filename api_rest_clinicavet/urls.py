from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pets.urls')),
    path('', include('clientes.urls')),
    path('', include('veterinarios.urls')),
    path('', include('consultas.urls'))
]
