import gettext
import locale
import pkg_resources


# Entry points should be using:
#locale.setlocale(locale.LC_ALL, '')


d = pkg_resources.resource_filename('test_i18n', 'l10n')

languages = []
lang = locale.getlocale()[0]
if lang is not None:
    languages.append(lang)
trans = gettext.translation('test_i18n', d, languages, fallback=True)


if hasattr(trans, 'ugettext'):
    def _(msg):
        return trans.ugettext(msg)
    def _n(singular, plural, n):
        return trans.ungettext(singular, plural, n)
else:
    # Yes, ugettext was removed from Python 3. Yes, this is pathetic.
    def _(msg):
        return trans.gettext(msg)
    def _n(singular, plural, n):
        return trans.ngettext(singular, plural, n)
