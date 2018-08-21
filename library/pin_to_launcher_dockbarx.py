#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


class LaunchersPreference(object):
    def __init__(self, ansible, launchers_str):
        self.ansible = ansible
        self.launchers_str = launchers_str

    def value_already_set(self):
        return False

    def call(self, call_type, fail_onerr=True):
        changed = False
        out = ''

        config_source = '/etc/gconf/gconf.xml.defaults'

        cmd = ('gconftool-2 '
               '--direct '
               '--config-source xml:readwrite:%s ') % config_source

        key = '/apps/dockbarx/launchers'

        try:
            if call_type == 'get':
                cmd += '--get %s' % key

            elif call_type == 'set':
                cmd += ('--type list --list-type=string '
                        '--set %s "%s"'
                        ) % (key, self.launchers_str)

            rc, out, err = self.ansible.run_command(cmd, use_unsafe_shell=True)

            if len(err) > 0:
                if fail_onerr:
                    self.ansible.fail_json(msg='gconftool-2 failed with '
                                               'error: %s' % (str(err)))
            elif rc != 0:
                if fail_onerr:
                    self.ansible.fail_json(msg='gconftool-2 failed with '
                                               'exit code: %i' % (rc))
            else:
                changed = True

        except OSError as exception:
            self.ansible.fail_json(msg='gconftool-2 failed with exception: '
                                       '%s' % exception)
        return changed, out.rstrip()


def main():
    module = AnsibleModule(
        argument_spec=dict(
            launchers=dict(type='list'),
        ),
        supports_check_mode=True
    )

    launchers = module.params['launchers']

    changed = False
    new_value = ''

    if launchers is None:
        launchers = []

    launchers_str = '[' + ','.join(launchers) + ']'

    launchers_pref = LaunchersPreference(module, launchers_str)

    _, current_value = launchers_pref.call('get', fail_onerr=False)

    if current_value != launchers_str:
        if module.check_mode:
            changed = True
            new_value = launchers_str
        else:
            changed, _ = launchers_pref.call('set')
            _, new_value = launchers_pref.call('get')
    else:
        new_value = current_value

    facts = dict(gconftool2={'changed': changed,
                             'new_value': new_value,
                             'previous_value': current_value,
                             'playbook_value': module.params['launchers']})

    module.exit_json(changed=changed, ansible_facts=facts)


if __name__ == '__main__':
    main()
