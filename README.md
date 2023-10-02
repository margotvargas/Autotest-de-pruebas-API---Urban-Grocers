<h1 align="center">
# PROYECTO SPRINT 6
</h1>

## PRUEBAS API - URBAN GROCERS

Este proyecto implica la creación de pruebas API, la cual administra un servicio de entrega de comestibles, abarcando funciones como la creación de usuarios, gestión de pedidos, administración de almacenes y delivery.
Se nos brinda realizar 9 pruebas automatizadas de la lista de comprobación para la creación de un kit, relacionado a un usuario. Los cuales se han realizado a traves del Python, previa instalacion del Pytest y request.

## API
Servidor: tripleten-services.com
Se utilizaron 2 endpoint:
- /api/v1/users
- /api/v1/kits

## Funciones
Para poder relizar la lista, se ha creado 2 funciones principales:

- get_new_user_token(): el cual nos permite la creación de un nuevo usuario y obteniendo el token de autenticación.
- post_new_client_kit(name): nos permite crear el kit de comestibles asociando la autenticación del usuario creado.


## Lista de comprobación

Se han creado la lista de comprobación, para el campo NAME en la solicitud de creación de un kit de productos.

| DESCRIPCION | RESPUESTA ESPERADA |
| ------ | ------ |
| Prueba 1: Crear un kit con nombre de longitud mínima de 1 caracter | Código de respuesta esperada — 201 |
| Prueba 2: Crear un kit con nombre con longitud de 511 caracteres | Código de respuesta esperada — 201  |
| Prueba 3: Crear un kit con nombre con longitud de 0 caracteres | Código de respuesta esperada — 400  |
| Prueba 4: Crear un kit con nombre con longitud de 512 caracteres | Código de respuesta esperada — 400  |
| Prueba 5: Crear un kit con nombre de caracteres especiales:"№%@",  | Código de respuesta esperada — 201  |
| Prueba 6: Crear un kit con espacios en blanco en campo nombre | Código de respuesta esperada — 201  |
| Prueba 7: Crear un kit con nombre tipo de caracteres: números enteros | Código de respuesta esperada — 201  |
| Prueba 8: Crear un kit sin mombre en contenido del parametro requerido  | Código de respuesta esperada — 400  |
| Prueba 9: Crear un kit con un parametro diferente (numeros): 123  | Código de respuesta esperada — 400  |

En cada prueba se realizó su respectiva función, ejemplo: test_create_kit_name_1_letter_result_201()


> Para las pruebas 1, 2, 5, 6, 7 se tuvo éxito en la creación del kit, obteniendo el resultado esperado.

> Por otro lado, se encontró bugs para las pruebas 3, 4 y 9 ya que no se obtuvo el resultado esperado 400, sino se pudo realizar el registro obteniendo un resultado 201.

> Por último, para la prueba 8 "Crear un kit sin mombre en contenido del parametro requerido", se obtuvo como respuesta el codigo 500, siendo el esperado el 400, por el cual también obtenemos un bug a reportar.
