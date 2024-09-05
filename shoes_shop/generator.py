import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ShoesProject.settings'

import django
django.setup()

from rest_framework import serializers
from django.apps import apps

def generate_serializers():
    serializers_dict = {}
    for modeln in apps.get_models():
        class Meta:
            model = modeln
            fields = [field.name for field in modeln._meta.fields if field.name != 'id']

        serializer_class = type(f'{modeln.__name__}Serializer',
                                (serializers.ModelSerializer,),
                                {'Meta': Meta})
        serializers_dict[modeln.__name__] = serializer_class
    return serializers_dict

# вызовите функцию и выведите результат
serializers = generate_serializers()
for model_name, serializer in serializers.items():
    print(f"class {serializer.__name__}(serializers.ModelSerializer):")
    print("    class Meta:")
    print(f"        model = {model_name}")
    print(f"        fields = {serializer.Meta.fields}")
