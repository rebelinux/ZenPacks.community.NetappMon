################################
# These variables are overwritten by Zenoss when the ZenPack is exported
# or saved.  Do not modify them directly here.
# NB: PACKAGES is deprecated
<<<<<<< HEAD
NAME = "ZenPacks.community.NortelMon"
VERSION = "1.4.8.3"
AUTHOR = "Jonathan Colon"
LICENSE = ""
NAMESPACE_PACKAGES = ['ZenPacks', 'ZenPacks.community']
PACKAGES = ['ZenPacks', 'ZenPacks.community', 'ZenPacks.community.NortelMon']
INSTALL_REQUIRES = []
COMPAT_ZENOSS_VERS = ">=3.0"
=======
NAME = "ZenPacks.community.NetappMon"
VERSION = "1.0.0"
AUTHOR = ""
LICENSE = "GPLv2+"
NAMESPACE_PACKAGES = ['ZenPacks', 'ZenPacks.community']
PACKAGES = ['ZenPacks', 'ZenPacks.community', 'ZenPacks.community.NetappMon']
INSTALL_REQUIRES = []
COMPAT_ZENOSS_VERS = ">=4.2"
>>>>>>> 64785c68657f8df9bb2f417ef3b11392116a0f22
PREV_ZENPACK_NAME = ""
# STOP_REPLACEMENTS
################################
# Zenoss will not overwrite any changes you make below here.

<<<<<<< HEAD
from setuptools import setup, find_packages

=======
import os
from subprocess import Popen, PIPE
from setuptools import setup, find_packages

# Run "make build" if a GNUmakefile is present.
if os.path.isfile('GNUmakefile'):
    print 'GNUmakefile found. Running "make build" ..'
    p = Popen('make build', stdout=PIPE, stderr=PIPE, shell=True)
    print p.communicate()[0]
    if p.returncode != 0:
        raise Exception('"make build" exited with an error: %s' % p.returncode)

>>>>>>> 64785c68657f8df9bb2f417ef3b11392116a0f22
setup(
    # This ZenPack metadata should usually be edited with the Zenoss
    # ZenPack edit page.  Whenever the edit page is submitted it will
    # overwrite the values below (the ones it knows about) with new values.
<<<<<<< HEAD
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    license = LICENSE,
    
    # This is the version spec which indicates what versions of Zenoss
    # this ZenPack is compatible with
    compatZenossVers = COMPAT_ZENOSS_VERS,
    
    # previousZenPackName is a facility for telling Zenoss that the name
    # of this ZenPack has changed.  If no ZenPack with the current name is
    # installed then a zenpack of this name if installed will be upgraded.
    prevZenPackName = PREV_ZENPACK_NAME, 
    
    # Indicate to setuptools which namespace packages the zenpack
    # participates in
    namespace_packages = NAMESPACE_PACKAGES,
    
    # Tell setuptools what packages this zenpack provides.
    packages = find_packages(),
    
    # Tell setuptools to figure out for itself which files to include
    # in the binary egg when it is built.
    include_package_data = True,
    
=======
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    license=LICENSE,

    # This is the version spec which indicates what versions of Zenoss
    # this ZenPack is compatible with
    compatZenossVers=COMPAT_ZENOSS_VERS,

    # previousZenPackName is a facility for telling Zenoss that the name
    # of this ZenPack has changed.  If no ZenPack with the current name is
    # installed then a zenpack of this name if installed will be upgraded.
    prevZenPackName=PREV_ZENPACK_NAME,

    # Indicate to setuptools which namespace packages the zenpack
    # participates in
    namespace_packages=NAMESPACE_PACKAGES,

    # Tell setuptools what packages this zenpack provides.
    packages=find_packages(),

    # Tell setuptools to figure out for itself which files to include
    # in the binary egg when it is built.
    include_package_data=True,

>>>>>>> 64785c68657f8df9bb2f417ef3b11392116a0f22
    # The MANIFEST.in file is the recommended way of including additional files
    # in your ZenPack. package_data is another.
    #package_data = {}

    # Indicate dependencies on other python modules or ZenPacks.  This line
    # is modified by zenoss when the ZenPack edit page is submitted.  Zenoss
    # tries to put add/delete the names it manages at the beginning of this
    # list, so any manual additions should be added to the end.  Things will
    # go poorly if this line is broken into multiple lines or modified to
    # dramatically.
<<<<<<< HEAD
    install_requires = INSTALL_REQUIRES,

    # Every ZenPack egg must define exactly one zenoss.zenpacks entry point
    # of this form.
    entry_points = {
=======
    install_requires=INSTALL_REQUIRES,

    # Every ZenPack egg must define exactly one zenoss.zenpacks entry point
    # of this form.
    entry_points={
>>>>>>> 64785c68657f8df9bb2f417ef3b11392116a0f22
        'zenoss.zenpacks': '%s = %s' % (NAME, NAME),
    },

    # All ZenPack eggs must be installed in unzipped form.
<<<<<<< HEAD
    zip_safe = False,    
=======
    zip_safe=False,
>>>>>>> 64785c68657f8df9bb2f417ef3b11392116a0f22
)
