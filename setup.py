
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Monopoly Calculator (go paperless!)',
    'author': 'Chuck Logan Lim',
    'url': 'https://github.com/chuckoy/monopoly-cash-tracker',
    'download_url': 'Where to download it.',
    'author_email': 'chucklogan.lim@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['monopoly'],
    'scripts': [],
    'name': 'monopoly'
}

setup(**config)
