#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""pack web static"""


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
    if local("mkdir -p versions").failed is True:
        return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return archive_name
