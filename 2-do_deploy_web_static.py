#!/usr/bin/python3
# Fabfile based on the file 1-pack_web_static.py) that distributes an
# archive to your web servers

import os
from fabric.api import *
from fabric.contrib import files

env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'
env.hosts = ['18.206.233.250', '34.239.255.79']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path: path of the archive to distribute.

    Returns:
        True if all operations have been done correctly, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name, ext = os.path.splitext(filename)

    put(archive_path, '/tmp/')

    run('mkdir -p /data/web_static/releases/{}'.format(name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(filename, name))

    run('rm /tmp/{}'.format(filename))
    run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(name, name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
    run('rm -rf /data/web_static/current')

    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(name))

    return True
