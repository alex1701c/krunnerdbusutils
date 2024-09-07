from setuptools import setup, find_packages

setup(
    name='krunnerdbusutils',
    version='0.1.0',
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'dbus-python',  # Ensure that dbus-python is installed
    ],
    tests_require=[
        'pytest',  # Specify your testing framework
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A utility library for interacting with the KRunner API via D-Bus.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alex1701c/krunnerdbusutils',
    classifiers=[],
    python_requires='>=3.10',
)
