# 目录结构  

···
├─class-21-3-24
│  │  application.py
│  │  manager.py
│  │  readme.md
│  │  release.sh
│  │  requirtments.txt
│  │  uwsgi.ini
│  │  www.py
│  ├─common
│  │  ├─libs
│  │  └─models
│  ├─config
│  ├─docs
│  ├─jobs
│  │  ├─bin
│  │  └─tasks
│  └─web
│      ├─controllers
│      ├─interceptors
│      ├─static
│      └─templates
···

########################################  
service firewalld stop--关闭防火墙  

## 报错解决  

vscode中/web/controllers/static.py报错  
修改.vscode文件为  
···
{
    "python.pythonPath": "/home/apr/anaconda3/envs/api_misuse/bin/python",
    // "terminal.integrated.env.osx": {"PYTHONPATH": "${workspaceFolder}"},
    "python.linting.pylintArgs": [
        // "--disable=F0401"
        "--disable=E0401"
    ]
}
···