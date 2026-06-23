"""
Setup file for Random User Generator
"""

from setuptools import setup, find_packages

setup(
    name="random-user-generator",
    version="1.0.0",
    description="A random user profile generator desktop application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/random-user-generator",
    packages=find_packages(),
    install_requires=[
        "requests==2.31.0",
        "Pillow==10.1.0",
    ],
    entry_points={
        "console_scripts": [
            "random-user=random_user_generator:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
