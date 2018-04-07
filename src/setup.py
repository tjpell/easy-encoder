from setuptools import setup

setup(
    name='rfpimp',
    version='1.0.8',
    url='https://github.com/tjpell/easy-encoder',
    license='MIT',
    py_modules=['unknown'],
    author='Taylor Pellerin',
    author_email='tjpellerin@dons.usfca.edu',
    install_requires=['numpy','pandas','sklearn'],
    description='Permutation and drop-column importance for scikit-learn random forests',
    keywords='scikit-learn train test validation unknown target cyclic encoding',
    classifiers=['License :: ',
                 'Intended Audience :: Developers']
)
