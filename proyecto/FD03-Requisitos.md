# FD03 · Especificación de requisitos

**MesaQA · Versión 0.1**

| ID | Requisito | Criterio verificable |
|---|---|---|
| RF-01 | Crear una incidencia con un título de 1 a 120 caracteres | POST /tickets válido devuelve 201 y Location. El título se guarda sin espacios exteriores. |
| RF-02 | Consultar una incidencia | GET en Location devuelve el objeto creado. Un identificador inexistente devuelve 404. |
| RF-03 | Listar las incidencias recientes | GET /tickets devuelve un máximo de 100 filas en orden descendente por id. |
| RF-04 | Cerrar una incidencia | PATCH /tickets/{id}/close devuelve closed. Repetir la solicitud conserva el estado. |
| RF-05 | Consultar la salud del servicio | GET /health devuelve 200 si el proceso puede consultar SQLite. |
| RNF-01 | Limitar el tamaño del cuerpo | Una solicitud mayor de 8 KiB devuelve 413. |
| RNF-02 | Separar instrucciones SQL de valores | Las operaciones de escritura y lectura por id usan parámetros SQLite. |
| RNF-03 | Evitar caché de respuestas operativas | Las respuestas incluyen Cache-Control: no-store. |
| RNF-04 | Mantener verificaciones repetibles | La CI genera cobertura y reportes de análisis y conserva los artefactos de la ejecución. |

## Escenarios de aceptación

1. Crear una incidencia y detectar su estado open por la URL devuelta.
2. Enviar un título vacío o un cuerpo mal formado. El servicio rechaza la solicitud y la lista de incidencias continúa vacía.
3. Cerrar una incidencia dos veces. Al reiniciar la aplicación con la misma base, la incidencia sigue cerrada.

## Requisitos de la siguiente fase

El proyecto de Unidad II exige sesiones, historial, caché, logs, telemetría, informes de mutación e interfaz y tres integraciones externas o la alternativa de extensión para VS Code. Se necesita acordar el alcance y la plataforma con el equipo antes de incorporar esos requisitos.
