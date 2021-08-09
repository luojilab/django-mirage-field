import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='django-mirage-field',
    version='1.2.2',
    install_requires=[
        "cryptography",
        "tqdm",
    ],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    license='MIT License',
    description='A Django model field that encrypt your data when save to and decrypt when get from database. It keeps data always encrypted in database.',
    long_description_content_type="text/markdown",
    long_description=README,
    url='https://github.com/luojilab/django-mirage-field',
    author='tcitry',
    author_email='tcitry@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
