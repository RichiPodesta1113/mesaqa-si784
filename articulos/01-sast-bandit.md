# Analicé el código de una API Flask con Bandit

Un detector de dependencias no revisa cómo una aplicación construye sus consultas. Para examinar el código propio de MesaQA, una API de incidencias de pruebas, ejecuté Bandit sobre el paquete qa. Bandit revisa el árbol sintáctico de Python y señala patrones inseguros para revisión.

## Implementación

MesaQA recibe JSON y guarda los títulos de las incidencias en SQLite. Limité el tamaño del cuerpo a 8 KiB y el título a 120 caracteres. Las consultas usan parámetros de SQLite para separar los valores de la instrucción SQL. La validación de entrada preserva el contrato de la API y las consultas parametrizadas evitan interpolar valores en SQL.

```bash
python -m pip install -r requirements.txt
python -m pip install bandit==1.9.4
bandit -r qa -f json -o evidencias/bandit.json
```

El informe de la ejecución local registró cero hallazgos de Bandit. Ese resultado corresponde al código y a las reglas analizadas. La revisión de autorización en un sistema con usuarios, las pruebas de concurrencia y la auditoría de dependencias requieren verificaciones adicionales.

El workflow de GitHub ejecuta el mismo análisis y conserva el JSON como artefacto. El Dockerfile empaqueta la API con Waitress y un usuario sin privilegios. El repositorio incluye el blueprint de Render para vincular el despliegue a verificaciones aprobadas.

- [Repositorio público](https://github.com/RichiPodesta1113/mesaqa-si784)
- [GitHub Actions](https://github.com/RichiPodesta1113/mesaqa-si784/actions)
- [Documentación de Bandit](https://bandit.readthedocs.io/en/latest/start.html)
