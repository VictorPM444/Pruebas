from django.test import TestCase
import pytest
from api.models import Marca, Categoria, Material, Temporada, Genero, Talla, Color, Usuario

@pytest.mark.django_db
def test_creacion_marca():
    marca = Marca.objects.create(nombreMarca='Nike', descripcion='Zapatos deportivos')
    assert marca.nombreMarca == 'Nike'
