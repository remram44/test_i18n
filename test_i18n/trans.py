import codecs
import gettext
import locale
import pkg_resources
import sys


# Entry points should be using:
#locale.setlocale(locale.LC_ALL, '')


d = pkg_resources.resource_filename('test_i18n', 'l10n')

trans = gettext.translation('test_i18n', d)


def _(*args):
    return trans.ugettext(*args)


if str == bytes:
    # Python tends to f*ck up, make sure it doesn't decide to use 'ascii'
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
    sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr)
