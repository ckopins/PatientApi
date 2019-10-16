from ..entities import Entity, Log
from ..start_up import api_config

Session = api_config.Session

def log(created_by, level='Error', msg=None, trace=None, auto_close=True):
    session = Session()
    newLog = Log.Log(created_by, level=level, trace=trace, msg=msg)

    session.add(newLog)
    session.commit()

    if auto_close:
        session.close()

def str_has_value(value):
    return value and (not value.isspace())

def check_debug(time, function_name):
    if __debug__:
        log('debug', level='DEBUG', msg=f'{function_name} execution time: {time}', auto_close=False)