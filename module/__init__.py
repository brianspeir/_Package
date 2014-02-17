# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Brian Speir. All rights reserved.
#
# Licensed under The BSD 3-Clause License (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of
# the License at http://opensource.org/licenses/BSD-3-Clause.
#
#

"""module

Write a one line summary here...

And a longer description including more stuff should go here. The
maximum line length for doctrings or comments is limted to 72
characters.

"""

__version__ = "major.minor.maintenance-pre"

from .core import hmm


def register_blueprints(app):
    # Prevent circular imports by registering blueprint in a method.
    # http://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/
    from module.core import get_hmm
    app.register_blueprint(get_hmm.blueprint)
