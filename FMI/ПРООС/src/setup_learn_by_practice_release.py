import os, sys
import msilib
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'D:/Python 3.6.1/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'D:/Python 3.6.1/tcl/tk8.6'

sys.argv.append('bdist_msi')

UPGRADE_CODE = '{6346f532-207e-451e-8469-a515174fa661}'
MAIN_SCRIPT = 'E:/Programming/Python/Watch for dummies/main.py'
ICON = 'E:/Programming/Python/Watch for dummies/images/search.ico'
VERSION = '0.1.1'
PRODUCT_NAME = 'Product searcher'
COMPANY_NAME = 'Stanin CO.'
AUTHOR_NAME = 'Zdravko Stanin'
AUTHOR_CONTACT_MAIL = 'zdravko.stanin@abv.bg'
INITIAL_TARGET_FOLDER = r'[ProgramFilesFolder]\{}'.format(PRODUCT_NAME)
DESKTOP_FOLDER = 'DesktopFolder'
START_MENU_KEY = 'StartMenuShortcut'
START_MENU_FOLDER = 'StartMenuFolder'


version = VERSION

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_files = ['D:/Python 3.6.1/DLLs/tcl86t.dll',
                 'D:/Python 3.6.1/DLLs/tk86t.dll',
                 'E:/Programming/Python/Watch for dummies/queries.xml']

build_exe_options = {
    'include_files': include_files,
    'include_msvcr': True   # skip error msvcr100.dll missing
}

icon_table = [
    (
        PRODUCT_NAME + ' Icon',                     # Name
        msilib.Binary(ICON),                        # Data - .ico, .dll or .exe
     )
]

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    (
        START_MENU_KEY,           # Shortcut
        START_MENU_FOLDER,        # Directory_
        PRODUCT_NAME,             # Name
        'TARGETDIR',              # Component_
        '[TARGETDIR]' + PRODUCT_NAME + '.exe',# Target
        None,                     # Arguments
        None,                     # Description
        None,                     # Hotkey
        None,                     # Icon
        None,                     # IconIndex
        None,                     # ShowCmd
        'TARGETDIR'               # WkDir
     )
]

# Now create the table dictionary
msi_data = {
    'Shortcut': shortcut_table,
    'Icon': icon_table
}

bdist_msi_options = {
    'data': msi_data,
    'upgrade_code': UPGRADE_CODE,
    'add_to_path': True,
    'initial_target_dir': INITIAL_TARGET_FOLDER
    #'target_name': INSTALL_NAME - Uncomment in case the installer should be named differently
}

executable = Executable(
    script=MAIN_SCRIPT,  # the name of your main python script goes here
    initScript=None,
    base=base,  # if creating a GUI instead of a console app, type "Win32GUI"
    targetName=PRODUCT_NAME + '.exe',#'Subtitles Distributor.exe',  # this is the name of the executable file
    icon=ICON,  # if you want to use an icon file, specify the file name here
    shortcutName=PRODUCT_NAME,#'Subtitles Distributor',
    shortcutDir=DESKTOP_FOLDER
)

executables = [
    executable
]

setup(
    name=PRODUCT_NAME,
    version=version,
    author=AUTHOR_NAME,
    author_email=AUTHOR_CONTACT_MAIL,
    description=PRODUCT_NAME,
    options={'build_exe': build_exe_options,
             'bdist_msi': bdist_msi_options},
    executables=executables
)
