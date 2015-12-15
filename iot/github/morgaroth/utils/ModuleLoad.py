import sys
import traceback


class MyModuleLoadError(Exception):
    name = "UNNAMED"

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.with_traceback([])


def exc(previous, t):
    def excepthook(type, value, tb):
        if type is t:
            traceback.print_exception(type, value, 0)
        else:
            previous(type, value, tb)

    return excepthook


sys.excepthook = exc(sys.excepthook, MyModuleLoadError)
