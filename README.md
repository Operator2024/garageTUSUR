# GarageTUSUR

Educational application. Developed by assignment. Educational variant number twelve


## Pyinstaller make

### Makefile
``
pyi-makespec --onedir --windowed --icon "D:/Coding/Python/github/garageTUSUR/src/images/python.ico" --name "GarageTUSUR"
--log-level "INFO" --noupx --version-file "D:/Coding/Python/github/garageTUSUR/build/file_version_info.txt" --exclude-module "altgraph" --exclude-module "future" --exclude-module "pefile" --exclude-module "pip" --exclude-module "pyinstaller" --exclude-module "setuptools" --upx-exclude "vcruntime140.dll" --upx-exclude "MSVCP140.dll" --upx-exclude "msvcp140.dll" --upx-exclude "msvcp140_1.dll" --upx-exclude "MSVCP140_1.dll" --upx-exclude "pyside2.abi3.dll" --upx-exclude "python37.dll" --upx-exclude "pythoncom37.dll" --upx-exclude "pywintypes37.dll" --upx-exclude "shiboken2.abi3.dll" --upx-exclude "vcruntime140_1.dll" --paths "D:/Coding/Python/github/garageTUSUR/venv/Lib/site-packages/shiboken2" --additional-hooks-dir "D:/Coding/Python/github/garageTUSUR/venv/Lib/site-packages/pkg_resources"  "D:/Coding/Python/github/garageTUSUR/garage_gui.py"
``

### Build makefile

``
pyinstaller --clean --noconfirm GarageTUSUR.spec
``

``
pyinstaller --clean --upx-dir "D:\Coding\upx-3.96-win64" "GarageTUSUR.spec"
``

При исопльзовании сжатия библиотек необходимо внимательно проверять название библиотек, так как
они чувствительны к регистру. Папку PySide лучше не сжимать, приложение не сможет запуститься.

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


