from setuptools import setup

def readme():
    with open('README.txt') as f:
        README = f.read()
    return README

setup(
    name="TOPSIS-Yashpal-101803611",
    version="1.0.0",
    description="A Python package implementing TOPSIS technique.",
    long_description="dcbudhdichegfudhwidhwihdiuhdg7ug3wfdue",
    long_description_content_type="text/markdown",
    author="Yashpal",
    author_email="yyashpal_be18@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["packageTopsis"],
    include_package_data=True,
    install_requires=['numpy',
                      'pandas'
     ],
     entry_points={
        "console_scripts": [
            "topsis=packageTopsis:main",
        ]
     },
)
