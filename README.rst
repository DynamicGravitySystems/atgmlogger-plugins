ATGMLogger-Plugins
==================

ATGMLogger-Plugins is a plugin package for the atgmlogger serial logging
application, containing non-essential feature plugins to extend functionality.

Build
-----

Execute:

.. code-block::

    # Build a wheel package (requires wheel: [pip install wheel])
    python setup.py bdist_wheel

    # or for a source distribution (tar.gz)
    python setup.py sdist


Installation
------------

Using pip and venv:

.. code-block::

    cd <atgmlogger install path/venv>
    source venv/scripts/activate
    pip install <path-to-atgmlogger-plugins.whl>

atgmlogger will automatically attempt to load plugins if they are available,
and if a configuration directive with the plugin's name is present in the
atgmlogger.json configuration file. See the example_configs directory for
example configuration parameters relating to the available plugins.
