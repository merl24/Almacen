from django.urls import path
from .views import *

urlpatterns=[
    #INTRACCIONES FRONTEND/ VISTAS
    path('',home),                                          #Frontend   //  INDEX
    path('registro/',gestion_prod),                         #Frontend   //  VISTA: REGISTRO DE PRODUCTOS
    path('productos/',lista_productos),                     #Frontend   //  VISTA: LISTA DE PRODUCTOS
    path('registrar_prod/',reg_productos),                  #Backend    //  INTERACCION DE REGISTRO
    path('editar_producto/<codigo>',editar_productos),          #Frontend   //  VISTA: EDICION PRODUCTOS
    path('editar/',editar_prod),                        #Backend    //  INTERACCION DE EDITOR
    
    path('eliminar_producto/<id>',eliminar_productos),
]