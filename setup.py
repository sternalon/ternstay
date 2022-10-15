from setuptools import setup, find_packages


requires = [
    "python-dotenv",
]


dev_require = [
    "black",
    "flake8",
    "isort",
    "pytest",
    #"pytest-cov",
]

setup(
    name="ternstay",
    version="1.0.0",
    description="Builds the TernStay recon backend",
    classifiers=["Programming Language :: Python"],
    author="Alon Stern",
    author_email="alon@ternstay.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"dev": dev_require},
    install_requires=requires,
)

