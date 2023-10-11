from distutils.core import setup

setup(
    name="sds",
    py_modules=["sdsflood"],
    entry_points={"console_scripts": ["sdsflood=sds:main"]},
    version="0.2.6",
    description="SDS DDoS attack tool. SDS written in Python.",
    author="Dhananjaya Silva",
    author_email="dhananjaya@sds.com",
    url="https://github.com/sds/sdsflood",
    keywords=["ddos", "http", "sdsflood"],
    license="MIT",
)
