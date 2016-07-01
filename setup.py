from setuptools import setup


setup(
    name='pytest-datadir',
    version='0.1.0',
    entry_points={
        'pytest11': ['pytest_datadir = pytest_datadir'],
    },
    py_modules=['pytest_datadir'],
    platforms='any',
    install_requires=[
        'pytest>=2.7',
    ],
    url='https://github.com/menegazzo/pytest-datadir/',
    license='MIT',
    author='Fabio Menegazzo',
    author_email='menegazzo@gmail.com',
    description='Add your test resource near to your tests',
    long_description=open('README.rst').read(),
    keywords="pytest datadir tmpdir",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
    ]
)
