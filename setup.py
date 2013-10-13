from __future__ import unicode_literals

import os

from setuptools import setup
from setuptools.command.install_lib import install_lib as _install_lib
from distutils.cmd import Command
from distutils.command.build import build as _build

import msgfmt


NAME = 'test_i18n'


class compile_translations(Command):
    description = "compile .po files into .mo files"
    user_options = []

    def initialize_options(self):
        pass
 
    def finalize_options(self):
        pass
 
    def run(self):
        po_dir = os.path.join(os.path.dirname(os.curdir), 'po')
        for path, names, filenames in os.walk(po_dir):
            for f in filenames:
                if f.endswith('.po'):
                    lang = f[:-3]
                    src = os.path.join(path, f)
                    dest_path = os.path.join(
                            'build', 'locale', lang, 'LC_MESSAGES')
                    dest = os.path.join(dest_path, '%s.mo' % NAME)
                    if not os.path.exists(dest_path):
                        os.makedirs(dest_path)
                    if not os.path.exists(dest):
                        print "Compiling %s" % src
                        msgfmt.make(src, dest)
                    else:
                        src_mtime = os.stat(src)[8]
                        dest_mtime = os.stat(dest)[8]
                        if src_mtime > dest_mtime:
                            print 'Compiling %s' % src
                            msgfmt.make(src, dest)


class build(_build):
    sub_commands = [("compile_translations", None)] + _build.sub_commands


class install_lib(_install_lib):
    def run(self):
        self.run_command("compile_translations")
        _install_lib.run(self)


setup(name=NAME,
      version='0.1',
      packages=['test_i18n'],
      description="This is a test package for gettext",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      license='Public Domain',
      package_data = {
        'test_i18n': ['l10n/*.mo'],
      },
      cmdclass={
        'build': build, 'install_lib': install_lib,
        'compile_translations': compile_translations},
      keywords=['python', 'i18n', 'gettext'],
      classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization'])
