#!/usr/bin/python3
import os
from fabric.api import env, put, run
"""deploy """

env.hosts = ['54.89.116.199', '54.173.38.154']


def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    fileName = os.path.basename(archive_path)
    name = fileName.split(".")[0]
    destPath = "/data/web_static/releases/{}/".format(name)
    currentPath = "/data/web_static/current"
    if put(archive_path, "/tmp/{}".format(fileName)).failed is True:
        return False
    if run("sudo mkdir -p {}".format(destPath)).failed is True:
        return False
    if run("sudo tar -xzf /tmp/{} -C {}".format(fileName, destPath)).failed is True:
        return False
    if run("rm /tmp/{}".format(fileName)).failed is True:
        return False
    if run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("sudo rm -rf {}web_static".format(destPath)).failed is True:
        return False
    if run("sudo rm -rf {}".format(currentPath)).failed is True:
        return False
    if run("sudo ln -s {} {}".format(destPath, currentPath)).failed is True:
        return False
    print("New version deployed!")
    return True
