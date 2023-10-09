from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self,data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua numeros neste campo'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve conter 9 digitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'Celular inválido, insira da seguinte forma: XX 9XXXX-XXXX'})
        return data 

    
    def validate_celular(self,celular):
        if len(celular) < 11:
            raise serializers.ValidationError('O celular deve conter pelo menos 11 digitos')
        return celular