# R-ERP

## 创建django项目

`django-admin startpoject backend R-ERP`
### 创建sqlite3数据库
`touch db.sqlite3`
`python manage.py migrate`
```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
* 创建app
`python manage.py startapp orders backend`

### 创建后台admin
`python manage.py createsuperuser`

## 前端采用开源Ant Design Vue Pro
`git clone https://github.com/vueComponent/ant-design-vue-pro.git`

`mv ant-design-vue-pro frontend`

### 启动前端
`npm run serve`
  App running at:
  - Local:   http://localhost:8010/
  - Network: http://192.168.8.103:8010/

## 功能修改
### 修改登录功能
#### 前端修改


#### 后端添加

