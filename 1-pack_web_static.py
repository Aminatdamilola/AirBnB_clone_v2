#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of the web_static folder 
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """create .tgz file and archive the contents of web_static folder"""
local("mkdir -p versions")
time_str = datetime.now().strftime("%Y%m%d%H%M%S")
archive_name = "web_static_{}.tgz".format(time_str)
    result = local("tar -czvf versions/{} web_static".format(archive_name))
 if result.failed:
        return None
return "versions/{}".format(archive_name)
