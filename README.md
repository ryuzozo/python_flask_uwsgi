# python_flask_uwsgi
https://amateur-engineer-blog.com/flask-uwsgi-nginx/

## Nginx/uWSGI install
apt update
apt install python3-pip
pip3 install uwsgi

## make application
create app.py
create wsgi.py
create app.ini

uwsgi --ini app.ini &

## Nginx
create myapp.conf (/etc/nginx/sites-enabled)

systemctl start nginx

→ダメ。別案

https://qiita.com/Jazuma/items/521cf31538cb618d285a

## flask
create __init__.py , manage.py


flask run実行後
curl http://localhost:5000/helloで実行確認 flaskの動作確認OK


uwsgi --http=0.0.0.0:8000 --wsgi-file=/tmp/flask_sample/manage.py --callable=application
画面確認 uwsgiの動作確認OK


