conf：配置目录
- nginx.conf：nginx配置文件
 	
html：默认站点目录，出现502时，会调用50x.html
- 50x.html：出现502时，会显示此页面
- index.html

logs：
- access.log：访问日志文件，可以查看网站用户访问情况信息
- error.log：错误日志文件，包括nginx启动故障

sbin：nginx命令目录