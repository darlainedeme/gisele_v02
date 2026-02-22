from setuptools import setup, find_packages

setup(
    name='gisele',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'gisele = scripts.run_gisele:main',
        ],
    },
)
