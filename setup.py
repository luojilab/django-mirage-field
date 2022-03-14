import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='django-mirage-field',
    version='1.4.0',
    install_requires=[
        "cryptography",
        "tqdm",
    ],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    license='MIT License',
    description='A Django model fields collection that encrypt your data when save to and decrypt when get from database. It keeps data always encrypted in database.',
    long_description_content_type="text/markdown",
    long_description=README,
    url='https://github.com/luojilab/django-mirage-field',
    author='tcitry',
    author_email='tcitry@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
