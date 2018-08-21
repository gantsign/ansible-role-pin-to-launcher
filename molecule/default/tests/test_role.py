import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dockbarx_config(host):
    # Need to -set-home when using sudo for gconftool-2 to work
    output = host.check_output("sudo %s --set-home gconftool-2 --get %s",
                               "--user=test_usr",
                               "/apps/dockbarx/launchers")
    launchers = ['test-app;/usr/share/applications/test-app.desktop',
                 'test-id;/usr/share/applications/test-app2.desktop']
    assert output == '[' + ','.join(launchers) + ']'


def test_unity_config(host):
    path = '/usr/share/glib-2.0/schemas/20_ansible_launcher.gschema.override'
    config_file = host.file(path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == 0o644

    # File.contains uses grep
    favorites = ['application://test-app3.desktop',
                 'application://test-app4.desktop',
                 'unity://running-apps']
    expected_pattern = r"\['" + "', '".join(favorites) + r"'\]"
    assert config_file.contains(expected_pattern)
