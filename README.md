# Yajuu! respuestas
### _Reviviendo una leyenda_

Yajuu es un proyecto pequeño desarrollado por una sola persona para intentar emular lo que alguna vez fue una pagina muy interesante de preguntas y respuestas.



El proyecto actualmente esta en una fase **muy temprana** de desarrollo y no representa el producto final.

**Nombre del desarrollador**: Michael Franco
**Tecnologias usadas**: HTML5, CSS, Python con Django.

## Características del proyecto

- El nombre del proyecto oficial en django es: Yajuu
- El proyecto actual tiene 4 aplicaciones con sus respectivos **M**odelos, **V**istas y **T**emplates: -->  (_Estas aplicaciones no se encuentran en su versión final y podrían cambiar_)

| Nombre App          |Modelos                         |Vistas                         |Templates |
|----------------|-------------------------------|-----------------------------|--------|
|home| Avatar           | get_avatar / index / search / register /user_update / avatar_load          |index /  avatar_form / login / register / user_form / contact(_en construcción_)|  
|mod|Moderator            |mod_form            |mod_form|
|post|Post|post_form / post_detail / create_model_view(_en revisión_)|post_index / post_detail
|users|User|user_form / show_data(_en revisión_)|user_form

## Instalación

Por favor copiar el repositorio en la rama correspondiente para este proyecto, la rama es: **yajuu-development**

En una terminal , bajamos el repositorio:
```sh
git pull origin yajuu-develpment
git checkout yajuu-development
```
Listo!
