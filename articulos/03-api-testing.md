# Probé el contrato de una API de incidencias con unittest

Una prueba de API debe comprobar la respuesta y el efecto sobre el estado. En MesaQA, al crear una incidencia se espera un HTTP 201, un estado inicial open y una cabecera Location que permite recuperar el recurso. Además, una solicitud inválida debe dejar la base de datos intacta.

Cada caso crea una base SQLite temporal. El cliente de pruebas de Flask invoca la aplicación sin depender de Internet. Las pruebas comprueban lectura, orden de las incidencias, tipos de contenido, tamaños máximos, errores 404 y el cierre repetido de una incidencia. Una segunda instancia con la misma base comprueba que el cierre quede guardado. Otras dos pruebas levantan Waitress en localhost y realizan peticiones HTTP reales a un puerto efímero. Verifican el ciclo de vida del ticket y comprueban que rechazar un título vacío deja intacta la lista.

```bash
python -m pip install -r requirements.txt
python -m pip install coverage==7.17.3
coverage run --concurrency=thread --source=qa -m unittest discover -s tests -v
coverage report
```

La ejecución local aprobó once pruebas y cubrió 66 de 66 líneas ejecutables. La cobertura mide ejecución de líneas. El comportamiento esperado se comprueba con las aserciones sobre el código HTTP, el cuerpo JSON, las cabeceras y la persistencia.

La automatización ejecuta las mismas pruebas y genera un informe XML antes del despliegue. El blueprint usa el plan gratuito de Render y configura despliegue automático cuando pasan las verificaciones de la rama. La conexión con Render queda pendiente. Cuando exista una URL pública, GET /health permitirá confirmar que el servicio de nube responde.

- [Repositorio público](https://github.com/RichiPodesta1113/mesaqa-si784)
- [GitHub Actions](https://github.com/RichiPodesta1113/mesaqa-si784/actions)
- [Pruebas de aplicaciones Flask](https://flask.palletsprojects.com/en/stable/testing/)
