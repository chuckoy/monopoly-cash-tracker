
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Monopoly Calculator (go paperless!)',
    'author': 'Chuck Logan Lim',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'chucklogan.lim@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['monopoly'],
    'scripts': [],
    'name': 'monopoly'
}

setup(**config)

