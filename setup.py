import io
import re
from glob import glob
from os.path import dirname
from os.path import join
from os.path import basename
from os.path import splitext

from setuptools import find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


classifiers = """
Environment :: Console
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Software Development :: Libraries :: Python Modules
"""

classifier_list = [c for c in classifiers.split("\n") if c]
install_reqs = [str(p.req) for p in parse_requirements(
    join(dirname(__file__), 'requirements.txt'), session='req')]

setup(
    name='youtube-django',
    url='http://youtube-django.rtfd.io',
    license='MIT License',
    description=('YouTube API Data V3 and Google Authentication '
                 'implementation for Django'),
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['pytest-runner', 'setuptools_scm'],
    install_requires=install_reqs,
    tests_require=['tox', 'pytest', 'pytest-cov', 'coverage', 'codecov'],
    long_description=('%s\n%s' % (
        read('README.rst'),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')))
    ),
    author='Ivan Neto',
    author_email='ivan.cr.neto@gmail.com',
    packages=find_packages('.'),
    package_dir={'': '.'},
    zip_safe=False,
    classifiers=classifier_list,
    keywords=[
        'youtube', 'djanto', 'django-youtube', 'youtube-django',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
    extras_require={
    },
)
