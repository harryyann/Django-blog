# 设置基础镜像
FROM daocloud.io/python:3.6
MAINTAINER HarryYann

ADD . /app
WORKDIR /app

# 安装依赖, 使用阿里云镜像
RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ -r ./requirements.txt --trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ gunicorn --trusted-host mirrors.aliyun.com