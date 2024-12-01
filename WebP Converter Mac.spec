# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['webp_to_mp4_converter.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'imageio',
        'imageio_ffmpeg',
        'moviepy',
        'numpy',
        'cv2',
        'customtkinter',
        'packaging.version',
        'packaging.specifiers',
        'packaging.requirements'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='WebP Converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,  
    codesign_identity=None,
    entitlements_file='entitlements.plist',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='WebP Converter',
)

app = BUNDLE(
    coll,
    name='WebP Converter.app',
    icon='icon.icns',
    bundle_identifier='com.emilhaybullin.webpconverter',
    info_plist={
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.15.0',
        'NSRequiresAquaSystemAppearance': False,
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
    },
)
