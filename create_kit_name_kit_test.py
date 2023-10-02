import data
import sender_stand_request

#PRUEBA 1
def test_create_kit_name_1_letter_result_201(): #Realizamos una peticion a la API para crear un nuevo kit y obtener la respuesta y filtrarla
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba1']) #Realizamos la peticion a API de crear kit llamando a la funcion de crear kit en archivo sender_stand
    respuesta_json = respuesta.json() #Obtenemos la respuesta y la filtramos para obtener el nombre y el status code
    assert respuesta.status_code == 201 #Realizamos un assert para comprobar el resultado esperado sea igual al 201
    assert respuesta_json['name'] == data.kit_body['prueba1']['name'] #por eso obtenemos el json entramos a name y la comparamos con la prueba1
    print(respuesta_json) #Imprimimos la respuesta en formato Json

#PRUEBA 2
def test_create_kit_name_511_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba2'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba2']['name']
    print(respuesta_json)

#PRUEBA 3
def test_create_kit_name_0_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba3'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba2']['name']
    print(respuesta_json)

#PRUEBA 4
def test_create_kit_name_512_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba4'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba4']['name']
    print(respuesta_json)

#PRUEBA 5
def test_create_kit_name_especial_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba5'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba5']['name']
    print(respuesta_json)

#PRUEBA 6
def test_create_kit_name_space_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba6'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba6']['name']
    print(respuesta_json)

#PRUEBA 7
def test_create_kit_name_number_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba7'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba7']['name']
    print(respuesta_json)

#PRUEBA 8
def test_create_kit_name_parameter_isnot_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba8'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba8']['name']
    print(respuesta_json)

#PRUEBA 9
def test_create_kit_name_parameter_diferent_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba9'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba9']['name']
    print(respuesta_json)

