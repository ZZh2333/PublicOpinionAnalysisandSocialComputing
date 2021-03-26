# 目录结构  

···

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
