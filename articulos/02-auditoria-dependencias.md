# Audité las dependencias de MesaQA con pip-audit

Flask, Waitress y sus dependencias forman parte de lo que se ejecuta al publicar MesaQA. Un análisis de código propio presta poca atención a los avisos de seguridad específicos de una versión de una biblioteca. Para esa revisión utilicé pip-audit y un manifiesto con versiones fijas.

## Procedimiento

```bash
python -m pip install pip-audit==2.10.1
pip-audit -r requirements.txt --format json --output evidencias/dependencias.json
```

El informe registra las versiones examinadas y los avisos conocidos que el servicio consultado devuelve. Si aparece un aviso, se comprueba cómo se usa la biblioteca, se busca la versión corregida y se vuelve a ejecutar la suite antes de publicar. El resultado no determina por sí solo si una ruta concreta de la aplicación es vulnerable.

La auditoría corre en el mismo workflow que las pruebas de API y el análisis estático. El blueprint de despliegue permite asociar la publicación de la imagen a las verificaciones del repositorio. Un cambio en la base de avisos puede alterar el resultado sin que cambie el código, por lo que conviene volver a ejecutar la auditoría.

- [Repositorio público](https://github.com/RichiPodesta1113/mesaqa-si784)
- [GitHub Actions](https://github.com/RichiPodesta1113/mesaqa-si784/actions)
- [Documentación de pip-audit](https://github.com/pypa/pip-audit)

En la ejecución local con pip-audit 2.10.1 se revisaron nueve paquetes y el informe no devolvió avisos. El JSON conserva las versiones comprobadas.
