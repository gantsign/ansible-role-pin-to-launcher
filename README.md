Ansible Role: Pin to Launcher
=============================

Role to pin applications to the desktop application launcher.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Users with applications to pin to the desktop application launcher
users: []
```

Users are specified as follows:

```yaml
- username: # Unix username
  pin_to_launcher:
    launcher: # Desktop application launcher to pin applications to (currently supported: 'dockbarx')
    favorites:
      - application: # the file name of the .desktop file in /usr/share/applications/
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      users:
        - username: vagrant
          pin_to_launcher:
            launcher: dockbarx
            favorites:
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
