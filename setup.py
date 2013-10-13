from __future__ import unicode_literals

from setuptools import setup


setup(name='test_i18n',
      version='0.1',
      packages=['test_i18n'],
      description="This is a test package for gettext",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      license='Public Domain',
      package_data = {
        'test_i18n': ['l10n/*.mo'],
      },
      keywords=['python', 'i18n', 'gettext'],
      classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization'])
