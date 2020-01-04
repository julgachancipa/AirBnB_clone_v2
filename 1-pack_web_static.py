#!/usr/bin/python3
"""Pack web static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress files"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(current_date))
        return out_var
    except:
        return None
