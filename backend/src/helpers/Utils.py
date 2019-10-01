from ..entities import Entity, Log

def log(session, created_by, level='Error', msg=None, trace=None, auto_close=True):
    newLog = Log.Log(created_by, level=level, trace=trace, msg=msg)

    session.add(newLog)
    session.commit()

    if auto_close:
        session.close()

def str_has_value(value):
    return value and (not value.isspace())

def check_debug(session, time, function_name):
    if __debug__:
        log(session, 'debug', level='DEBUG', msg=f'{function_name} execution time: {time}', auto_close=False)