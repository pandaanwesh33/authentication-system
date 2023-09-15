from peewee import PostgresqlDatabase
from playhouse.db_url import connect
import config

db = connect(config.DATABASE_URL)