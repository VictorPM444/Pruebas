# tests/test_tu_app.py
import pytest
from api.models import Categoria



@pytest.mark.django_db
def test_creacion_categoria():
    # Crear una instancia de Categoria para la prueba
    categoria_prueba = Categoria.objects.create(
        nombreCategoria='Ropa',
        descripcion='Ropa de moda para todas las edades.'
    )

    # Recuperar la categoría de la base de datos
    categoria_recuperada = Categoria.objects.get(nombreCategoria='Ropa')

    # Verificar que la categoría recuperada sea la misma que la creada
    assert categoria_prueba.nombreCategoria == categoria_recuperada.nombreCategoria
    assert categoria_prueba.descripcion == categoria_recuperada.descripcion
