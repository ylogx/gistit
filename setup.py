from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['gistit = gistit.main:main'],
    },
)

fhan = open('requirements.txt', 'rU')
requires = [ line.strip() for line in fhan.readlines() ]
#print('We require: ', requires)

setup(
        name='GistIt',
        description='GistIt helps create github gists quickly',
        version='0.0.1',
        packages=['gistit'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/gistit',
        long_description=open('README.txt').read(),
        install_requires=requires,
        **add_keywords
)

