Ansible Role: Pin to Launcher
=============================

[![Build Status](https://travis-ci.com/gantsign/ansible-role-pin-to-launcher.svg?branch=master)](https://travis-ci.com/gantsign/ansible-role-pin-to-launcher)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.pin--to--launcher-blue.svg)](https://galaxy.ansible.com/gantsign/pin-to-launcher)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-pin-to-launcher/master/LICENSE)

Role to pin applications to the desktop application launcher.

Requirements
------------

* Ansible >= 2.8

* Ubuntu

    * Xenial (16.04)
    * Note: other Ubuntu versions are likely to work but have not been tested.

* A supported launcher

    * [Gnome](https://www.gnome.org)

        * The default desktop installed with Ubuntu from Bionic (18.04).

    * [Unity](https://en.wikipedia.org/wiki/Unity_(user_interface))

        * The default desktop installed with Ubuntu prior to Bionic (18.04).

    * [DockbarX](https://github.com/M7S/dockbarx)

        * An optional install that's compatible with the
          [XUbuntu](http://xubuntu.org/)/[Xfce4](https://www.xfce.org/) desktop.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The desktop application launcher to pin applications to:
# (currently supported: 'gnome', 'unity', dockbarx')
pin_to_launcher: unity

# The favorite applications to pin
pin_to_launcher_favorites: []
```

Favorites are specified as follows:

```yaml
pin_to_launcher_favorites:
  - application: # The file name of a .desktop file in /usr/share/applications/
    application_id: # DockbarX specific (StartupWMClass or executable file name)
    when_desktop: # If specified, only install if the desktop matches this value
  - unity: # Unity specific (e.g. 'running-apps', 'expo-icon' or 'devices')
```

Example Playbooks
-----------------

### Example Gnome Playbook

Gnome is the default desktop on Ubuntu from Bionic (18.04).

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      pin_to_launcher: gnome
      pin_to_launcher_favorites:
        # You'll probably need these apps pinned when using Gnome.
        - application: 'ubiquity.desktop' # The application search/menu
          when_desktop: gnome
        - application: 'org.gnome.Nautilus.desktop' # The file browser
          when_desktop: gnome
        # Pin the applications of your choice below.
        #
        # Tip: run `gsettings get org.gnome.shell favorite-apps` to
        # see the apps you currently have pinned.
        - application: 'firefox.desktop'
        - application: 'thunderbird.desktop'
        - application: 'rhythmbox.desktop'
        - application: 'libreoffice-writer.desktop'
```

### Example Unity Playbook

Unity was the default desktop on Ubuntu prior to Bionic (18.04).

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      pin_to_launcher: unity
      pin_to_launcher_favorites:
        # You'll probably need these apps pinned when using Unity.
        - application: 'ubiquity.desktop' # The application search/menu
          when_desktop: unity
        - application: 'org.gnome.Nautilus.desktop' # The file browser
        # The following two apps are less frequently used so you may want to put
        # them below your other apps.
        - application: 'ubuntu-software-center.desktop' # Ubuntu software center
        - application: 'unity-control-center.desktop' # System settings

        # Pin the applications of your choice below.
        #
        # Tip: run `gsettings get com.canonical.Unity.Launcher favorites` to
        # see the apps you currently have pinned.
        - application: google-chrome.desktop

        # The 'unity' favorites are not apps as such, but are placeholders in
        # the Ubuntu launcher.
        #
        # You can reorder the items below, but be don't omit them unless you
        # know what you're doing.
        #
        # These can be omitted if you're using DockbarX, but they'll be ignored
        # anyway.
        - unity: running-apps
        - unity: expo-icon
        - unity: devices
```

### Example DockbarX Playbook

DockbarX is a popular dockbar that has integration with the Xfce4 desktop. To
use this you have to [install DockbarX first](https://github.com/M7S/dockbarx).

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      pin_to_launcher: dockbarx
      pin_to_launcher_favorites:
        # There are no applications pinned by default with DockbarX, so add
        # whatever apps you want here.
        #
        # Tip: run `gconftool-2 --get /apps/dockbarx/launchers` to see what apps
        # you currently have pinned.
        - application: exo-terminal-emulator.desktop
        - application: Thunar-folder-handler.desktop
          # If your application isn't grouped with its launcher it may help to
          # specify the `application_id`; this is either the `StartupWMClass`
          # (if one is present in the `.desktop` file), or the file name of the
          # application executable.
          application_id: Thunar
          when_desktop: dockbarx
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
