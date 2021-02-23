from setuptools import setup, find_namespace_packages

setup(
    name='jonstout-actions-demo',
    version='0.0.1',
    description='Small examply for working with github actions.',
    author='Jonathan Stout',
    author_email='jonstout@globalnoc.iu.edu',
    license='Apache Software License',
    packages=find_namespace_packages(include=['jonstout.*']),
    zip_safe=False
)
