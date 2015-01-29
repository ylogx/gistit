from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['gistit = gistit.gistit:main'],
    },
)

setup(
        name='GistIt',
        description='GistIt helps create github gists quickly',
        version='0.0.2',
        packages=['gistit'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/gistit',
        long_description=open('README.txt').read(),
        **add_keywords
)

