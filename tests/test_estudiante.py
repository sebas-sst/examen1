"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva

from copy import deepcopy
from reservas import modificar_reserva


def test_cambio_valido():
    datos = [
        {"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 660, "fin": 720, "estado": "confirmada"},
    ]
    assert modificar_reserva(datos, "R1", 720, 780) == "OK"
    assert datos[0]["inicio"] == 720
    assert datos[0]["fin"] == 780
    assert datos[1]["inicio"] == 660


def test_conflicto():
    datos = [
        {"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"},
    ]
    assert modificar_reserva(datos, "R1", 630, 690) == "CONFLICTO"


def test_conservarcion_ante_conflicto():
    datos = [
        {"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"},
    ]
    antes = deepcopy(datos)
    modificar_reserva(datos, "R1", 630, 690)
    assert datos == antes


def test_limite_adyacente():
    datos = [
        {"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"},
    ]
    assert modificar_reserva(datos, "R1", 480, 600) == "OK"
    assert datos[0]["inicio"] == 480
    assert datos[0]["fin"] == 600

# Ejemplo de estructura, sin solución del caso:
# def test_nombre_del_comportamiento():
#     datos = [...]
#     antes = deepcopy(datos)
#     resultado = modificar_reserva(datos, ...)
#     assert resultado == "..."
#     assert datos == antes  # Cuando la operación debe conservar TODO.
