<h3>You can run it as an executable. Download the .exe file and open it.</h3>
<h4>
  It will start on your local IP (find your IP from the command prompt using "ipconfig") and port 2121. 
  Use the following credentials: Username - root, Password - 456456.
</h4>

<h3>To configure dev env.</h3>

Create virtual environment

```sh
  python -m venv myenv
```

Install 'pyftpdlib'

```sh
  pip install pyftpdlib
```

Install 'pyinstaller'

```sh
  pip install pyinstaller
```

Make EXE

```sh
  pyinstaller --onefile .\ftpServer.py
```
