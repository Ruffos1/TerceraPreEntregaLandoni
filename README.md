# TerceraPreEntregaLandoni
# Formulario de búsqueda de clientes en Django

Este proyecto muestra un ejemplo de cómo crear un formulario de búsqueda de clientes utilizando Django. El formulario permite buscar clientes en función de su nombre, apellido, fecha de nacimiento, país y suscripción.

## Orden de prueba de las funcionalidades

1. Configuración del entorno y la base de datos.
2. Creación de los modelos `Pais`, `Suscripcion` y `Cliente`.
3. Creación del formulario de búsqueda utilizando el modelo `Cliente`.
4. Implementación de la vista `buscar_clientes` que procesa la búsqueda y muestra los resultados.
5. Creación de las plantillas HTML `buscar_clientes.html` y `resultado_busqueda.html` para mostrar el formulario y los resultados.
6. Configuración de las URLs para acceder a la vista de búsqueda.
7. Ejecución del servidor de desarrollo y acceso al formulario de búsqueda.

## Funcionalidades principales

- **Formulario de búsqueda**: El formulario de búsqueda permite ingresar los criterios de búsqueda, como nombre, apellido, fecha de nacimiento, país y suscripción.
- **Búsqueda de clientes**: La vista `buscar_clientes` procesa los criterios de búsqueda y realiza la consulta en la base de datos para obtener los resultados correspondientes.
- **Filtrado de resultados**: Los clientes se filtran en función de los criterios de búsqueda proporcionados. Solo se muestran aquellos que cumplen con los criterios seleccionados.
- **Interfaz de usuario amigable**: El formulario de búsqueda y los resultados se muestran utilizando plantillas HTML, lo que facilita la interacción del usuario con la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes sugerencias para mejorar el proyecto, no dudes en abrir un issue o enviar un pull request.

## Licencia
