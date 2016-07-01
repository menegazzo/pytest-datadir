.. _pytest: http://pytest.org

.. |python| image:: https://img.shields.io/pypi/pyversions/pytest-datadir.svg
  :target: https://pypi.python.org/pypi/pytest-datadir/

.. |version| image:: http://img.shields.io/pypi/v/pytest-datadir.svg
  :target: https://pypi.python.org/pypi/pytest-datadir
  
.. |downloads| image:: http://img.shields.io/pypi/dm/pytest-datadir.svg
  :target: https://pypi.python.org/pypi/pytest-datadir
  
.. |travis| image:: https://img.shields.io/travis/menegazzo/pytest-datadir/master.svg
  :target: https://travis-ci.org/menegazzo/pytest-datadir

.. |coverage| image:: http://img.shields.io/coveralls/menegazzo/pytest-datadir.svg
  :target: https://coveralls.io/r/menegazzo/pytest-datadir

==============
pytest-datadir
==============

pytest-datadir is a `pytest`_ plugin that allows programmers to add auxiliary
files (such as expected results, configuration files, and others) to tests.

It works over `tmpdir` fixture by copying the auxiliary files to the temporary
directory. The returning object is the `tmpdir` itself. The original files will
be preserved, always.

|python| |version| |downloads| |travis| |coverage|

Usage
=====

Create a folder with the same name as your test module and add all necessary files there.

.. code-block::

    ./
    - test_foo/
      - foo.bar
      - alpha.json
      - bravo.yaml
    - test_foo.py

Then use `datadir` fixture just like `tmpdir`.

.. code-block:: python

    def test_foo(datadir):
        assert datadir.join('foo.bar').isfile() is True
        assert datadir.join('alpha.json').isfile() is True
        assert datadir.join('bravo.yaml').isfile() is True
        
        new_filename = datadir.join('new.filename')
        assert new_filename.isfile() is False
        
        new_filename.ensure()
        assert new_filename.isfile() is True

Releases
========

Please consult the `releases page`_.

.. _releases page: https://github.com/menegazzo/pytest-datadir/releases

Bugs/Requests
=============

Please report any issues or feature requests in the `issue tracker`_.

.. _issue tracker: https://github.com/menegazzo/pytest-datadir/issues

Contributing
============

Contributions are welcome, so feel free to submit a bug or feature
request.

Pull requests are highly appreciated (tests and coverage are required)!
