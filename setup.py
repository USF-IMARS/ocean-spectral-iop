from setuptools import setup

PACKAGE_NAME = "TODO_put_package_name_here"

setup(
    # The package metadata is specified in setup.cfg but GitHub's downstream dependency graph
    # does not work unless we put the name this here too.
    name=f"{PACKAGE_NAME}",
    use_scm_version={
        "write_to": f"{PACKAGE_NAME}/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    },
)
