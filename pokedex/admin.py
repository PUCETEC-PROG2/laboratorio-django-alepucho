from django.contrib import admin
from .models import Pokemon
from .models import Trainer
@admin.register(Pokemon)
class PokemonsAdmin(admin.ModelAdmin):
    pass
@admin.register(Trainer)
class TrainersAdmin(admin.ModelAdmin):
    pass