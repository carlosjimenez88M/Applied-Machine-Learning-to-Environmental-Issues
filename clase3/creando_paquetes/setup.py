# setup.py
from setuptools import setup, find_packages

setup(
    name='poisson_distribution',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    author='Gente maravillosa de la nacional',
    author_email='tu_email@example.com',
    description='Un paquete para trabajar con distribuciones de Poisson',
    
    url='https://github.com/tu_usuario/poisson_distribution',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
