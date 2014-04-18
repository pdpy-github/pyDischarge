# coding=utf-8
# Copyright (C) Duncan Macleod (2013)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

"""Read gravitational-wave data from a cache of files
"""

from astropy.io import registry

from glue.ligolw.lsctables import TableByName

from ...io.cache import (identify_cache, identify_cache_file,
                         read_cache_factory)


# register cache reading for all lsctables
for table in TableByName.itervalues():
    registry.register_reader('lcf', table, read_cache_factory(table))
    registry.register_reader('cache', table, read_cache_factory(table))
    registry.register_identifier('lcf', table, identify_cache_file)
    registry.register_identifier('cache', table, identify_cache)
