pieceofcake - a user-friendly cookiecutter wrapper
==================================================

This is a wrapper around the `cookiecutter <https://github.com/cookiecutter/cookiecutter/>`_
tool which provides a more user-friendly way of asking questions.

With **cookiecutter**, the user is not presented with any questions, just the names
of the parameters to set::

    % cookiecutter gh:astrofrog/fake-template
    package_name [example]: test-package
    include_example_code [n]: y

With **pieceofcake**, the user is shown a series of verbose questions which provide
more context as to the meaning/implications of each parameter::

    % cookiecutter gh:astrofrog/fake-template final-package

    Welcome to the pieceofcake, a user-friendly cookiecutter wrapper!

    This script will now ask you a series of questions to help you set up
    your package.

    What is the name of your package? This is the name that will appear on
    PyPI and which users will use when installing the package with e.g.
    pip or conda.
    > Package name [example]: test-package

    Should example code be included? This will consist of sample Python
    and Cython files in the package, demonstrating how to create different
    sub-modules and importing between them.
    > Include example code? [n]: y

    Running cookiecutter...

    You should now be all set! Your generated package is in final-package

Installing
==========

To install, run::

    pip install pieceofcake

Using
=====

To use **pieceofcake**::

    pieceofcake template output_directory

where ``template`` follows the same syntax as for cookiecutter, and can be
the path to a local directory, or e.g. gh:astrofrog/fake-template to use
a GitHub repository.

Note that ``pieceofcake`` will work with all cookiecutter templates, but
nice questions will only be shown if the ``cookiecutter.json`` file contains
the ``_parameters`` key as described below in **For template creators**.

For template creators
=====================

To define questions for each parameter, add a new ``_parameters`` key in
your ``cookiecutter.json`` file, which should then contain a dictionary for
each parameter::

    "_parameters": {
        "package_name": {
            "default_value": "test-package",
            "prompt": "Package name",
            "help": "What is the name of your package? This is the name that will appear on PyPI and which users will use when installing the package with e.g. pip or conda."
        },
        "include_example_code": {
            "prompt": "Include example code?",
            "help": "Should example code be included? This will consist of sample Python and Cython files in the package, demonstrating how to create different sub-modules and importing between them."
        }
    }

The ``default_value``, ``prompt``, and ``help`` keys are all optional - if
``default_value`` is not defined, the default value is taken from the main
``cookiecutter`` section. If ``prompt`` is not included, it is set to the
parameter name, and if ``help`` is not included, no help/question is shown.

This approach was inspired by `cookiecutter/cookiecutter#794
<https://github.com/cookiecutter/cookiecutter/issues/794>`_
