from setuptools import setup, find_packages

setup(
    name='tosend',
    version='0.1.0',
    author='Kosi',
    author_email='kiu2102@columbia.edu',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'datajoint',
        'numpy',
        'matplotlib',
        'pickle5; python_version < "3.8"'
    ],
    description='A package for managing and visualizing neuroscience data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
