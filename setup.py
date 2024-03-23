from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='document-generator',
    version='1.0.0',
    description='A FastAPI document generation project',
    author='Your Name',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'start_server = uvicorn main:app --reload',
        ],
    },
)
