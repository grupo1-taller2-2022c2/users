# users

## Base de datos
- Se corre en el container postgres-container (servicio dev_db del docker-compose)
  
- IMPORTANTE: Si agregamos, modificamos, o lo que sea un modelo en app/models (ej: agrego una columna al modelo user_models), entonces debemos hacer:
  
  0. **Si es que creamos un nuevo archivo de models, lo tenemos que agregar al archivo `alembic/env.py` a la línea `from app.models import Base, ..., acá!`** para que alembic pueda trackear las tablas de ese archivo
  1. ```alembic revision --autogenerate -m "nombre_del_cambio"``` que va a generar una nueva versión de la base
  2. Vamos a alembic/versions, buscamos la versión que recién creamos y comprobamos que el upgrade y downgrade estén bien (si no, los modificamos)
  3. ```alembic upgrade head``` para que impacte el cambio en la base de datos. Este comando es el que también se corre ni bien se levanta el container de la base, ya que esta empieza vacía y debemos popularla con la estructura
  
- Si queremos modificar la base pero hacerlo manualmente (y no depender de que lo detecte de app/models), lo que hacemos es:
  1. ```alembic revision -m "nombre_del_cambio"```
  2. Vamos a alembic/versions, buscamos la versión que recién creamos y completamos el upgrade y downgrade
  3. ```alembic upgrade head```

- Para agregar valores automáticamente (que siempre queramos que estén en la base por ej. para probar) podemos agregar los valores tal como se ve en la migration `..._insert_values_to_tables` en `alembic/versions` debajo de los que ya se agregan. De ser necesario, importar tablas del models. **IMPORTANTE**: poner en el depends_on a los códigos de las migrations de las que depende (no podés agregar valores a una tabla que no fue creada todavía)
    
- Si nos quisiéramos conectar desde pgadmin/dbeaver/etc., tenemos que conectarnos a ese container (es el servidor), con lo cual:
  - Para saber la IP (Host) de ese container hacemos ```docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-container```
  - El usuario es `postgres`
  - La contraseña es `grupo1`
  - El puerto es el `5432` (es el puerto dentro del container, en nuestra máquina lo mapié al 6543 para que no moleste)

- Cualquier cosa visitar [este enlace para más info de alembic](https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/)