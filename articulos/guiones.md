# Guiones de demostración

Cada guion dura aproximadamente 3 minutos. Muestra el repositorio propio y los resultados reales. Después de desplegar, muestra la URL pública y la respuesta de /health.

## 1. Análisis estático con Bandit

- 0:00–0:25. Presenta MesaQA y explica qué examina el análisis estático.
- 0:25–1:20. Abre qa/app.py y explica la validación de títulos y los parámetros de SQLite.
- 1:20–2:20. Ejecuta Bandit, abre su JSON y muestra el número real de hallazgos.
- 2:20–3:10. Abre el workflow, el artefacto generado y el servicio desplegado cuando esté disponible.

## 2. Auditoría con pip-audit

- 0:00–0:30. Distingue los avisos de dependencias de los hallazgos en el código propio.
- 0:30–1:15. Muestra requirements.txt y explica las versiones fijas.
- 1:15–2:15. Ejecuta pip-audit y abre el informe de los paquetes examinados.
- 2:15–3:10. Muestra cómo GitHub Actions conserva la evidencia y a qué servicio se despliega.

## 3. Pruebas del contrato HTTP

- 0:00–0:35. Muestra POST /tickets y la cabecera Location.
- 0:35–1:35. Explica las pruebas de creación, persistencia, error 404 e idempotencia.
- 1:35–2:30. Ejecuta la suite y muestra el reporte de cobertura.
- 2:30–3:15. Muestra el repositorio y el endpoint /health del servicio publicado.
