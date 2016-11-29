from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='artifactory-lib',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    # Using Step 7: from SCM https://pypi.python.org/pypi/setuptools_scm
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Python library for interacting with Artifactory API',
    url='https://github.com/MYOB-Technology/artifactory-lib',
    author='Gustavo Hoirisch',
    author_email='gustavo.hoirisch@myob.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='artifactory management library',
    py_modules=["Artifactory"],
    install_requires=['requests']
)
