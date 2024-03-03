def raise_system_exit_exception():
    raise SystemExit(1)


def sum(x,y):
    return x + y


def check_json_data(data):
    if type(data) == dict:
        return "OK"
    else:
        raise Exception("FAILED")

