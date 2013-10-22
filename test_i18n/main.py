# -*- coding: utf-8 -*-

import codecs
import locale
import sys
import os


def setup():
    app_dir = os.path.dirname(os.path.abspath(__file__))

    locale.setlocale(locale.LC_ALL, '')

    # Python 2 tends to f*ck up, make sure it doesn't decide to use 'ascii'
    if str == bytes:
        writer = codecs.getwriter(locale.getpreferredencoding())
        sys.stdout = writer(sys.stdout)
        sys.stderr = writer(sys.stderr)

    # Setup the Python path
    try:
        import test_i18n
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(app_dir, '..')))
        try:
            import test_i18n
        except ImportError:
            sys.stderr.write(_(u"Couldn't setup the Python path\n"))
            sys.exit(2)

    from test_i18n.trans import setup_translation
    setup_translation()


def main():
    setup()

    from test_i18n.hello import say_hello
    if len(sys.argv) >= 2:
        say_hello(sys.argv[1])
    else:
        say_hello(u'rémi')
