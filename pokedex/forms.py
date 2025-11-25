from django import forms
from .models import Pokemon
from .models import Trainer
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
        
        
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        labels ={
            "name":"Nombre del Entrenador",
            "last_name":"Apellido del Entrenador",
            "years":"Años del Entrenador",
            "level":"Nivel del Entrenador",
            "datebirth":"Fecha de Nacimiento del Entrenador"
            
        }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "years": forms.NumberInput(attrs={"class":"form-control"}),
            "level": forms.NumberInput(attrs={"class":"form-control"}),
            "datebirth": forms.DateInput(attrs={"class":"form-control", "type":"date)" })
        }