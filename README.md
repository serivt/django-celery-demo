# Django Celery Demo
Proyecto de demostración de Django + Celery.

## Pasos
1. Estructura básica del proyecto ([ebd0cf2](https://github.com/serivt/django-celery-demo/commit/ebd0cf20472de884575ed867f49c553bac3d7c90)).
2. Configuración para usar Django junto a Celery ([2038283](https://github.com/serivt/django-celery-demo/commit/203828315370dad27c164054e599beb37dd00124)).
3. Aplicación para demostración de tareas ([4110a9c](https://github.com/serivt/django-celery-demo/commit/4110a9cc45f93f1afc54b1c74fb9f7a42a658be1)).
4. Demostración de tareas periodicas `django-celery-beat` ([f893706](https://github.com/serivt/django-celery-demo/commit/f893706e493b814053325b27118e3658bdb4cb8a)).
5. Demostración de `django-celery-results` ([5189188](https://github.com/serivt/django-celery-demo/commit/51891888b0259087c1a124bd5a64d8930d1d56dc)).

## Como ejecutar
El proyecto esta configurado para ejecutarse con Docker y Docker Compose.
1. Crear imagen.
2. Levantar servicios.
```bash
$ docker build -t django-celery-demo .
$ docker-compose up
```

## Como probar
Para probar el proyecto se debe ejecutar 3 terminales:
1. Servidor de Django.
2. Workers de Celery.
3. Celery Beat.

```bash
$ poetry run python manage.py runserver 0.0.0.0:8000
$ poetry run celery -A config beat -l debug
$ poetry run celery -A config worker -l debug
```
