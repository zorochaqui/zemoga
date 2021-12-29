# zemoga

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```
----------------------------------------------------------------------------------
Esta ruta es para listar el un portafolio, los datos

GET
http://localhost:8000/api/portfolios/1

Respuesta

{
    "imagePath": "images/about.jpg",
    "twitterUser": "elonmusk",
    "id": 1,
    "experience": "Master’s in Software Engineering and Systems and Computer Engineer from Universidad de los Andes, with experience and knowledge in: architecture, design, and software development with highly complex data management in multiple areas.",
    "phone": "+571234567890",
    "email": "santidils7@gmail.com",
    "zipCode": "7777",
    "address": "Bogota, Colombia",
    "name": "Santiago Ardila Acuña"
}

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

En está api se actualiza los datos del portafolio guardado

PUT
http://localhost:8000/api/portfolios/1

ingresa un json con todos estos campos, no es necesario ponerlos todos, ya que puedes poner uno solo

{
    experience  : "data",
    imagePath   : "data",
    name        : "data",
    twitterUser : "data",
    email       : "data",
    address     : "data",
    phone       : "data",
    zipCode     : "data"
}

Salida

{
    "success": "se actualizó correctamente"
}

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
GET 

Está api te lista todos los tweets de una cuenta, puedes poner la cantidad de tweets que quieres ver.

http://localhost:8000/api/portfolios/name/<name>/tweets/<int:quantity>
<name> = elonmusk #nombre de la cuenta
<int:quantity> = 5 #cantidad de tweets

http://localhost:8000/api/portfolios/name/elonmusk/tweets/5

Salida

{
    "tweets": [
        {
            "tweet": "Lex asks great questions https://t.co/TlyuEGoOVA"
        },
        {
            "tweet": "@cleantechnica Most people still have no idea that sustainable energy generation is growing so fast"
        },
        {
            "tweet": "@SpaceXMR 🤣"
        },
        {
            "tweet": "@engineers_feed The resolution of the universe is not smaller than Planck length\nhttps://t.co/hoyZR4d0pP"
        },
        {
            "tweet": "@karpathy All of reality can be simulated with ones &amp; zeroes"
        }
    ]
}

----------------------------------------------------------------------------------