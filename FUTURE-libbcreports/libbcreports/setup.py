import os
import warnings

# from distutils.core import setup
from setuptools import setup


with open(os.path.join('libbcreports', '__init__.py')) as init_:
    for line in init_:
        if '__version__' in line:
            version = line.split('=')[-1].strip().replace('"', '')
            break
    else:
        version = 'unknown'
        warnings.warn('Unable to find version, using "%s"' % version)
        input("Continue?")


setup(name='libbcreports',
      version=version,
      description='BitCurator Reporting Tools',
      author='BitCurator',
      author_email='bitcurator@gmail.com',
      maintainer="BitCurator",
      maintainer_email="bitcurator@gmail.com",
      url="https://github.com/bitcurator/bitcurator-distro-tools",
      install_requires=[
        "schema", "docopt"  # , "PyQt5"
      ],
      packages=['libbcreports', 'GUI'],
      # package_data={'bctools': ['font/*.ttf', 'font/*.txt']},

      py_modules=['dfxml', 'fiwalk'],

      entry_points={
        'console_scripts': [
          'reports-gui = GUI.ReportsGUI:main',
        ],
      },

      classifiers=['Development Status :: 2 - Pre-Alpha'
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.7",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development :: Libraries :: Python Modules"],
      keywords="bitcurator")
