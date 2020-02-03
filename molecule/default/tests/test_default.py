import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_docker_version(host):
    cmd = host.run('docker --version')
    assert cmd.rc == 0


def test_docker_compose_version(host):
    cmd = host.run('docker-compose --version')
    assert cmd.rc == 0
