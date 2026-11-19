# Probé el contrato de una API de incidencias con unittest

Una prueba de API debe comprobar la respuesta y el efecto sobre el estado. En MesaQA, al crear una incidencia se espera un HTTP 201, un estado inicial open y una cabecera Location que permite recuperar el recurso. Además, una solicitud inválida debe dejar la base de datos intacta.

Cada caso crea una base SQLite temporal. El cliente de pruebas de Flask invoca la aplicación sin depender de Internet. Las pruebas comprueban lectura, orden de las incidencias, tipos de contenido, tamaños máximos, errores 404 y el cierre repetido de una incidencia. Una segunda instancia con la misma base comprueba que el cierre quede guardado.

```bash
python -m pip install -r requirements.txt
python -m pip install coverage==7.17.3
coverage run --source=qa -m unittest discover -s tests -v
coverage report
```

La ejecución local aprobó nueve pruebas y cubrió 66 de 66 líneas ejecutables. La cobertura mide ejecución de líneas. El comportamiento esperado se comprueba con las aserciones sobre el código HTTP, el cuerpo JSON, las cabeceras y la persistencia.

La automatización ejecuta las mismas pruebas y genera un informe XML antes del despliegue. Después de publicar en un servicio público, se puede consultar GET /health para verificar que el proceso responde a través de la red.

- [Repositorio público](https://github.com/RichiPodesta1113/mesaqa-si784)
- [GitHub Actions](https://github.com/RichiPodesta1113/mesaqa-si784/actions)
- [Pruebas de aplicaciones Flask](https://flask.palletsprojects.com/en/stable/testing/)
