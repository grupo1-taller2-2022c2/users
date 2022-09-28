from alembic import op
from sqlalchemy import Table, MetaData

# get metadata from current connection
meta = MetaData(bind=op.get_bind())

# pass in tuple with tables we want to reflect, otherwise whole database will get reflected
meta.reflect(only=('users',))

# define table representation
users = Table('users', meta)

# insert records
op.bulk_insert(users,
               [
                   {'email': 'agus_su@gmail.com', 'password': '123'},
                   {'email': 'chino@hotmail.com', 'password': '1234'},
                   {'email': 'mati@yahoo.com', 'password': '1235'},
                   {'email': 'juani@gmail.com', 'password': '1236'},
                   {'email': 'cristo@gmail.com', 'password': '1237'}])
