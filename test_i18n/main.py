# -*- coding: utf-8 -*-

import codecs
import locale
import sys
import os


def setup():
    app_dir = os.path.dirname(os.path.abspath(__file__))

    locale.setlocale(locale.LC_ALL, '')

    # Python tends to f*ck up, make sure it doesn't decide to use 'ascii'
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
    sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr)

    # Setup the Python path
    try:
        import test_i18n.main
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(app_dir, '..')))
        try:
            import test_i18n.main
        except ImportError:
            sys.stderr.write(_(u"Couldn't setup the Python path\n"))
            sys.exit(2)


def main():
    setup()

    from test_i18n.hello import say_hello
    if len(sys.argv) >= 2:
        say_hello(sys.argv[1])
    else:
        say_hello(u'rémi')
