# Prueba_eConcept_Group
Prueba de conocimientos backend

# Lenguaje de programacion
* python3
# Framework
* Django (2.1.7)
# Dependencias
* django-cors-headers (2.5.2)
* httpie (opcional)

# Como funciona?
Cuando clone el repositorio, debe entrar a la carpeta prueba. Alli ejecutara el comando "python3 manage.py runserver" el cual ejecutara el servidor web por la url "http://localhost:8000/".
Para hacer la peticion a la api, debe ser a la url "http://localhost:8000/create_user" y enviarle por el metodo POST el JSON.

# Ejemplo
Habiendo instalado la dependencia httpie con el comando "pip3 install httpie", y con el servidor arriba de django, se puede poner el siguiente comando en la consola 

http localhost:8000/create_user pf:='{ "canal": "ECO", "codigotrs": "200000", "date":"200222019","idServices":"01", "vrs":"0.1" }' pv:='{"usuario":{"name":"oscar","password":"123456789", "email":"ariasp26@gmail.com"},"Rol":"admin"}' -v

imediatamente respondera el json acordado, dependiendo del resultado.

# Codigos
En el json, el app respondera los siguientes codigos
* 0000 -> la transaccion fue un exito.
* 0001 -> el canal  enviado no es ECO.
* 0002 -> al hacer la validacion de los datos encuentra un error por ejemplo, no se reconoce el email como un email valido o el limite de caracteres del espacio se excedio. Este error retorna un diccionario siendo la llave el campo que tiene el error y el valor siendo el mensaje del error.
* 0003 -> el email ya existe en la base de datos, no se puede repetir.
# Base de datos
la base de datos se elaboro el SQLite, por ser un una prueba, dada su versatilidad y facil uso, sin embargo puede migrar a cualquier motor de sql, dependiendo de la necesidad
