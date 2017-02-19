import os
import warnings

#from distutils.core import setup
from setuptools import setup


with open(os.path.join('bctools', '__init__.py')) as init_:
    for line in init_:
        if '__version__' in line:
            version = line.split('=')[-1].strip().replace('"','')
            break
    else:
        version = 'unknown'
        warnings.warn('Unable to find version, using "%s"' % version)
        input("Continue?")


setup(name='bctools',
      version=version,
      description='BitCurator report and GUI tools',
      author='Kam Woods',
      author_email='kamwoods@gmail.com',
      maintainer = "Kam Woods",
      maintainer_email = "kamwoods@gmail.com",
      url="https://github.com/kamwoods/bitcurator",
      #packages=['bctools', ],
      #package_data={'bctools': ['font/*.ttf', 'font/*.txt']},

      py_modules = ['dfxml', 'fiwalk', 'bc_config', 'bc_genrep_dfxml', 'bc_genrep_feature_xls', 'bc_genrep_premis', 'bc_genrep_text', 'bc_genrep_xls', 'bc_graph', 'bc_pdf', 'bc_regress', 'bc_utils'],

      scripts = ['bc_disk_access_v2.py', 'bc_reports_tab.py', 'generate_report.py'],

      classifiers = ['Development Status :: 2 - Pre-Alpha'
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Programming Language :: Python",
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.0'
                     "Programming Language :: Python :: 3.1",
                     "Programming Language :: Python :: 3.2",
                     "Operating System :: OS Independent",
                     "Topic :: Software Development :: Libraries :: Python Modules"],
      keywords="bitcurator")

