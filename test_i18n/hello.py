from .trans import _


def say_hello(name):
    print _(u"Hello {name}!").format(name=name)
