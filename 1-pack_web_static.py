#!/usr/bin/python3
""" A script that generates a .tgz archive from the contents of the
web_static folder of AirBnB using the function do_pack.
Archives must be stored in the folder versions
All files in the web_static must be added to the final archive
Name of executable:
    web_static_<year><month><day><hour><minute><second>.tgz
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ The function to generate the .tgz archive """
    try:
        # Create the versions directory if it dosnt exist
        local("mkdir -p versions")

        # Generate the file name based on the current date and time
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(time_format)

        # Create the .tgz archive
        local("tar -czvf versions/{} web_static".format(file_name))

        # Return the archive path
        return "versions/{}".format(file_name)

    except Exception as e:
        print("Error:", e)
        return None
