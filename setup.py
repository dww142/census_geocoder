from setuptools import setup

setup(
   name='census_geocoder',
   version='1.0',
   description='Python wrapper to *some* of the functionality of the US Census Bureau Geocoding web service',
   author='Dan Welsh',
   author_email='danielwelsh@gmail.com',
   packages=['census_geocoder'],  #same as name
   install_requires=['requests'], #external packages as dependencies
)
