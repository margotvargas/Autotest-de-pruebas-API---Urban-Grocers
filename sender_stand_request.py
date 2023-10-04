import requests
import configuration
import data

def get_new_user_token(): ##Función para crear el usuario y obtener el token
    ##1. Se realiza la peticion a las APIs del servidor en el archivo configuration.py y los datos del nuevo usuario a crear en archivo data.py
    respuesta = requests.post(configuration.URL_SERVIDOR + configuration.USER_ENDPOINT, json=data.usuario_nuevo)
    # 2. Obtiene la respuesta y la interpretamos como JSON en la variable "respuesta_json".
    respuesta_json = respuesta.json()
    ##3. Aqui extraemos solo el alfanumérico del token con las []
    return respuesta_json['authToken']

auth_token = get_new_user_token() #4. Asignamos la función a la variable auth_token

#5. Ya tenemos el token pero lo necesitamos en el formato bearer como lo indica en la documentacion de la API para la creacion del kit
authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}
print(authorization) #6. Imprimimos la creación del usuario con el token incluyendole el string "Bearer".


#Funcion para crear el kit con el token del usuario.
def post_new_client_kit(name):
    #Se realiza una solicitud POST a la URL del servidor más la ruta del kit (/api/v1/kits) utilizando la biblioteca requests.
    #Se incluyen encabezados de autorización en la solicitud, que se obtienen al enviar una solicitud POST para crear un nuevo usuario y extrayendo el token de autenticación.
    respuesta= requests.post(configuration.URL_SERVIDOR + configuration.KIT_ENDPOINT,
                             json=name,
                             headers=authorization
                             )
    return respuesta #La respuesta de la solicitud se devuelve.

