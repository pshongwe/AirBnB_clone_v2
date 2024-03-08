#!/usr/bin/python3
import os
from fabric.api import env, put, run
"""deploy """

env.hosts = ['54.89.116.199', '54.173.38.154']


def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    name = file_name.split(".")[0]
    dest_path = "/data/web_static/releases/{}/".format(name)

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(dest_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_path))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf {}web_static".format(dest_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_path))
        return True
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
