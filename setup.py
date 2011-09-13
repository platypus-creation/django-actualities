from setuptools import setup, find_packages

setup(
    name = "django-actualities",
    version = "0.2.2",
    description = """
    A django blog app
    """,
    author = "Platypus Creation",
    author_email = "contact@platypus-creation.com",
    url = "https://github.com/platypus-creation/django-actualities",
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django-taggit==0.9.3',
    ],
)
