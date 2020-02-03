# Ansible Role: Docker

An Ansible Role that installs [Docker](https://www.docker.com) on Linux.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# Edition can be one of: 'ce' (Community Edition) or 'ee' (Enterprise Edition).
docker_edition: ce
docker_package: "docker-{{ docker_edition }}"
docker_package_state: present
```

The `docker_edition` should be either `ce` (Community Edition) or `ee` (Enterprise Edition). You can also specify a specific version of Docker to install using the distribution-specific format: Red Hat/CentOS: `docker-{{ docker_edition }}-<VERSION>`; Debian/Ubuntu: `docker-{{ docker_edition }}=<VERSION>`.

You can control whether the package is installed, uninstalled, or at the latest version by setting `docker_package_state` to `present`, `absent`, or `latest`, respectively. Note that the Docker daemon will be automatically restarted if the Docker package is updated. This is a side effect of flushing all handlers (running any of the handlers that have been notified by this and any other role up to this point in the play).

```yaml
docker_service_state: started
docker_service_enabled: true
docker_restart_handler_state: restarted
```
These Variables control the state of the `docker` service, and whether it should start on boot.

```yaml
docker_install_compose: true
docker_compose_version: "1.22.0"
docker_compose_path: /usr/local/bin/docker-compose
```
Docker Compose installation options.

```yaml
docker_apt_release_channel: stable
docker_apt_arch: amd64
docker_apt_repository: "deb [arch={{ docker_apt_arch }}] https://download.docker.com/linux/{{ ansible_distribution|lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
```
(Used only for Debian/Ubuntu.) You can switch the channel to `edge` if you want to use the Edge release.

```yaml
docker_yum_repo_url: https://download.docker.com/linux/centos/docker-{{ docker_edition }}.repo
docker_yum_repo_enable_edge: '0'
docker_yum_repo_enable_test: '0'
```
(Used only for RedHat/CentOS.) You can enable the Edge or Test repo by setting the respective vars to `1`.

```yaml
docker_users:
  - user1
  - user2
```
A list of system users to be added to the `docker` group (so they can use Docker on the server).

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - keyboardinterrupt.docker
```

## License

MIT / BSD

## Author Information

- [KeyboardInterrupt](https://blog.keyboardinterrupt.com)
