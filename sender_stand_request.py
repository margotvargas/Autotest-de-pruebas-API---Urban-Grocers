import requests
import configuration
import data

def get_new_user_token(): #Función para crear el usuario y obtener el token

    ##1. Haremos la petición al servidor (URL) y a las APIS del archivo configuration, asi como los datos para la creación del nuevo usuario del archivo data
    respuesta = requests.post(configuration.URL_SERVIDOR + configuration.USER_ENDPOINT,
                              json=data.usuario_nuevo)

    ##2. Al ya obtener la respuesta del general, solo extraemos el token completo de json
    respuesta_json=respuesta.json()
    ##3. Aqui extraemos solo el alfanumérico con las [] del diccionario y le asignamos una variable
    return respuesta_json['authToken']

auth_token = get_new_user_token()
#4 Obtuvimos el token pero lo necesitamos en el formato del encabezado incluyendo bearer, como lo indica en la documentación de la API para la creacion del kit.
authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}
print(authorization)


#Función para tener el kit
def post_new_client_kit(name):
    respuesta= requests.post(configuration.URL_SERVIDOR + configuration.KIT_ENDPOINT,
                             json=name,
                             headers=authorization
                             )

    return respuesta




