from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dotalytics_api",
    version="0.0.1",
    author="Trevor McCasland",
    description="dota2 analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevormccasland/dotalytics-api",
    packages=["dotalytics_api"],
    entry_points={
            'console_scripts': [
                    'dotalytics-api=dotalytics_api.main:main',
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
