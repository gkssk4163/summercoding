# summercoding
TODO List

### 개발환경
Ubuntu 18.04 LTS

### 설치 및 빌드 방법
```bash
$ sudo apt-get update
$ sudo apt install python3.6
$ sudo apt install python3-pip

$ pip3 install django

$ sudo apt install git
$ git clone https://github.com/hanna0/summercoding.git website/

$ cd website/
$ python3 manage.py migrate
$ python3 manage.py createsuperuser #관리자ID/PW 
$ python3 manage.py collectstatic
$ python3 manage.py runserver 0:8000 --insecure
```

### 접속
https://[ip_address]:8000
