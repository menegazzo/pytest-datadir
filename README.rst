.. _pytest: http://pytest.org

.. |python| image:: https://img.shields.io/pypi/pyversions/pytest-stash.svg
  :target: https://pypi.python.org/pypi/pytest-stash/

.. |version| image:: http://img.shields.io/pypi/v/pytest-stash.svg
  :target: https://pypi.python.org/pypi/pytest-stash
  
.. |downloads| image:: http://img.shields.io/pypi/dm/pytest-stash.svg
  :target: https://pypi.python.org/pypi/pytest-stash
  
.. |travis| image:: https://img.shields.io/travis/menegazzo/pytest-stash/master.svg
  :target: https://travis-ci.org/menegazzo/pytest-stash

.. |coverage| image:: http://img.shields.io/coveralls/menegazzo/pytest-stash.svg
  :target: https://coveralls.io/r/menegazzo/pytest-stash

============
pytest-stash
============

pytest-stash is a `pytest`_ plugin that allows programmers to add auxiliary
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

Then use `stash` fixture just like `tmpdir`.

.. code-block:: python

    def test_foo(stash):
        assert stash.join('foo.bar').isfile() is True
        assert stash.join('alpha.json').isfile() is True
        assert stash.join('bravo.yaml').isfile() is True
        
        new_filename = stash.join('new.filename')
        assert new_filename.isfile() is False
        
        new_filename.ensure()
        assert new_filename.isfile() is True

Releases
========

Please consult the `releases page`_.

.. _releases page: https://github.com/menegazzo/pytest-stash/releases

Bugs/Requests
=============

Please report any issues or feature requests in the `issue tracker`_.

.. _issue tracker: https://github.com/menegazzo/pytest-stash/issues

Contributing
============

Contributions are welcome, so feel free to submit a bug or feature
request.

Pull requests are highly appreciated (tests and coverage are required)!
