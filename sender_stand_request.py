import requests
import configuration
import data

def obtener_token(): #Función para crear el usuario y obtener el token
    ##1. Haremos la petición al servidor y la respuesta nos la mostrara en respuesta_token_usuario (de data y configuration)
    respuesta = requests.post(configuration.URL_SERVIDOR + configuration.USER_ENDPOINT,
                              json=data.usuario_nuevo)
    ##print(respuesta_token_usuario) #Aqui muestra la respuesta general del 201

    ##2. Al ya obtener la respuesta del 201, extraemos el token de json
    respuesta_json=respuesta.json()
    #print(respuesta_json) #Esta es la respuesta del JSON muestra el authToken completo pero solo queremos el alfanumérico

    ##3. Aqui extraemos solo el alfanumérico con las [] del diccionario y le asignamos una variable auth_token e imprimimos para comprobar
    #auth_token = respuesta_json['authToken']
    #print(auth_token)

    ##4. Lo convertimos a funcion y la llamamos
    # con return
    return respuesta_json['authToken']

auth_token = obtener_token()#ya tenemos el token pero lo necesitamos en el formato bearer
# como lo indica en la documentacion de la API para la creacion del kit
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


def imprimir_resultado_post_kit(name):
    resultado = post_new_client_kit(name)

    print("Estado de la solicitud:", resultado.status_code)



