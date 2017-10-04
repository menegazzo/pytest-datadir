from setuptools import setup


setup(
    name='pytest-stash',
    version='0.1.0',
    entry_points={
        'pytest11': ['pytest_stash = pytest_stash'],
    },
    py_modules=['pytest_stash'],
    platforms='any',
    install_requires=[
        'pytest>=2.7',
    ],
    url='https://github.com/menegazzo/pytest-stash/',
    license='MIT',
    author='Fabio Menegazzo',
    author_email='menegazzo@gmail.com',
    description='Add your test resource near to your tests',
    long_description=open('README.rst').read(),
    keywords="pytest datadir stash tmpdir",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
    ]
)
