import testinfra

def test_hosts_file(host):
    # проверим, что /etc/hosts существует
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"

def test_python_installed(host):
    python = host.exists("python3")
    pip = host.exists("pip3")
    sudo = host.exists("sudo")
    assert python
    assert pip
    assert sudo
