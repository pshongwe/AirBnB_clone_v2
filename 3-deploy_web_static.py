#!/usr/bin/python3
from fabric.api import local, env, put, run
from datetime import datetime
import os
"""pack and deploy web static"""

env.hosts = ['54.89.116.199', '54.173.38.154']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the directory versions if it doesn't exist
    local("mkdir -p versions")
    # Get the current time in the format: yearmonthdayhourminutesecond
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    # Name of the archive
    archive_name = "versions/web_static_{}.tgz".format(now)
    # Create the archive
    local("tar -cvzf {} web_static".format(archive_name))
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None
    return archive_name


def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    fn = os.path.basename(archive_path)
    name = fn.split(".")[0]
    destPath = "/data/web_static/releases/{}/".format(name)
    currentPath = "/data/web_static/current"
    if put(archive_path, "/tmp/{}".format(fn)).failed is True:
        return False
    if run("sudo mkdir -p {}".format(destPath)).failed is True:
        return False
    if run("sudo tar -xzf /tmp/{} -C {}".format(fn, destPath)).failed is True:
        return False
    if run("sudo rm /tmp/{}".format(fn)).failed is True:
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


def deploy():
    """Full blown deploy"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
