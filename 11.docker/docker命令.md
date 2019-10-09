### docker安装
1. yum install -y yum-utils device-mapper-persistent-data lvm2 <br>安装必须的库
2. yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo <br>设置仓库
3. yum -y install docker-ce <br> 安装docker
4. systemctl start docker <br> 启动docker
5. docker run hello-world <br> 测试运行hello-world

### 配置docker镜像加速器
1. 进入阿里云地址：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors
2. vim /etc/docker/daemon.json
3. 重启daemon：systemctl daemon-reload
4. 重启docker：systemctl  restart docker

### 基础命令
|命令 | 作用|
|-|-|
docker version | 查看版本
docker info | 
docker ps | 查询正在运行的容器
docker --help |
docker images |
docker images -a | 列出本地所有镜像
docker images -q | 只显示镜像ID
docker search redis | 从docker hub搜素镜像
docker search -s 50 redis | 超过50个点赞数的redis
docker search --no-trunc redis | 不省略
docker pull nginx | 下载最新版本nginx镜像
docker rmi nginx | 删除nginx镜像
docker rmi -f hello-world | 强制删除镜像
docker rmi 镜像id1 镜像id2 | 根据id删除镜像
docker rmi -f ${docker images -qa} | 删除所有镜像
docker logs -f -t --tail 10 容器NAME或者ID | 显示最新10条日志
docker top 容器NAME或者ID | 查看容器
docker inspect 容器NAME或者ID | 查看容器信息
docker cp NAMEID:/root/test.txt /opt/| 从容器里面拷贝文件到opt

### 启动命令
|命令 | 作用|
|- | -|
docker run -it --name cont 镜像NAME或ID | 交互式启动容器并指定一个别名
docker run -it -p 8888:8080 tomcat| 启动tomcat，docker端口为8888
docker run -it -P tomcat| 启动tomcat，随机指定docker端口
docker run -d centos  | 后台运行
exit | 容器退出
ctrl+P+Q | 容器不停止退出
docker attach NAMEID | 进入已启动的容器
docker exec -t NAMEID ls -l /root | 不进入容器运行命令
docker start cont | 启动名为cont的容器
docker restart cont | 重启容器
docker stop 容器NAME或者ID | 正常停止
docker kill NAME或者ID | 强制停止
docker commit -a='rza' -m 'tomcat test' 2dc24fb474c0 rza/tomcat:1.2| 生成新的docker镜像

### 容器卷
|命令|作用|
|-|-|
docker run -it -v 宿主机路径:/容器路径 镜像名| 生成两个对应的文件夹，宿主机和容器共享
docker build -f /opt/mydocker/Dockerfile -t rza_centos . | 用dockerfile构建镜像
docker inspect 容器id | 查看容器相关信息 