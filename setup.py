from setuptools import setup

setup(
    name='ezencoder',
    packages = ['ezencoder'],  # this must be the same as the name above
    version='0.1',
    url='https://github.com/tjpell/easy-encoder',
    download_url='https://github.com/tjpell/easy-encoder/archive/0.1.tar.gz',
    license='MIT',
    py_modules=['src/unknown', 'src/target', 'src/cyclic'],
    author='Taylor Pellerin',
    author_email='tpellerin51@gmail.com',
    install_requires=['numpy', 'pandas', 'sklearn', 'matplotlib'],
    description='Data encoding techniques for use with tabular data such as pandas series and numpy arrays.',
    keywords=['scikit-learn', 'train', 'test', 'validation', 'unknown', 'target', 'cyclic', 'encoding'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers']
)
