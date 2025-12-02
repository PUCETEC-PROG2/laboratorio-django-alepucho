from rest_framework import viewsets
from .serializers import PokemonSerializer
from pokedex.models import Pokemon
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]