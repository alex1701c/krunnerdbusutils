from setuptools import setup, find_packages

setup(
    name='krunnerdbusutils',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'dbus-python',
    ],
    tests_require=[
        'pytest',
    ],
    author='Alexander Lohnau',
    author_email='alex1701c.dev@gmx.net',
    description='A utility library for interacting with the KRunner API via D-Bus',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alex1701c/krunnerdbusutils',
    classifiers=[],
    python_requires='>=3.10',
)
