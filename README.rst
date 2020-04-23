=============
moco-explorer
=============


.. image:: https://img.shields.io/pypi/v/moco_explorer.svg
        :target: https://pypi.python.org/pypi/moco-explorer

.. image:: https://img.shields.io/travis/sommalia/moco_explorer.svg
        :target: https://travis-ci.org/sommalia/moco-explorer

.. image:: https://readthedocs.org/projects/moco-explorer/badge/?version=latest
        :target: https://moco-explorer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


The quick and easy interface for exporting data from moco.


* Free software: GNU General Public License v3

Disclaimer
----------

This project is in no way finished, or polished.
I am not responsible for any commercial, financial or emotional damage that may or may not be caused by using this project.


Features
--------

* Easy access to your moco data
* Csv/Json/Text Export
* Authentication over cli with username and password


Requirements
------------

* python 3.5 or greater
* moco_wrapper 0.6.2 or greater

Installation
------------

From source
===========

.. code-block:: shell

    $ git clone https://github.com/sommalia/moco_explorer moco-explorer
    $ cd moco-explorer
    $ pip install -r requirements_dev.txt
    $ make install

From pip
========

.. code-block:: shell

    $ pip install moco_explorer

Quickstart
----------

Authentication
==============

To retrieve information from yout moco instance the moco_explorer needs to authenticate with it. For your first request,
it will stop and ask for your account information.

You can also manually create the configuration file with `moco_explore config create`.

.. code-block:: shell

    $ moco_explorer config create
    $ > Enter your moco domain: testcompany.mocoapp.com // testcompany would also work
    $ > Enter your moco email: testaccount@testcompany.com
    $ > Enter your moco password: *******

After that a config file in your users home directory will be created.

.. code-block:: shell

    $ cat $HOME/.moco_explorer.json
    {
        "domain": "testcompany",
        "api_key": "HERE IS THE API KEY"
    }

If you want to load or create your configuration file in an alternative location you can specify the path with the **-c/--config** option.


.. code-block:: shell

    $ moco_explorer -c $HOME/alternative-moco-config.json config create

By default the moco_explorer will look for the configuration file under $HOME/.moco_explorer.json. If you created the configuration
file in an alternative location make sure you always specify the **-c/--config** option.

What can I do?
==============

Currently the following endpoints can be queried (also accessible with `moco_explorer --help`)

.. code-block:: shell

    company
    contact
    deal
    invoice
    offer
    project
    user



Retrieving a list of **all** contacts in **csv** format

.. code-block:: shell

    $ moco_explorer -f csv contact getlist -a


Retrieving a single company object (id **123**) in **json** format

.. code-block:: shell

    $ moco_explorer -f json company get 123


Get an overview over a specific project (id **1233**)

.. code-block:: shell

    $ moco_explorer -f text project get 1233

Work through the **pages** of the projects (100 items per page). If you have more than 100 objects, the results are
paginated (eg. for 105 items, the first page will contain 100, the second 5 items).

.. code-block:: shell

    $ moco_explorer -f json project getlist --page 1
    $ moco_explorer -f json project getlist --page 2

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
