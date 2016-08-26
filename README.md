Ansible Role: Pin to Launcher
=============================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-pin-to-launcher.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-pin-to-launcher)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.pin--to--launcher-blue.svg)](https://galaxy.ansible.com/gantsign/pin-to-launcher)

Role to add items to the desktop application launcher.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Users with items to add to the desktop application launcher
users: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.pin-to-launcher
      users:
        - username: vagrant
          pin_to_launcher_items:
            - 'exo-terminal-emulator;/usr/share/applications/exo-terminal-emulator.desktop'
            - 'thunar;/usr/share/applications/Thunar-folder-handler.desktop'
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
