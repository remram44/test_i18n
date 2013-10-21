import os
from setuptools import setup
from distutils.cmd import Command
from distutils.command.build import build as _build

import msgfmt


NAME = 'test_i18n'


class compile_translations(Command):
    description = "compile .po files into .mo files"
    user_options = [
        ('build-lib', None, "lib build folder")]

    def initialize_options(self):
        self.build_lib = None

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        po_dir = os.path.join(os.path.dirname(__file__), 'po')
        print "Compiling po files..."
        for path, names, filenames in os.walk(po_dir):
            for f in filenames:
                if f.endswith('.po'):
                    lang = f[:-3]
                    src = os.path.join(path, f)
                    dest_path = os.path.join(
                            self.build_lib,
                            NAME, 'l10n', lang, 'LC_MESSAGES')
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


setup(name=NAME,
      version='0.1',
      packages=['test_i18n'],
      entry_points={
          'console_scripts': ['say_hello = test_i18n.main:main']},
      description="This is a test package for gettext",
      author="Remi Rampin",
      author_email='remirampin@gmail.com',
      license='Public Domain',
      package_data={
        'test_i18n': ['l10n/*/LC_MESSAGES/*.mo'],
      },
      cmdclass={
        'build': build,
        'compile_translations': compile_translations},
      keywords=['python', 'i18n', 'gettext'],
      classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization'])
