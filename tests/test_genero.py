# tests/test_tu_app.py
import pytest
from api.models import Genero


@pytest.mark.django_db
def test_creacion_genero():
    # Crear una instancia de Genero para la prueba
    genero_prueba = Genero.objects.create(
        nombreGenero='Masculino'
    )

    # Recuperar el género de la base de datos
    genero_recuperado = Genero.objects.get(nombreGenero='Masculino')

    # Verificar que el género recuperado sea el mismo que el creado
    assert genero_prueba.nombreGenero == genero_recuperado.nombreGenero
