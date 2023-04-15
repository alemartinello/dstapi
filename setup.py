import setuptools

# Read requirements.txt file content
with open('requirements.txt') as f:
    requirements = f.read().splitlines() 

setuptools.setup(
    name='dstapi',
    version='0.1',
    packages=setuptools.find_packages(),
    install_requires=requirements
)
