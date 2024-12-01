#define MyAppName "Universal Format Converter"
#define MyAppVersion "1.0"
#define MyAppPublisher "Emil Haybullin"
#define MyAppExeName "Universal Format Converter.exe"

[Setup]
; Уникальный идентификатор для приложения
AppId={{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Путь к иконке установщика
SetupIconFile=app_icon.ico
; Сжатие
Compression=lzma
SolidCompression=yes
; Современный стиль установщика
WizardStyle=modern
; Разрешить выбор папки установки
DisableDirPage=no
; Создавать ярлык на рабочем столе
DisableProgramGroupPage=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Путь к папке с собранным приложением
Source: "dist\Universal Format Converter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
