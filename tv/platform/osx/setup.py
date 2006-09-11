import os
import sys
import string
import py2app
import shutil
import plistlib

from glob import glob
from distutils.core import setup
from Pyrex.Distutils import build_ext
from distutils.extension import Extension

# Find the top of the source tree and set search path
# GCC3.3 on OS X 10.3.9 doesn't like ".."'s in the path so we normalize it

root = os.path.dirname(os.path.abspath(sys.argv[0]))
root = os.path.join(root, '..', '..')
root = os.path.normpath(root)
sys.path[0:0]=['%s/portable' % root]

# Only now may we import things from our own tree

import template_compiler
template_compiler.compileAllTemplates(root)

# Look for the Boost library in various common places.
# - we assume that both the library and the include files are installed in the
#   same directory sub-hierarchy.
# - we look for library and include directory in:
#   - the standard '/usr/local' tree
#   - Darwinports' standard '/opt/local' tree
#   - Fink's standard '/sw' tree

boostLib = None
boostIncludeDir = None
boostSearchDirs = ('/usr/local', '/opt/local', '/sw')

for rootDir in boostSearchDirs:
    libItems = glob(os.path.join(rootDir, 'lib/libboost_python-1_3*.a'))
    incItems = glob(os.path.join(rootDir, 'include/boost-1_3*/'))
    if len(libItems) == 1 and len(incItems) == 1:
        boostLib = libItems[0]
        boostIncludeDir = incItems[0]

if boostLib is None or boostIncludeDir is None:
    print 'Boost library could not be found, interrupting build.'
    sys.exit(1)
else:
    print 'Boost library found (%s)' % boostLib

# Get subversion revision information.

import util
revision = util.queryRevision(root)
if revision is None:
    revisionURL = 'unknown'
    revisionNum = '0000'
    revision = 'unknown'
else:
    revisionURL, revisionNum = revision
    revision = '%s - %s' % revision

# Inject the revision number into app.config.template to get app.config.

appConfigTemplatePath = os.path.join(root, 'resources', 'app.config.template')
appConfigPath = '/tmp/democracy.app.config'
s = open(appConfigTemplatePath, "rt").read()
s = string.Template(s).safe_substitute(APP_REVISION = revision, 
                                       APP_REVISION_URL = revisionURL, 
                                       APP_REVISION_NUM = revisionNum, 
                                       APP_PLATFORM = 'osx')
f = open(appConfigPath, 'wt')
f.write(s)
f.close()

# Update the Info property list.

def updatePListEntry(plist, key, conf):
    entry = plist[key]
    plist[key] = string.Template(entry).safe_substitute(conf)

conf = util.readSimpleConfigFile(appConfigPath)
infoPlist = plistlib.readPlist(u'Info.plist')

updatePListEntry(infoPlist, u'CFBundleGetInfoString', conf)
updatePListEntry(infoPlist, u'CFBundleIdentifier', conf)
updatePListEntry(infoPlist, u'CFBundleName', conf)
updatePListEntry(infoPlist, u'CFBundleShortVersionString', conf)
updatePListEntry(infoPlist, u'CFBundleVersion', conf)
updatePListEntry(infoPlist, u'NSHumanReadableCopyright', conf)

print "Building Democracy Player v%s (%s)" % (conf['appVersion'], conf['appRevision'])

# Get a list of additional resource files to include

resourceFiles = ['Resources/%s' % x for x in os.listdir('Resources')]

# And launch the setup process...

py2app_options = dict(
    plist = infoPlist,
    iconfile = '%s/platform/osx/Democracy.icns' % root,
    packages = ['dl_daemon']
)

setup(
    app = ['Democracy.py'],
    data_files = resourceFiles,
    options = dict(py2app = py2app_options),
    ext_modules = [
        Extension("idletime",["%s/platform/osx/idletime.c" % root]),
        Extension("database",["%s/portable/database.pyx" % root]),
        Extension("sorts",["%s/portable/sorts.pyx" % root]),
        Extension("fasttypes",["%s/portable/fasttypes.cpp" % root],
                  extra_objects=[boostLib],
                  include_dirs=[boostIncludeDir])
        ],
    cmdclass = dict(build_ext = build_ext)
)

# Setup some variables we'll need

bundleRoot = 'Democracy.app/Contents'
execRoot = os.path.join(bundleRoot, 'MacOS')
rsrcRoot = os.path.join(bundleRoot, 'Resources')
prsrcRoot = os.path.join(rsrcRoot, 'resources')

# Create a hard link to the main executable with a different name for the 
# downloader. This is to avoid having 'Democracy' shown twice in the Activity 
# Monitor since the downloader is basically Democracy itself, relaunched with a 
# specific command line parameter.

print "Creating Downloader hard link."

srcPath = os.path.join(execRoot, 'Democracy')
linkPath = os.path.join(execRoot, 'Downloader')

if os.path.exists(linkPath):
    os.remove(linkPath)
os.link(srcPath, linkPath)

# Copy our own portable resources, install the app.config file and remove 
# useless data

print "Copying portable resources to application bundle"

if os.path.exists(prsrcRoot):
    shutil.rmtree(prsrcRoot)
os.mkdir(prsrcRoot)

excludedRsrc = ['app.config.template', 'locale', 'testdata']
for resource in glob(os.path.join(root, 'resources', '*')):
    rsrcName = os.path.basename(resource)
    if rsrcName not in excludedRsrc:
        print "    %s" % rsrcName
        if os.path.isdir(resource):
            shutil.copytree(resource, os.path.join(prsrcRoot, rsrcName))
        else:
            shutil.copy(resource, prsrcRoot)

# Install the final app.config file

print "Copying config file to application bundle"
shutil.move(appConfigPath, os.path.join(prsrcRoot, 'app.config'))

# Copy the gettext MO files in a 'locale' folder inside the application bundle 
# resources folder. Doing this manually at this stage instead of automatically 
# through the py2app options allows to avoid having an intermediate unversioned 
# 'locale' folder.

print "Copying gettext MO files to application bundle."

localeDir = os.path.join (root, 'resources', 'locale')
shutil.rmtree(os.path.join(rsrcRoot, 'locale'), True);

for source in glob(os.path.join(localeDir, '*.mo')):
    lang = os.path.basename(source)[:-3]
    dest = 'Democracy.app/Contents/Resources/locale/%s/LC_MESSAGES/democracyplayer.mo' % lang
    os.makedirs(os.path.dirname(dest))
    shutil.copy2(source, dest)

# As of Democracy 0.9.0, we want to be able to play FLV files so we bundle our
# own copy of VLC (without the DVD CSS library) and use it explicitely from the 
# frontend code.

embeddedVLCPath = 'Democracy.app/Contents/'
if os.path.exists(os.path.join(embeddedVLCPath, 'vlc')):
    print 'Current application bundle already has an embedded VLC, skipping embedding phase.'
else:
    vlcArchivePath = '../../../dtv-binary-kit/vlc/mac/vlc-0.8.5.tar.gz'
    if not os.path.exists(vlcArchivePath):
        print "Can't find VLC in Democracy binary kit, skipping embedding phase."
    else:
        import tarfile
        print "Copying VLC to application bundle."
        tar = tarfile.open(vlcArchivePath, 'r:gz')
        for tarInfo in tar:
            if tarInfo.name.endswith('vlc_libdvdcss.dylib'):
                print "Skipping DVD CSS library."
            else:
                print "Unpacking %s" % tarInfo.name
                tar.extract(tarInfo, embeddedVLCPath)

# And we're done...

print "------------------------------------------------"
