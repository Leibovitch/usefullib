import setuptools

setuptools.setup(
    name='usefullib',
    author='Noy Leibovitch',
    version='0.0.1',
    description='extension to common python ',
    keywords='',
    url='https://github.com/Leibovitch/usefullib.git',
    py_modules=['pandas', 'math'],
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
  ],
)
