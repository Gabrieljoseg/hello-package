from setuptools import setup, find_packages

setup(
    name="hello-package",
    version="0.1.0",
    description="Um pacote de exemplo simples",
    author="Seu Nome",
    author_email="gabrieljgomes9@gmail.co",
    url="https://github.com/Gabrieljoseg/hello-package",  # Substitua pelo seu URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)