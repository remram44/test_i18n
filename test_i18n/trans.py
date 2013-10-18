import gettext
import locale
import pkg_resources


# Entry points should be using:
#locale.setlocale(locale.LC_ALL, '')


d = pkg_resources.resource_filename('test_i18n', 'l10n')

languages = [locale.getlocale()[0]]
trans = gettext.translation('test_i18n', d, languages, fallback=True)


def _(msg):
    return trans.ugettext(msg)
def _n(singular, plural, n):
    return trans.ungettext(singular, plural, n)
