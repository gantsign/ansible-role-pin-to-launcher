def test_dockbarx_config(Sudo, Command):
    # Need to -set-home when using sudo for gconftool-2 to work
    output = Command.check_output("sudo --user=test_usr --set-home gconftool-2 --get /apps/dockbarx/launchers")
    assert 'test-app;/usr/share/applications/test-app.desktop' in output
