import data
import sender_stand_request

def test_create_kit_name_1_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba1'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba1']['name']
    print(respuesta_json)

def test_create_kit_name_511_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba2'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba2']['name']
    print(respuesta_json)

def test_create_kit_name_0_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba3'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba2']['name']
    print(respuesta_json)

def test_create_kit_name_512_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba4'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba4']['name']
    print(respuesta_json)

def test_create_kit_name_especial_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba5'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba5']['name']
    print(respuesta_json)

def test_create_kit_name_space_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba6'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba6']['name']
    print(respuesta_json)


def test_create_kit_name_number_letter_result_201():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba7'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 201
    assert respuesta_json['name'] == data.kit_body['prueba7']['name']
    print(respuesta_json)

def test_create_kit_name_parameter_isnot_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba8'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba8']['name']
    print(respuesta_json)

def test_create_kit_name_parameter_diferent_letter_result_400():
    respuesta = sender_stand_request.post_new_client_kit(data.kit_body['prueba9'])
    respuesta_json = respuesta.json()
    assert respuesta.status_code == 400
    assert respuesta_json['name'] == data.kit_body['prueba9']['name']
    print(respuesta_json)