/* Standard Hurd pathnames.
   Copyright (C) 1991 Free Software Foundation

This file is part of the GNU Hurd.

The GNU Hurd is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 1, or (at your option)
any later version.

The GNU Hurd is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the GNU Hurd; see the file COPYING.  If not, write to
the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.  */

#pragma once

/* Port rendezvous points are specified by symbols _SERVERS_FOO,
   the canonical pathname being /servers/foo.  */

#define	_SERVERS_CORE	"/servers/core"


/* Hurd servers are specified by symbols _HURD_FOO,
   the canonical pathname being /hurd/foo.  */

#define	_HURD_IFSOCK	"/hurd/ifsock"
#define	_HURD_SYMLINK	"/hurd/symlink"
