project(
    'example',
    version : '1.0',
    license: ['GplV3']
)

prefix = get_option('prefix')
appdir = prefix / 'share'

glibdir = get_option('prefix')/'share/glib-2.0/schemas/'
icondir = get_option('prefix')/'share/icons/hicolor/scalable/apps'
desktopdir = get_option('prefix')/'share/applications'

install_data('data/org.example.application.svg', install_dir : icondir)
install_data('data/org.example.application.desktop', install_dir : desktopdir)
install_data('data/org.example.application.gschema.xml', install_dir : glibdir)

install_subdir('example/', install_dir: appdir)
install_data('example.py', install_dir : bindir, rename: 'example')
