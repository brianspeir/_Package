${PACKAGE_NAME} Repository
==========================

Write a one line summary here...

And a longer description including more stuff should go here. The
maximum line length is limted to 72 characters.

`Look <http://www.brianspeir.com>`_.

Package Sturcture
-----------------

The structure of the package.

::

    .
    │
    ├── documents                      <--- Document everything.
    │   │
    │   ├── _build
    │   │
    │   ├── _static
    │   │
    │   ├── _templates
    │   │
    │   ├── config.py
    │   │
    │   ├── index.rst
    │   │
    │   └── Makefile
    │
    ├── derived_data                   <--- Temp, cache, etc...
    │   │
    │   .
    │
    ├── module                         <--- Most code goes here.
    │   │
    │   ├── base
    │   │   │
    │   │   .
    │   │
    │   ├── __init__.py
    │   │
    │   ├── core.py
    │   │
    │   └── helpers.py
    │
    ├── tests                          <--- Test everything.
    │   │
    │   ├── __init__.py
    │   │
    │   ├── context.py                 <--- Fuck camelCase...
    │   │
    │   ├── test_advanced.py
    │   │
    │   └── test_basic.py
    │
    ├── vendor
    │   │
    │   .
    │
    ├── .env                           <--- Maybe a good idea.
    │
    ├── .gitignore                     <--- Umm... yes!
    │
    ├── AUTHORS                        <--- Give credit if due.
    │
    ├── CHANGELOG                      <--- Good luck.
    │
    ├── LICENSE                        <--- License everything.
    │
    ├── Makefile                       <--- Fucking awesome!
    │
    ├── manage.py                      <--- Make needs friends.
    │
    ├── README.rst                     <--- Tell me lies. But tell me.
    │
    ├── requirements.txt               <--- Thanks, that helped.
    │
    └── setup.py                       <--- Not for me.
