import os
from setuptools import setup, find_packages
import distutils.cmd
import subprocess

import metadata


class SimpleCommand(distutils.cmd.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class DevDocsCommand(SimpleCommand):
    description = "Run development server for documentation"

    def run(self):
        subprocess.check_call(
            ['sphinx-autobuild', '.', '_build/html', '-p', '8001',
             '-z', os.path.join('..', 'emailpal')],
            cwd='docs'
        )


setup(name='django-email-pal',
      cmdclass={
          'devdocs': DevDocsCommand,
      },
      zip_safe=False,
      version=metadata.get_version(),
      description='Easy HTML+plaintext email sending for Django',

      # TODO: Add long_description.

      author='18F',
      author_email='18f-pypi@gsa.gov',
      license='Public Domain',
      url='https://github.com/18F/django-email-pal',
      package_dir={'emailpal': 'emailpal'},
      include_package_data=True,
      packages=find_packages(),
      install_requires=[
          'django>=1.11.1,<2',
      ],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.11',
          'Intended Audience :: Developers',
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'],
      )
