#
# binding.gyp - Nodem build script
#
# Written by David Wicksell <dlw@linux.com>
# Copyright © 2012-2016,2018 Fourth Watch Software LC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License (AGPL)
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#

{
  'targets': [
    {
      'target_name': 'mumps',
      'type': 'loadable_module',
      'sources': [
        'src/mumps.cc'
      ],
      'cflags': [
        '-ansi',
        '-pedantic',
        '-std=c++11',
        '-Wno-deprecated-declarations',
        '-Wno-expansion-to-defined'
      ],
      'defines': [
        'GTM_VERSION=63'
      ],
      'variables': {
        'gtm_dist%': '<!(if test "$ydb_dist" != "" ; then echo $ydb_dist; else echo $gtm_dist; fi)'
      },
      'include_dirs': [
        '<(gtm_dist)'
      ],
      'libraries': [
        '-L<(gtm_dist)',
        '-lgtmshr',
        '-lyottadb'
      ],
      'ldflags': [
        '-Wl,-rpath,<(gtm_dist),--enable-new-dtags'
      ]
    }
  ]
}
