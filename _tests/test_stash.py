# encoding: UTF-8
from __future__ import unicode_literals

import os

from pytest_stash import stash


def test_stash(stash, tmpdir, request):
    assert stash == tmpdir

    dirname = os.path.dirname(request.module.__file__)
    dirname = os.path.join(dirname, request.function.__name__)
    assert os.listdir(dirname) == os.listdir(str(stash))

    foo_file = stash.join('foo.bar')
    assert foo_file.check() is False

    stash.ensure('foo.bar')
    assert foo_file.check() is True
    assert os.listdir(dirname) != os.listdir(str(stash))
    assert sorted(os.listdir(dirname) + ['foo.bar']) == sorted(os.listdir(str(stash)))

    deeper_file = stash.join('inner-folder', 'deeper-folder', 'charlie.c')
    assert deeper_file.check() is True
    assert deeper_file.read_text('utf-8') == 'charlie'
