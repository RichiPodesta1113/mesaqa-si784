# FD02 · Documento de visión

**MesaQA · Calidad y Pruebas de Software SI784 · Versión 0.1**

## Introducción

El objetivo es que un equipo académico pueda registrar incidencias de sus pruebas, recuperar el estado y demostrar con evidencia qué partes del flujo funcionan. La interfaz de la primera versión es una API JSON.

## Posicionamiento

Para estudiantes que necesitan compartir el estado de una incidencia sin montar un gestor completo, MesaQA ofrece un flujo de creación y cierre con un contrato comprobable. Un informe de prueba puede citar el identificador y la respuesta obtenida.

## Interesados

| Perfil | Necesidad | Resultado esperado |
|---|---|---|
| Estudiante que ejecuta pruebas | Registrar una observación | Identificador, estado inicial y enlace de consulta |
| Estudiante que desarrolla | Consultar incidencias recientes | Lista por creación descendente |
| Revisor | Comprobar el comportamiento documentado | Pruebas repetibles, cobertura y reportes de seguridad |

## Capacidades, alcance y dependencias

La primera versión crea, lista, consulta y cierra incidencias. Expone una verificación de salud y guarda el estado en SQLite. Usa Python 3.12, Flask, Waitress y un sistema de archivos que permita escritura a la identidad del contenedor. El acceso compartido sin cuentas se limita a datos de demostración. Las sesiones, la autorización, la interfaz gráfica y las integraciones quedan fuera de esta primera versión.

## Criterios de éxito

El servicio responde a /health con HTTP 200. Los casos inválidos se rechazan sin crear filas. Cerrar una incidencia dos veces conserva el estado. GitHub Actions genera evidencia reproducible. Una publicación pública se confirma sólo cuando el endpoint del proveedor responde.
