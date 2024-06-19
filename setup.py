from setuptools import setup, find_packages
from uac_api import __version__
version = __version__

def main():
    with open('README.md', 'r') as readme:
        long_description = readme.read()
    setup(
        name='uac-api',
        version=version,
        author_email="huseyim@gmail.com",
        license="CC BY-NC 4.0",
        url="https://github.com/gomleksiz/uac-api",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            "requests",
        ],
        extras_require={
            'networkx':  ['networkx'],
        },
        author='Stonebranch',
        description='A Python wrapper for the Stonebranch UAC API',
        python_requires='>=3.7',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        long_description=long_description,
        long_description_content_type="text/markdown"
    )


if __name__ == '__main__':
    main()
