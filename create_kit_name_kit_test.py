import data
import sender_stand_request

def test_create_kit_name_1_letter_result_201(): #peticion a la API para crear un nuevo kit #Obtener la respuesta y filtrarla
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba1']) #Realizamos la peticion a API de crear kit llamando a la funcion de crear kit en archivo sender_stand
    respuesta_json = respuesta.json() #Obtenemos la respuesta y la filtramos para obtener el nombre y el status code
    assert respuesta.status_code == 201 #respuesta esperada pero trae mucha informacion
    assert respuesta_json['name'] == data.kit_body['prueba1']['name'] #por eso obtenemos el json entramos a name y la comparamos con la prueba1
    print(respuesta_json)


def test_create_kit_name_511_letter_result_201(): #peticion a la API para crear un nuevo kit #Obtener la respuesta y filtrarla
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba2']) #Realizamos la peticion a API de crear kit llamando a la funcion de crear kit en archivo sender_stand
    respuesta_json = respuesta.json() #Obtenemos la respuesta y la filtramos para obtener el nombre y el status code
    assert respuesta.status_code == 201 #respuesta esperada
    assert respuesta_json['name'] == data.kit_body['prueba2']['name'] #respuesta
    print(respuesta_json)