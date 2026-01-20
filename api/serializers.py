from rest_framework import serializers
from pokedex.models import Pokemon, Trainer
from django.core.files.base import ContentFile
import base64
class PokemonSerializer(serializers.ModelSerializer):
    
    picture=serializers.CharField(required=True, allow_blank=True)
    
    class Meta:
        model = Pokemon
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method == 'PUT':
            self.fields['picture'].required = False
        
    def validate_picture(self, value):
        if value:
            try:
                # Decodificar base64
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Invalid base64 image")
        return None
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'