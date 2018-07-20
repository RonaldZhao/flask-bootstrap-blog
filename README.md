# flask-bootstrap-blog

基于Python3.6 + Flask + Bootstrap4 + MySQL8.0

## 已实现功能

- 用户注册
- 用户登录
- 用户注销
- 修改用户名
- 发布文章(支持Markdown语法)
- 文章列表
- 文章详情

## 用法

1. 下载, 解压, 新建并激活虚拟环境

2. 执行`pip install -r requirements.txt`

3. 到`blog/config.py`文件中配置数据库连接信息, 默认密码为`123456`, 默认数据库为`blog`

4. 执行`python manage.py shell`, 进入后执行`db.create_all()`, 然后`quit()`

5. 执行`python manage.py dev`启动服务, Done.