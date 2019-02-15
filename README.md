## Webscraping y Minería de Redes Sociales
### Febrero de 2019

Desarrollado por:

 * [Hernán Avila](hernan.avila@datalytics.com)
 * [Jorge Quintana](jorge.quintana@datalytics.com) 

Proyecto de recopilación de datos para la Cámara de Comercio de Medellín usando técnicas de Webscraping y Minería de Redes Sociales en Python. Las aplicaciones son desplegadas en Instancias (Compute Engine) de Google Cloud Platform usando Docker. Para construir las imagenes basta con instalar Docker de forma local y ejecutar el siguiente comando: 

```
  docker build -t [NOMBRE_DE_LA_IMAGEN] .                              # Si se está dentro de la carpeta que contiene el Dockerfile
  docker build -t [NOMBRE_DE_LA_IMAGEN] -f [RUTA_DEL_DOCKERFILE] .     # Si se está en una carpeta externa que no contiene el Dockerfile
```

Para arrancar el contenedor de forma local se debe ejecutar el siguiente comando:

```
  docker run -d --name [NOMBRE_DEL_CONTENEDOR] -v [VOLUMEN_HOST]:[VOLUMEN_CONTENEDOR] [NOMBRE_DE_LA_IMAGEN]
```

Para poder acceder a los resultados de forma local se debe crear un volumen, en donde estarán los archivos necesarios para que el contenedor funcione de forma correcta, y en donde se gurdará el archivo con los resultados del proceso, en este caso un archivo csv con la siguiente estructura: economista_[NOMBRE_CLUSTER]_antioquia.csv. Para monitoriar si el contenedor está corriendo y cuántos recursos está utilizando se pueden ejecutar los siguientes comandos, respectivamente:

```
  docker ps
  docker stats
```

#### TODO: 
  * Se debe documentar todo el proceso
  * Se deben generar pruebas sobre los .py
  * Se deben optimizar las imagenes usando como base Linux Alpine y no Ubuntu, ya que las imagenes quedan de más de 1GB. Para esto se debe probar y documentar la forma de instalar pandas y Numpy (desde los .whl) en Linux Alpine

Versión preliminar no aprobada
