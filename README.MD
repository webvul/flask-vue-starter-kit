> 基于 flask + vue 敏捷开发

## 架构

- 后端api [flask-restful](https://flask-restful.readthedocs.io/en/latest/)
- 前端组件库 [Element](http://element.eleme.io/)

## 项目结构

```
.
├── README.md
├── client //前端代码
│   ├── README.md
│   ├── build
│   ├── config
│   ├── index.html
│   ├── node_modules
│   ├── package.json
│   ├── src
│   ├── static
│   └── test
├── deploy //部署所需文件
│   └── requirements.txt
├── manage.py
├── server //后端代码
│   ├── api.py //导入controllers,分配uri
│   ├── config //数据库、邮件配置
│   ├── controllers //存放后端各个模块的逻辑代码
│   └── helpers //公共常用函数方法
├── start.sh
└── venv //虚拟环境
    ├── bin
    ├── include
    ├── lib
    └── pip-selfcheck.json
```
## 后端
```
sh start.sh
source venv/bin/activate
python manage.py runserver --threaded -h 0.0.0.0 -D -r
```

## 前端
```
cd client
npm(cnpm) i
npm run dev
npm run build
```

