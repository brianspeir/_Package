#
# Copyright (C) 2014 Brian Speir. All rights reserved.
#
# Licensed under The BSD 3-Clause License (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of
# the License at http://opensource.org/licenses/BSD-3-Clause.
#
#

# module.Makefile
#
# Write a one line summary here...
#
# And a longer description including the modules and subpackages exported
# by this package should go here. The maximum line length for doctrings or
# comments is limted to 72 characters.
#
#

init:
	@sudo pip install -r requirements.txt --use-mirrors

test:
	@nosetests tests

clean:
	@echo "Recursivly removing .pyc files."
	@find . -name "*.pyc" -delete
