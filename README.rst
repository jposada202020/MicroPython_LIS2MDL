⛔️ DEPRECATED
===============

This repository is no longer supported, please consider using alternatives.

.. image:: http://unmaintained.tech/badge.svg
  :target: http://unmaintained.tech
  :alt: No Maintenance Intended

MicroPython Driver for the ST LIS2MDL Magnetometer sensor


Installing with mip
====================
To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_LIS2MDL

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_LIS2MDL")


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_LIS2MDL/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_LIS2MDL/examples.json")


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-lis2mdl/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-lis2mdl

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-lis2mdl

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-lis2mdl


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://micropython-lis2mdl.readthedocs.io/en/latest/>`_.
