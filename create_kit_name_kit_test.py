import data
import sender_stand_request


#PRUEBA 1: Crear un kit con longitud mínima de 1 caracter.
def test_create_kit_name_1_letter_result_201():
    #1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    #con el nombre del kit correspondiente a 1 caracter "prueba1" desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba1'])
    #2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    #3. Verifica que el código de estado de la respuesta sea 201.
    assert respuesta.status_code == 201
    #4. Verifica que el nombre del kit en la respuesta coincida con el nombre proporcionado en el cuerpo de la solicitud (diccionario prueba1 del archivo data.kit_body)
    assert respuesta_json['name'] == data.kit_body['prueba1']['name']
    #5. Finalmente, se imprime la respuesta en formato Json.
    print(respuesta_json)

#PRUEBA 2: Crear un kit con longitud máxima de 511 caracteres.
def test_create_kit_name_511_letter_result_201():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente a 511 caracter "prueba2" desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba2'])
    # 2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    # 3. Verifica que el código de estado de la respuesta sea 201.
    assert respuesta.status_code == 201
    # 4. Verifica que el nombre del kit en la respuesta coincida con el nombre proporcionado en el cuerpo de la solicitud (diccionario prueba2 del archivo data.kit_body)
    assert respuesta_json['name'] == data.kit_body['prueba2']['name']
    # 5. Se imprime la respuesta del nuevo kit creado en formato Json.
    print(respuesta_json)

#PRUEBA 3: Crear un kit de 0 caracteres en name.
def test_create_kit_name_0_letter_result_400():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente "prueba3" campo vacio, desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba3'])
    # 2. Verifica que el código de estado de la variable respuesta sea igual a 400.
    assert respuesta.status_code == 400

#PRUEBA 4: Crear un kit de 512 caracteres en name (Limite superior + 1)
def test_create_kit_name_512_letter_result_400():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente "prueba4" con 512 caracteres, desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba4'])
    # 2. Verifica que el status code de la variable respuesta sea igual a 400.
    assert respuesta.status_code == 400

#PRUEBA 5: Crear un kit con caracteres especiales
def test_create_kit_name_especial_letter_result_201():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente "prueba5"  desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba5'])
    # 2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    # 3. Verifica que el código de estado de la respuesta sea 201.
    assert respuesta.status_code == 201
    # 4. Verifica que el nombre del kit en la respuesta coincida con el nombre proporcionado en el cuerpo de la solicitud (diccionario prueba5 del archivo data.kit_body)
    assert respuesta_json['name'] == data.kit_body['prueba5']['name']
    #5. Finalmente, se imprime la respuesta en formato Json.
    print(respuesta_json)

#PRUEBA 6: Crear un kit con espacios en blanco en nombre
def test_create_kit_name_space_letter_result_201():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente "prueba6" desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba6'])
    # 2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    # 3. Verifica que el código de estado de la respuesta sea 201.
    assert respuesta.status_code == 201
    # 4. Verifica que el nombre del kit en la respuesta coincida con el nombre proporcionado en el cuerpo de la solicitud (diccionario prueba6 del archivo data.kit_body)
    assert respuesta_json['name'] == data.kit_body['prueba6']['name']
    print(respuesta_json) #Se imprime la respuesta en formato Json.

#PRUEBA 7: Crear un kit con números enteros en nombre
def test_create_kit_name_number_letter_result_201():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # con el nombre del kit correspondiente "prueba7" desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba7'])
    # 2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    # 3. Verifica que el código de estado de la respuesta sea 201.
    assert respuesta.status_code == 201
    # 4. Verifica que el nombre del kit en la respuesta coincida con el nombre proporcionado en el cuerpo de la solicitud (diccionario prueba7 del archivo data.kit_body)
    assert respuesta_json['name'] == data.kit_body['prueba7']['name']
    print(respuesta_json)

#PRUEBA 8: Crear un kit donde el parámetro no se pasa en la solicitud:
def test_create_kit_name_parameter_isnot_letter_result_400():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # sin indicar el parámetro { } "prueba8", desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba8'])
    # 2. Verifica que el status code de la variable respuesta sea igual a 400.
    assert respuesta.status_code == 400

#PRUEBA 9: Crear un kit donde se registra un parámetro diferente (número).
def test_create_kit_name_parameter_diferent_letter_result_400():
    # 1. Llama a la API con la función para crear un kit "post_new_client_kit" definida en el archivo sender_stand_request.py
    # indicando como parámetro números en "prueba9", desde el archivo data.kit_body, almacenandola en la variable "respuesta"
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba9'])
    # 2. Verifica que el status code de la variable respuesta sea igual a 400.
    assert respuesta.status_code == 400
