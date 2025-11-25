
from rest_framework import viewsets
from .serializers import PokemonSerializer
from pokedex.models import Pokemon

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    required_scopes = ['write']