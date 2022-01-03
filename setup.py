import setuptools

setuptools.setup(
    name="baidu_sem_sdk",
    url="https://github.com/digital-value-apps/baidu_sem_sdk/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["requests"],
)
