from os.path import abspath, dirname, join
from setuptools import find_packages, setup


ENTRY_POINTS = """
[crosscompute.types]
geotable = crosscompute_geotable:GeoTableType
"""
FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'CHANGES.rst', 'README.rst'])
setup(
    name='crosscompute-geotable',
    version='0.7.7.4',
    description='GeoTable data type plugin for CrossCompute',
    long_description=DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: OSI Approved :: MIT License',
    ],
    author='CrossCompute Inc',
    author_email='support@crosscompute.com',
    url='https://crosscompute.com/docs',
    keywords='web pyramid pylons crosscompute',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    install_requires=[
        'invisibleroads-macros>=0.9.5.1',
        'invisibleroads-uploads>=0.4.2.3',
        'crosscompute>=0.7.7',
        'crosscompute-table>=0.7.7',
        # 'geotable',
        'numpy',
        'pandas',
        'six',
    ],
    entry_points=ENTRY_POINTS)
