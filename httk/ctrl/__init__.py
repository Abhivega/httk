# 
#    The high-throughput toolkit (httk)
#    Copyright (C) 2012-2013 Rickard Armiento
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
httk Control module

  - Core parts of command line tools, etc., for controlling httk projects 
  - Handling project directories, project states
  - Starting execution of jobs locally, on cluster
  - Fetch output, supervise run status
  - Move jobs between clusters, etc.
"""


from httk.core import citation
citation.add_src_citation("httk","Rickard Armiento")

from project import *
from utils import *
from control import *
