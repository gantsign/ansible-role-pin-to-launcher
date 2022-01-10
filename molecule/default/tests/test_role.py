def test_gnome_config(host):
    path = ('/usr/share/glib-2.0/schemas/'
            '20_ansible_favorite_apps.gschema.override')
    config_file = host.file(path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == 0o644

    # File.contains uses grep
    favorites = ['test-app3.desktop', 'test-app6.desktop']
    expected_pattern = r"\[ '" + "', '".join(favorites) + r"' \]"
    assert config_file.contains(expected_pattern)
