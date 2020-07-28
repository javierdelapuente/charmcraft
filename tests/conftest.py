# Copyright 2020 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For further info, check https://github.com/canonical/charmcraft

import pathlib

import pytest


@pytest.fixture
def tmp_path(tmp_path):
    """Always present a pathlib's Path.

    This is to avoid pytest using pythonlib2 in Python 3.5, which leads
    to several slight differences in the tests.

    This "middle layer fixture" has the same name of the pytest's fixture,
    so when we drop Py 3.5 support we will be able to just remove this,
    and all the tests automatically will use the standard one (no further
    changes needed).
    """
    return pathlib.Path(str(tmp_path))
