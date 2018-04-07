from setuptools import setup

setup(
    name='ezencoder',
    version='1.0.1',
    url='https://github.com/tjpell/easy-encoder',
    license='MIT',
    py_modules=['unknown'],
    author='Taylor Pellerin',
    author_email='tjpellerin@dons.usfca.edu',
    install_requires=['numpy','pandas','sklearn', 'matplotlib'],
    description='Data encoding techniques for use with tabular data such as pandas series and numpy arrays.',
    keywords='scikit-learn train test validation unknown target cyclic encoding',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers']
)
