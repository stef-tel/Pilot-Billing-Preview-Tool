# -*- mode: python -*-

block_cipher = None


a = Analysis(['login_screen.py'],
             pathex=['C:\\Users\\sesa236189\\source\\repos\\testPyvot_v1\\testPyvot_v1\\testPyvot_v1', 'C:\\Users\\sesa236189\\source\\repos\\testPyvot_v1\\testPyvot_v1\\testPyvot_v1\\screens_test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='login_screen',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='login_screen')
