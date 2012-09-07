{
  'targets': [
    {
      'target_name': 'libmagic_lib',
      'type': 'static_library',
      'include_dirs': [ '.', 'src', 'pcre' ],
      'dependencies': [
        'pcre/binding.gyp:pcre_lib',
      ],
      'defines': [ 'HAVE_CONFIG_H' ],
      'conditions': [
        [ 'OS=="win"', {
          'sources': [
            'src/asprintf.c',
            'src/strlcat.c',
            'src/strlcpy.c',
            'src/getline.c',
          ],
          'include_dirs': [ 'msvc', 'config/win' ],
          'defines': [
            'WIN32', '_WIN32', '_USE_32BIT_TIME_T'
          ],
          'libraries': [
            'shlwapi.lib'
          ],
        }],
        [ 'OS=="linux"', {
          'sources': [
            'src/strlcat.c',
            'src/strlcpy.c',
          ],
          'include_dirs': [ 'config/linux' ],
        }],
        [ 'OS=="mac"', {
          'include_dirs': [ 'config/mac' ],
        }],
        [ 'OS=="freebsd"', {
          'include_dirs': [
            'config/freebsd',
          ],
        }],
      ],
      'cflags': [ '-O3' ],
      'sources': [
        'src/magic.c',
        'src/apprentice.c',
        'src/softmagic.c',
        'src/ascmagic.c',
        'src/encoding.c',
        'src/compress.c',
        'src/is_tar.c',
        'src/readelf.c',
        'src/print.c',
        'src/fsmagic.c',
        'src/funcs.c',
        'src/apptype.c',
        'src/cdf.c',
        'src/cdf_time.c',
        'src/readcdf.c',
      ],
    },
  ]
}
