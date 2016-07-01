# encoding: UTF-8
from __future__ import unicode_literals

from pytest_datadir import datadir
import os


def test_datadir(datadir, tmpdir, request):
    assert datadir == tmpdir

    dirname = os.path.dirname(request.module.__file__)
    dirname = os.path.join(dirname, request.function.__name__)
    assert os.listdir(dirname) == os.listdir(str(datadir))

    datadir.ensure('foo.bar')
    assert os.listdir(dirname) != os.listdir(str(datadir))
    assert sorted(os.listdir(dirname) + ['foo.bar']) == sorted(os.listdir(str(datadir)))
