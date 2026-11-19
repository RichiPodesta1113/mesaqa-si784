# MesaQA

MesaQA es una API de demostración para registrar, consultar y cerrar incidencias de pruebas. El proyecto sirve de base a las tres actividades grupales de Calidad y Pruebas de Software SI784.

## Ejecutar

Con Python 3.12, instala las dependencias y arranca el servidor:

```text
python -m pip install -r requirements.txt
waitress-serve --listen=127.0.0.1:8080 --call qa.app:create_app
```

Abre `http://127.0.0.1:8080/health`. La API devuelve JSON.

| Método | Ruta | Resultado |
|---|---|---|
| GET | /health | 200 y estado del servicio |
| GET | /tickets | 200 y hasta 100 incidencias recientes |
| POST | /tickets | 201 y cabecera Location. Acepta JSON con title |
| GET | /tickets/{id} | 200 con la incidencia, o 404 |
| PATCH | /tickets/{id}/close | 200 y estado closed, o 404 |

Usa datos ficticios. La demo usa un tablero compartido sin cuentas de usuarios. La base SQLite local persiste en `data/`. En un servicio de nube sin disco persistente, los datos pueden perderse al redesplegar.

## Verificar

```text
python -m unittest discover -s tests -v
bandit -r qa
pip-audit -r requirements.txt
```

GitHub Actions ejecuta las pruebas con cobertura, Bandit y pip-audit. Los informes de referencia están en `evidencias/`. El Dockerfile ejecuta el servicio como usuario sin privilegios. `render.yaml` define un servicio de demostración en Render con despliegue tras verificaciones aprobadas. El servicio debe conectarse a este repositorio en la cuenta de Render antes del primer despliegue.

## Entregables

- [Análisis estático con Bandit](articulos/01-sast-bandit.md)
- [Auditoría de dependencias con pip-audit](articulos/02-auditoria-dependencias.md)
- [Pruebas de API con unittest](articulos/03-api-testing.md)
- [Guiones de video](articulos/guiones.md)
- [Formularios de proyecto FD01–FD04](proyecto/)
- [Registro de enlaces](entrega.md)
