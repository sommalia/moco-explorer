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
* Documentation: https://moco-explorer.readthedocs.io (work in progress)

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
==========

Currently the following endpoints can be queried

* company
* contact
* invoice
* offer
* project
* user

.. note::

    For more information see `moco_explorer --help`.

Retrieving a list of *all* contacts in *csv* format

.. code-block:: shell

    $ moco_explorer -f csv contact getlist -a


Retrieving a single company object (id 123) in *json* format

.. code-block:: shell

    $ moco_explorer -f json company get 123


Get an overview over a specific project (id 1233, include company information in response)

.. code-block:: shell

    $ moco_explorer -f text project get 1233 --include-company




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
