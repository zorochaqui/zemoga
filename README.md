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
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
GET 

http://localhost:8000/api/portfolios/name/<name>/tweets/<int:quantity>

En na

----------------------------------------------------------------------------------