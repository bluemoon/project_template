from setuptools import setup, find_packages
NAME    = ""
VERSION = ""

setup(
    name = NAME,
    version = VERSION,
    packages = find_packages('src'),
    package_dir = {'':'src'},
    zip_safe=False,
    include_package_data=True,
    license='GPL',
    author='Alex Toney',
    author_email='toneyalex@gmail.com',
    test_suite="nose.collector",
    tests_require="nose",
    entry_points = {
    }
)
