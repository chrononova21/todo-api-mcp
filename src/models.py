import uuid

from peewee import *

db_proxy = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = db_proxy

class TaskTable(BaseModel):
    task_id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = CharField()
    description = TextField(null=True)
    priority = CharField()
    status = CharField()
    tags = TextField(null=True)

    def save(self, *args, **kwargs):
        return super(TaskTable, self).save(*args, **kwargs)

def db_init():
    db = SqliteDatabase('tasks.db')
    db_proxy.initialize(db)
    db.connect()
    db.create_tables([TaskTable])
    return db

