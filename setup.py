#!/usr/bin/env python

from distutils.core import setup

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place. Thanks to James Pearson.
try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = ''

classifiers = [
	"Development Status :: 4 - Beta",
	"Intended Audience :: Developers",
	"Intended Audience :: Information Technology",
	"Intended Audience :: Science/Research",
	"Intended Audience :: System Administrators",
	"Intended Audience :: Telecommunications Industry",
	"License :: OSI Approved :: MIT License",
	"Operating System :: MacOS",
	"Operating System :: MacOS :: MacOS X",
	"Operating System :: POSIX",
	"Operating System :: POSIX :: Linux",
	"Operating System :: Unix",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2 :: Only",
	"Programming Language :: Python :: 2",
	"Programming Language :: Python :: 2.6",
	"Programming Language :: Python :: 2.7",
	"Topic :: Internet",
	"Topic :: Internet :: Log Analysis",
	"Topic :: Internet :: Name Service (DNS)",
	"Topic :: Internet :: Proxy Servers",
	"Topic :: Scientific/Engineering :: Information Analysis",
	"Topic :: System :: Networking",
	"Topic :: System :: Networking :: Monitoring"
]

setup(name='trparse',
        version='0.1.0',
        description='Traceroute parser',
        author='Luis Benitez',
        url='https://github.com/lbenitez000/trparse',
        long_description=long_description,
        license='MIT License',
        py_modules=['trparse'],
        classifiers=classifiers
)