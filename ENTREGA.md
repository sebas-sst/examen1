# Entrega individual — Parte práctica

- Nombre y código: Sebastian Soto  95429
- URL del repositorio privado:https://github.com/sebas-sst/examen1
- Rama entregada:
- Commit final: se presenta en el formulario/mensaje de entrega después del último commit.

## Resultado inicial

- Comando ejecutado:python -m pytest -v
- Resumen real de pytest antes de cambiar el código:

## Cambios y requisitos

En dos o tres frases, explique qué cambió en modificar_reserva y por qué.
En modificar_reservas agregue la funcion hay_conflicto para cumplir el Rf-04
## Trazabilidad de sus pruebas

| Nombre de la prueba | Requisito | Resultado esperado |
|---|---|---|
| `test_cambio_valido` | RF-05 | Retorna `"OK"`, |
| `test_conflicto` | RF-04 | Retorna `"CONFLICTO"`  |
| `test_conservar` | RF-04 | Retorna `"CONFLICTO"` |
| `test_limite` | RF-04 / RF-05 | Retorna `"OK"`  |

## Resultado final y límites

- Comando ejecutado:python -m pytest -v
- Resumen real de pytest (passed/failed y otros resultados si aparecen):
- ests/test_base.py::test_ejemplo_intervalos_adyacentes PASSED                                                                                                                [ 14%]
tests/test_base.py::test_intervalos_con_superposicion PASSED                                                                                                                 [ 28%]
tests/test_base.py::test_modificacion_sin_otras_reservas PASSED                                                                                                              [ 42%]
tests/test_estudiante.py::test_cambio_valido PASSED                                                                                                                          [ 57%]
tests/test_estudiante.py::test_conflicto PASSED                                                                                                                              [ 71%]
tests/test_estudiante.py::test_conservarcion_ante_conflicto PASSED                                                                                                           [ 85%]
tests/test_estudiante.py::test_limite_adyacente PASSED                                                                                                                       [100%]

================================================================================ 7 passed in 0.03s ============================
- ¿Qué comportamiento sigue sin comprobar? Escriba una limitación concreta:
- 

No presente una prueba fallida como aprobada. Conserve y explique cualquier pendiente.
