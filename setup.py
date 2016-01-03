from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = ['neodjango.test', ]

setup(
    name = 'neodjango',
    version = '0.0.8',
    author ='Renan Palmeira',
    author_email ='renanpalmeira1@hotmail.com',
    description ='A Django/Neo4j ORM layer.',
    license = 'GPL',
    url = 'https://neodjango.readthedocs.org/en/latest/',
    keywords = 'django neo4j graph graphdb graphdatabase database rest client driver',
    packages = find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data = True,
    long_description = open('README.md').read(),
    install_requires = [
        'neo4jrestclient>=2.1',
        'Django>=1.6',
        'requests',
        'six',
        'wsgiref',
    ],
    tests_require = [
        'nose>=1.0',
        'requests>=0.4.1',
        'nose-regression>=1.0',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)