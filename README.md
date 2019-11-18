# Documentacion de social auth

https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
https://medium.com/@katherinekimetto/simple-facebook-social-login-using-django-rest-framework-e2ac10266be1
https://github.com/RealmTeam/django-rest-framework-social-oauth2#facebook-example
https://pastebin.com/raw/08iLNCJc
https://pypi.org/project/django-rest-framework-social-oauth2/
https://python-social-auth-docs.readthedocs.io/en/latest/backends/facebook.html
https://www.bogotobogo.com/python/Django/Python-Django-OAuth2-Getting-Client-ID-Application-ID-Social-Sites-Facebook-Twitter-Google.php
https://developers.facebook.com/apps/1357758071069410/settings/basic/
https://stackoverflow.com/questions/33875919/importerror-cannot-import-name-serializer
https://mmaguero.github.io/MII-SSBW16-17/Tarea_8.html

# Tienda Duoc
Aplicacion en django para venta de articulos para proyecto Duoc

## Setup
`pip install -r requirements.txt`

### Usuarios

Tres cuentas:

| User | Password |
| ---- | -------- |
| admin | passwordpassword |
| client | passwordpassword |
| client2 | passwordpassword |

Los clientes pueden ver los productos y hacer ordenes, el administrador puede agregar productos y hacer ordenes.


## Notes
Detalles no funcionales:

- El email no es totalmente funcional.
- No hay tests unitarios.
