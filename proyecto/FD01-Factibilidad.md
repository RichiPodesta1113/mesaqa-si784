# FD01 · Informe de factibilidad

**Universidad Privada de Tacna · Calidad y Pruebas de Software SI784**
**Proyecto MesaQA · Versión 0.1 · 19 de noviembre de 2026**

## 1. Descripción y objetivos

MesaQA organiza incidencias de pruebas mediante un identificador y dos estados. El equipo propuesto es MesaQA en Classroom. La cuenta RichiPodesta1113 es el primer integrante registrado al preparar esta versión.

Los reportes informales deben poder contrastarse con pasos de verificación, resultados y responsables. GitHub documenta este problema operativo mediante formularios y tipos de incidencias. En el curso se requiere además que la calidad pueda comprobarse con pruebas y reportes reproducibles. No se midió todavía cuánto tiempo dedica un equipo a localizar incidencias antes de adoptar MesaQA. [Formularios de incidencias de GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)

- **Objetivo de investigación.** Medir con casos repetibles si registrar las incidencias mediante un contrato HTTP permite detectar entradas inválidas y comprobar la persistencia. La medida es la proporción de escenarios de aceptación aprobados.
- **Objetivo de solución.** Cubrir cinco rutas y los estados HTTP esperados con al menos ocho casos automatizados y 95 % de cobertura de línea en el módulo web.
- **Objetivo de control.** Ejecutar dos análisis de seguridad en CI y conservar reportes verificables para cada ejecución.

## 2. Riesgos

| Riesgo | Impacto | Respuesta |
|---|---|---|
| Cierre de actividades en Moodle | Sin envío en plazo | Conservar los repositorios y consultar si el docente habilita una reapertura. |
| Pérdida de datos en hosting efímero | Se pierde la demo anterior | Usar datos sintéticos y contratar almacenamiento persistente solo si se necesita. |
| Segundo integrante sin registrar | Revisión de pares pendiente | Reservar la plaza del grupo y asignar revisión cuando se confirme el integrante. |
| Dependencias o proveedores cambian | Resultados variables | Fijar versiones, guardar el resultado de cada análisis y repetirlo antes del despliegue. |

## 3. Situación actual

Las tareas de ejemplo se pueden registrar con título y estado. Para trabajo académico se requiere un entorno mínimo con Python, Git y SQLite. El prototipo comprueba creación, consulta y cierre. El flujo real con usuarios y responsables se valida en una versión posterior.

## 4. Factibilidad

La versión local ya compila y pasa sus pruebas con Python y SQLite. El equipo puede operarla con comandos documentados. El diseño usa datos de ensayo y evita almacenar información identificable. El alcance mínimo restringe consumo y almacenamiento. La publicación en nube depende del acceso a una cuenta SaaS y de sus condiciones.

## 5. Análisis financiero

Costo directo observado de la ejecución local: S/ 0 adicionales en software. No se contrató un servicio cloud. Cualquier tarifa, disco persistente o costo por consumo se evalúa antes de activar un plan de pago.

## 6. Conclusión

Es factible reproducir la API y sus verificaciones en local. El costo de operación, los experimentos con usuarios y el despliegue público quedan por validar.
