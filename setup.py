from setuptools import setup, find_packages

setup(
    name="grid_maker",
    version="0.1.0",
    description="A utility for creating grid layouts.",
    author="Keenan",
    author_email="jonathan@wantsmore.coffee",
    url="https://github.com/keenan-v1/grid-maker",
    packages=find_packages(),
    install_requires=[
        "pillow==11.0.0"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gridmaker=gridmaker:main",
        ],
    },    
)
