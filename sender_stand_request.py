import requests
import configuration
import data

def get_new_user_token():
    respuesta = requests.post(configuration.URL_SERVIDOR + configuration.USER_ENDPOINT, json=data.usuario_nuevo)
    respuesta_json = respuesta.json()
    return respuesta_json['authToken']

auth_token = get_new_user_token()
authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}
print(authorization)

def post_new_client_kit(name):
    respuesta= requests.post(configuration.URL_SERVIDOR + configuration.KIT_ENDPOINT,
                             json=name,
                             headers=authorization
                             )
    return respuesta

