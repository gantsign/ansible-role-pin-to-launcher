def test_dockbarx_config(Command):
    # Need to -set-home when using sudo for gconftool-2 to work
    output = Command.check_output("sudo --user=test_usr --set-home gconftool-2 --get /apps/dockbarx/launchers")
    assert output == '[test-app;/usr/share/applications/test-app.desktop,test-app2;/usr/share/applications/test-app2.desktop]'
