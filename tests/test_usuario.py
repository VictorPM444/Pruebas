# tests/test_tu_app.py
import pytest
from api.models import Usuario

@pytest.mark.django_db
def test_creacion_usuario():
    # Crear una instancia de Usuario para la prueba
    usuario_prueba = Usuario.objects.create(
        nombreUsuario='usuario_prueba',
        apellidoPaterno='Perez',
        apellidoMaterno='Lopez',
        password='clave_segura',
        correoElectronico='usuario_prueba@example.com',
        numeroTelefonico=123456789
    )

    # Recuperar el usuario de la base de datos
    usuario_recuperado = Usuario.objects.get(nombreUsuario='usuario_prueba')

    # Verificar que el usuario recuperado sea el mismo que el creado
    assert usuario_prueba.nombreUsuario == usuario_recuperado.nombreUsuario
    assert usuario_prueba.correoElectronico == usuario_recuperado.correoElectronico