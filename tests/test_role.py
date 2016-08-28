def test_dockbarx_config(Command):
    # Need to -set-home when using sudo for gconftool-2 to work
    output = Command.check_output("sudo --user=test_usr --set-home gconftool-2 --get /apps/dockbarx/launchers")
    assert output == '[test-app;/usr/share/applications/test-app.desktop,test-id;/usr/share/applications/test-app2.desktop]'

def test_unity_config(File):
    config_file = File('/usr/share/glib-2.0/schemas/20_ansible_launcher.gschema.override')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert oct(config_file.mode) == '0644'

    # File.contains uses grep
    expected_pattern = r"\['application://test-app3.desktop', 'application://test-app4.desktop', 'unity://running-apps'\]"
    assert config_file.contains(expected_pattern)
