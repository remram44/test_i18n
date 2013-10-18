from __future__ import unicode_literals

import os
from setuptools import setup


translation_files = []
def add_translations(realpath, path):
    for f in os.listdir(realpath):
        rf = os.path.join(realpath, f)
        pf = os.path.join(path, f)
        if os.path.isdir(rf):
            add_translations(rf, pf)
        elif os.path.isfile(rf):
            translation_files.append(pf)
add_translations(
        os.path.join(os.path.dirname(__file__), 'test_i18n', 'l10n'),
        'l10n')


setup(name='test_i18n',
      version='0.1',
      packages=['test_i18n'],
      entry_points={
          'console_scripts': ['say_hello = test_i18n.main:main']},
      description="This is a test package for gettext",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      license='Public Domain',
      package_data={
        'test_i18n': translation_files,
      },
      keywords=['python', 'i18n', 'gettext'],
      classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization'])
