# tests/test_tu_app.py
import pytest
from api.models import Marca

@pytest.mark.django_db
def test_creacion_marca():
    # Crear una instancia de Marca para la prueba
    marca_prueba = Marca.objects.create(
        nombreMarca='Nike',
        descripcion='Zapatos deportivos de prueba.'
    )

    # Recuperar la marca de la base de datos
    marca_recuperada = Marca.objects.get(nombreMarca='Nike')

    # Verificar que la marca recuperada sea la misma que la creada
    assert marca_prueba.nombreMarca == marca_recuperada.nombreMarca
    assert marca_prueba.descripcion == marca_recuperada.descripcion

