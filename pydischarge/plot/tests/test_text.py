# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2018-2020)
#
# This file is part of pyDischarge.
#
# pyDischarge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyDischarge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyDischarge.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for `pydischarge.plot.text`
"""

import pytest

from matplotlib import rc_context

from astropy.units import Unit

from .. import text as plot_text


@pytest.mark.parametrize('in_, out, texout', [
    ('test', 'test', 'test'),
    (4.0, '4.0', '4',),
    (8, '8', '8'),
    (Unit('m/Hz2'), '$\\mathrm{m\\,Hz^{-2}}$', '$\\mathrm{m\\,Hz^{-2}}$'),
])
def test_to_string(in_, out, texout):
    with rc_context(rc={'text.usetex': False}):
        assert plot_text.to_string(in_) == out
    with rc_context(rc={'text.usetex': True}):
        assert plot_text.to_string(in_) == texout
