from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
        labels ={
            "name":"Nombre del Pokémon",
            "type":"Tipo de Pokémon",
            "weight":"Peso del Pokémon (kg)",
            "height":"Altura del Pokémon (m)",
            "trainer":"Entrenador del Pokémon",
            "picture":"Imagen del Pokémon"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "type": forms.TextInput(attrs={"class":"form-control"}),
            "weight": forms.NumberInput(attrs={"class":"form-control", "step":"0.1"}),
            "height": forms.NumberInput(attrs={"class":"form-control", "step":"0.01"}),
            "trainer": forms.Select(attrs={"class":"form-control"}),
            "picture": forms.ClearableFileInput(attrs={"class":"form-control"})
        }