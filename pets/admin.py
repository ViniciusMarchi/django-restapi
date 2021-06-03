from django.contrib import admin
from .models import Animal, Cachorro, Gato, Passaro
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


# Realizando herança entre as tabelas

@admin.register(Animal)
class AdminAnimal(PolymorphicParentModelAdmin):
    base_model = Animal
    child_models = (Cachorro, Gato, Passaro)
    list_filter = (PolymorphicChildModelFilter,)

@admin.register(Cachorro)
class AdminCachorro(PolymorphicChildModelAdmin):
    base_model = Cachorro

@admin.register(Gato)
class AdminGato(PolymorphicChildModelAdmin):
    base_model = Gato

@admin.register(Passaro)
class AdminPassaro(PolymorphicChildModelAdmin):
    base_model = Passaro