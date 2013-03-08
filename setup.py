import os
from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

setup(
    name="django-logs",
    version='0.1',
    url='http://github.com/relekang/django-logs',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    description='Simple reusable django app for logging events within a django project',
    packages=find_packages(exclude='tests'),
    tests_require=[
        'django>=1.3',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
)
