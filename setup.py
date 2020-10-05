import setuptools

setuptools.setup(
    name="xprocess_test",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="cquick01",
    author_email="cquick@assurtech.com",
    description="test xprocess in docker",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[],
    python_requires=">=3.6",
)

