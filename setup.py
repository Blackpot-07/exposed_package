from setuptools import setup, find_packages

setup(
    name='SetupPackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Abdullah',
    author_email='iabdullah416@gmail.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Blackpot-07/exposed_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
