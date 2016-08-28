Ansible Role: Pin to Launcher
=============================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-pin-to-launcher.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-pin-to-launcher)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-pin-to-launcher/master/LICENSE)

Role to pin applications to the desktop application launcher.

Requirements
------------

* Ansible >= 1.9

* Ubuntu

    * Wily (15.10)
    * Note: other Ubuntu versions are likely to work but have not been tested.

* A supported launcher

    * [Unity](https://unity.ubuntu.com/)

        * The default desktop installed with Ubuntu.

    * [DockbarX](https://github.com/M7S/dockbarx)

        * An optional install that's compatible with the
          [XUbuntu](http://xubuntu.org/)/[Xfce4](https://www.xfce.org/) desktop.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The desktop application launcher to pin applications to:
# (currently supported: 'unity', dockbarx')
pin_to_launcher: unity

# The favorite applications to pin
pin_to_launcher_favorites: []
```

Favorites are specified as follows:

```yaml
pin_to_launcher_favorites:
  - application: # The file name of a .desktop file in /usr/share/applications/
```

Example Playbooks
-----------------

### Example Unity Playbook

Unity is the default desktop on Ubuntu.

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      pin_to_launcher: unity
      pin_to_launcher_favorites:
        # You'll probably need these apps pinned when using Unity.
        - application: 'ubiquity.desktop' # The application search/menu
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
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on [Ansible Galaxy](https://galaxy.ansible.com/gantsign).

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

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
