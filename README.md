# node

## 1. Installation
1. Python Dependencies ```pip3 install -r requirements.txt```
2. Gunicorn ```apt install gunicorn3```

## 2. Running the code
### 2.1 http
```
sudo gunicorn3 app:app --workers 3 --threads=2 --bind 0.0.0.0:80 --log-file app.log --access-logfile access.log --log-level DEBUG
```

### 2.2 https
```
sudo gunicorn3 --workers 3 --threads=2 --certfile '/etc/letsencrypt/live/sentinel-node1.anudit.dev/fullchain.pem' --keyfile '/etc/letsencrypt/live/sentinel-node1.anudit.dev/privkey.pem' --log-file app.log --access-logfile access.log --log-level DEBUG -b 0.0.0.0:443 app:app
```

## 3. Code Linting
```
pylint --rcfile=pylintrc app.py
```
