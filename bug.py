import traceback

metaslash = 1


def print_names(names):
    neal = 'neal'
    michelle = 'michele'
    eric = 5
    print("Local values: %(neal)s %(michele)s %(eric)s" % locals())


class Nothing:
    def __init__(self):
        self.value = None

    def print_value(self, value):
        print(value)

    def set(self, value):
        self.value = value


def try_to_do_something(value):
    try:
        if not value:
            raise RuntimeError("Hey, there's no value")
        print_names('a, b, c')
    except Exception:
        traceback.print_exc()


def set_global(value=None):
    global metaslash
    metaslash = value
    print('Old MetaSlash value is:', metaslash)
    useless = Nothing()
    print('a useless value is:', useless.value)

set_global(50)