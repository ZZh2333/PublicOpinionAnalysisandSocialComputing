from application import app, manager
import traceback
import sys
from flask_script import Server
import www

# 添加运行方法和指令
manager.add_command("run",Server(host='127.0.0.1',port=5000,use_debugger=True,use_reloader=True))
manager.add_command("runserver",Server(host='0.0.0.0',port=5005,use_debugger=True,use_reloader=True))
# manager.add_command("run2",Server(host='0.0.0.0',port=5002,use_debugger=True,use_reloader=True))

def main():
    manager.run()

# 入口方法
if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()