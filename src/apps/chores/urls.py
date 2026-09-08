from django.urls import path

from . import views


urlpatterns = [
    path("zonas/", views.zone_list, name="zone_list"),
    path("zonas/nueva/", views.zone_create, name="zone_create"),
    path("zonas/<int:pk>/editar/", views.zone_edit, name="zone_edit"),
    path("zonas/<int:pk>/desactivar/", views.zone_deactivate, name="zone_deactivate"),
    path("tareas/", views.chore_list, name="chore_list"),
    path("tareas/nueva/", views.chore_create, name="chore_create"),
    path("tareas/<int:pk>/editar/", views.chore_edit, name="chore_edit"),
    path("tareas/<int:pk>/retirar/", views.chore_retire, name="chore_retire"),
]
