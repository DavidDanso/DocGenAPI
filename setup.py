from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Define setup parameters
setup(
    name='document-generator',  # Name of the project
    version='1.0.0',  # Version number
    description='A FastAPI document generation project',  # Short description
    author='Your Name',  # Author name
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=requirements,  # Dependencies required for the project
    entry_points={  # Define entry points for console scripts
        'console_scripts': [
            'start_server = uvicorn main:app --reload',  # Command to start the server using Uvicorn
        ],
    },
)
