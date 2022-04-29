from dataclasses import field, fields
from rest_framework import serializers

from school_app.models import Curso


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','titulo','tempo','valor','descricao','conteudo')
        
        
    