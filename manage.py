# -*- coding: utf-8 -*-
# 脚本，比如启动服务器，与数据库交互

from app import app
import os

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000));
	host = "127.0.0.1";
	app.run(host=host, port=port, debug=True);