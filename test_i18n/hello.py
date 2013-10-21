from .trans import _, _n


def say_hello(name):
    print(_(u"Hello {name}!", name=name))

    for i in (2, 1):
        print(_n(u"{i} bottle of beer on the wall, {i} bottle of beer.",
                 u"{i} bottles of beer on the wall, {i} bottles of beer.",
                 i,
                 i=i))
        print(_n(u"Take one down and pass it around, {i1} bottle of beer on "
                 u"the wall.",
                 u"Take one down and pass it around, {i1} bottles of beer on "
                 u"the wall.",
                 i-1,
                 i1=i-1))
