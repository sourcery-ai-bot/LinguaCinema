# -*- mode: python -*-
a = Analysis(['LinguaCinema.py'],
             pathex=['../Lingualeo_player'],
             hiddenimports=[],
             hookspath=None)
a.datas += [
            ('bitmaps/player_next.png', '../Lingualeo_player/bitmaps/player_next.png',  'DATA'),
            ('bitmaps/player_play.png', '../Lingualeo_player/bitmaps/player_play.png',  'DATA'),
            ('bitmaps/player_prev.png', '../Lingualeo_player/bitmaps/player_prev.png',  'DATA'),
            ('bitmaps/player_stop.png', '../Lingualeo_player/bitmaps/player_stop.png',  'DATA'),
            ('bitmaps/player_pause.png', '../Lingualeo_player/bitmaps/player_pause.png',  'DATA'),
            ('mplayer2.exe', '../Lingualeo_player/mplayer2.exe',  'DATA'),
            ('mplayer/subfont.ttf', '../Lingualeo_player/mplayer/subfont.ttf',  'DATA'),
            ('bitmaps/flags/en.png', '../Lingualeo_player/bitmaps/flags/en.png',  'DATA'),
            ('bitmaps/flags/ru.png', '../Lingualeo_player/bitmaps/flags/ru.png',  'DATA'),
            ('bitmaps/flags/es.png', '../Lingualeo_player/bitmaps/flags/es.png',  'DATA'),
            ('bitmaps/flags/fr.png', '../Lingualeo_player/bitmaps/flags/fr.png',  'DATA'),
            ('bitmaps/flags/de.png', '../Lingualeo_player/bitmaps/flags/de.png',  'DATA'),
            ('bitmaps/flags/it.png', '../Lingualeo_player/bitmaps/flags/it.png',  'DATA'),
            ('bitmaps/flags/pt-pt.png', '../Lingualeo_player/bitmaps/flags/pt-pt.png',  'DATA'),
            ('bitmaps/flags/pt-br.png', '../Lingualeo_player/bitmaps/flags/pt-br.png',  'DATA'),
            ('bitmaps/flags/en.png', '../Lingualeo_player/bitmaps/flags/en.png',  'DATA'),
            ('bitmaps/flags/en.png', '../Lingualeo_player/bitmaps/flags/en.png',  'DATA'),
            ('locale/ru_RU/LC_MESSAGES/LinguaCinema.mo', '../Lingualeo_player/locale/ru_RU/LC_MESSAGES/LinguaCinema.mo',  'DATA'),
            ('locale/en_US/LC_MESSAGES/LinguaCinema.mo', '../Lingualeo_player/locale/en_US/LC_MESSAGES/LinguaCinema.mo',  'DATA'),
            ('locale/pt_BR/LC_MESSAGES/LinguaCinema.mo', '../Lingualeo_player/locale/pt_BR/LC_MESSAGES/LinguaCinema.mo',  'DATA'),
           ]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.linux&osx/LinguaCinema', 'LinguaCinema'),
          debug=False,
          strip=None,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'LinguaCinema.linux&osx'))
