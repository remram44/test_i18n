import gettext
import locale
import pkg_resources


# Entry points should be using:
#locale.setlocale(locale.LC_ALL, '')
#test_i18n.trans.setup_translation()


if str == bytes:
    string_types = basestring
else:
    string_types = str


trans = gettext.NullTranslations()


def setup_translation(languages=[]):
    global trans

    if isinstance(languages, string_types):
        languages = [languages]

    d = pkg_resources.resource_filename('test_i18n', 'l10n')
    
    lang = locale.getlocale()[0]
    if lang is not None:
        languages.insert(0, lang)
    trans = gettext.translation('test_i18n', d, languages, fallback=True)


if hasattr(trans, 'ugettext'):
    def _(*args, **kwargs):
        tr = trans.ugettext(*args)
        if kwargs:
            tr = tr.format(**kwargs)
        return tr
    def _n(singular, plural, n, **kwargs):
        tr = trans.ungettext(singular, plural, n)
        if kwargs:
            tr = tr.format(**kwargs)
        return tr
else:
    # Yes, ugettext was removed from Python 3. Yes, this is pathetic.
    def _(*args, **kwargs):
        tr = trans.gettext(*args)
        if kwargs:
            tr = tr.format(**kwargs)
        return tr
    def _n(singular, plural, n, **kwargs):
        tr = trans.ngettext(singular, plural, n)
        if kwargs:
            tr = tr.format(**kwargs)
        return tr
