# python

# deta.sh
```
cd automate_emails
iwr https://get.deta.dev/cli.ps1 -useb | iex
```
output: Deta was installed successfully to C:\Users\Admin\.deta\bin\deta.exe

```
deta login
```

output:
Please, log in from the web page. Waiting...
https://web.deta.sh/cli/56999
Logged in successfully.

```
deta new --python email_automation
```

output:
Successfully created a new micro
{
        "name": "email_automation",
        "id": "f135dda6-8385-4c0d-b11f-8fc13cc0a1ba",
        "project": "c0uh9v6t",
        "runtime": "python3.9",
        "endpoint": "https://nw3caz.deta.dev",
        "region": "ap-southeast-1",
        "visor": "disabled",
        "http_auth": "disabled"
}

```
![image](https://user-images.githubusercontent.com/18412583/187964804-8c6d2440-a947-449c-b381-70bd0fb0666d.png)


PS D:\CNTT\Python\SourceCode\automate_emails> deta visor enable
Successfully enabled visor mode
PS D:\CNTT\Python\SourceCode\automate_emails> deta update -e ".env"
Updating environment variables...
Successfully updated micro's environment variables
PS D:\CNTT\Python\SourceCode\automate_emails> deta deploy
Deploying...
Successfully deployed changes
Updating dependencies...
Collecting pandas
  Downloading https://files.pythonhosted.org/packages/91/2e/f2e84148e71dda670b310f1f7b9a220181e5dc1fe2f9dcf6a8632412bf4e/pandas-1.4.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7MB)
Collecting python-dotenv
  Downloading https://files.pythonhosted.org/packages/30/5f/2e5c564bd86349fe6b82ca840f46acf6f4bb76d79ba9057fce3d3e008864/python_dotenv-0.20.0-py3-none-any.whl
Collecting numpy>=1.18.5; platform_machine != "aarch64" and platform_machine != "arm64" and python_version < "3.10"
  Downloading https://files.pythonhosted.org/packages/f8/ea/ff38168d6565a8549f819699cac4d89bbc38fc5b27fb94f8e92bcd713348/numpy-1.23.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1MB)
Collecting pytz>=2020.1
  Downloading https://files.pythonhosted.org/packages/d5/50/54451e88e3da4616286029a3a17fc377de817f66a0f50e1faaee90161724/pytz-2022.2.1-py2.py3-none-any.whl (500kB)
Collecting python-dateutil>=2.8.1
  Downloading https://files.pythonhosted.org/packages/36/7a/87837f39d0296e723bb9b62bbb257d0355c7f6128853c78955f57342a56d/python_dateutil-2.8.2-py2.py3-none-any.whl (247kB)
Collecting six>=1.5
  Downloading https://files.pythonhosted.org/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl
Installing collected packages: numpy, pytz, six, python-dateutil, pandas, python-dotenv
Successfully installed numpy-1.23.2 pandas-1.4.4 python-dateutil-2.8.2 python-dotenv-0.20.0 pytz-2022.2.1 six-1.16.0
You should consider upgrading via the 'pip install --upgrade pip' command.

PS D:\CNTT\Python\SourceCode\automate_emails> deta cron set "10 minutes"
```

