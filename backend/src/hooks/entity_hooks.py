from sqlalchemy import event
from ..entities import Entity

# @event.listens_for(Entity.Entity, 'before_insert')
# def before_entity_insert(mapper, connection, target):
#     temp = 1
#     print(target)
