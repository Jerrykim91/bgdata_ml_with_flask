# 배포 진행과정 설명 

---

# aws
- 아마존 aws 콘솔 로그인 
- 네비바에서 서울로 위치를 맞추고 진행 
    - 만약에 다른나라로 설정하고 아래사항을 진행한 경우 삭제(종료)하고 다시 
- 네비바 서비스 -> EC2 ->인스턴트시작 클릭 ->  7단계가 나옴 

---

# EC2 - 총 7단계 
## 단계 1: Amazon Machine Image(AMI) 선택
    - 프리티어만 [체크]
        - 기본적으로 
        - 리눅스 
        - 윈도우 
    - Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - ami-0fc20dd1da406780b (64비트 x86) / ami-0959e8feedaf156bf (64비트 Arm)

## 단계 2: 인스턴스 유형 선택 
    - 바로 7단계로 이동(auto 잡혀서 디폴트로 세팅됨 그래서 7단계 )  

## 단계 7: 인스턴스 시작 검토
    - 새로 한사람 
        - 새 키 페어
    - 기존 
        - 기존 키 페어 
            - 체크박스 체크 
    - 인스턴스 아이디 : ********
    - IPv4 퍼블릭 IP
        - 13.***.97.*** : 내서버 아이피 
        - 도메인
---

# 데이터 베이스 
    - 엔드 포인트 (주소)
        - python-db.c2qr7mol2ce4.ap-northeast-2.rds.amazonaws.com
    - RDS 
    - 팝업창 - 기존 스타일로 바꾸기 클릭 
        -  엔진선택 
            - 마리아 - 체크박스 [체크]
        - DB 세부 정보 지정
            - 주의) 다중 AZ 배포(설정 x )
            - 스토리지 자동 조정 활성화[ 체크해제 ]
        - 설정 
            - DB 인스턴스 식별자 : python-db
            - 마스터 사용자 이름 : root
            - 마스터 암호 : 8자리 비번 
    - 고급 설정 구성
        - 퍼블릭 액세스 가능성 : y
    - 데이터베이스 옵션
        - 데이터베이스 이름
            - python_db
            - 3306
        -  안한다 함 
            스냅샷 x
            다 x 

## 마리아 디비로 이동 
    - 세션관리자에서 새 디비 생성
     - 디비 이름 : aws 
     - 호스트 명/ip : 엔드포인트 집어 넣음 
        - 역 세모 클릭 해서 리스트 여부로 연결을 확인가능하다 

## aws 이동 마리아 디비 관리 화면 클릭 
    - 하위 탭에 보안 그룹안에 링크로 이동
        - 인바운드룰 
---

## EC2 대시보드 
    - 실행중인 데시보드 클릭 
    - 실행중인 인스턴스 우클릭 
    - 연결  

## Download PuTTY
- https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
    - putty.exe (the SSH and Telnet client itself)
        - 64-bit
    - puttygen.exe (a RSA and DSA key generation utility)
        - 64-bit

## puttygen 가동 
    - 로드 클릭 
    - 모든 파일 클릭해서 팸파일 등록 
    - 팸파일 로드 되면 프라이빗 클릭 -> ppk 생성 여부를 확인 

## putty 가동 
- 호스트 네임에 IPv4 입력 ubuntu@
- EC2 인바운드 룰 확인 ->  Inbound rules 확인하고 매치 
- 세션에 저장 
    - 이름 입력() -> 저장 (리스트에 뜸)
    - 왼쪽 ssh ->auth -> 여기서 ppk 입력 
    - 오픈 누르지말고 다시 세션 저장으로 이동해서 
        - aws 저장 한번더 하고 오픈 -> 창뜨면 예 
        - 콘솔 창뜨면 종료하고 퓨티 다시 오픈 
    - 다시 퓨티 오픈하고 저장된거 확인 
    - 폰트 변경하고 다시오픈 

---

# 콘솔 - 서버 관리
```bash

---
# 기본화면 
Using username "ubuntu".
Authenticating with public key "imported-openssh-key"
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1057-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Mar 12 05:28:09 UTC 2020

  System load:  0.0               Processes:           88
  Usage of /:   13.8% of 7.69GB   Users logged in:     0
  Memory usage: 14%               IP address for eth0: 172.31.37.87
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.


Last login: Thu Mar 12 05:25:00 2020 from 61.83.51.99
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

--- # 기본 오픈 창 

ubuntu@ip-***:~$ ls # 아무것도 없음 

# 정상 체크 
ubuntu@ip-***:~$ cd ..
ubuntu@ip-***:/home$ cd ..
ubuntu@ip-***:/$ ls
bin   home            lib64       opt   sbin  tmp      vmlinuz.old
boot  initrd.img      lost+found  proc  snap  usr
dev   initrd.img.old  media       root  srv   var
etc   lib             mnt         run   sys   vmlinuz

# 로그 
ubuntu@ip-***:/$ cd var
ubuntu@ip-***:/var$ ls
backups  cache  crash  lib  local  lock  log  mail  opt  run  snap  spool  tmp
ubuntu@ip-***:/var$

# 다시 정상 환경 
ubuntu@ip-***:/var$ cd /home/ubuntu
ubuntu@ip-***:~$ cd

```
---
- 파일 두개 다운 
    - 강사님으로 부터 

```json
// deploy.json
{
    "REPO_URL":"https://github.com/kenshi/de",
    "PROJECT_NAME":"de",
    "REMOTE_HOST":"ec2-54-180-116-168.ap-northeast-2.compute.amazonaws.com",
    "REMOTE_HOST_SSH":"54.180.116.168",
    "REMOTE_USER":"ubuntu"
  }
```
---

```py  
# fabfile.py
#-*- coding:utf-8 -*-
# fabfile.py
from fabric.contrib.files import append, exists, sed, put
from fabric.api import env, local, run, sudo
import os
import json


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

envs = json.load(open(os.path.join(PROJECT_DIR, "deploy.json")))

REPO_URL = envs['REPO_URL']
PROJECT_NAME = envs['PROJECT_NAME']
REMOTE_HOST = envs['REMOTE_HOST']
REMOTE_HOST_SSH = envs['REMOTE_HOST_SSH']
REMOTE_USER = envs['REMOTE_USER']

env.user = REMOTE_USER
env.hosts = [
    REMOTE_HOST_SSH,
]
env.use_ssh_config = True
env.key_filename = '../ar_davinci.pem'
project_folder = '/home/{}/{}'.format(env.user, PROJECT_NAME)
apt_requirements = [
    'curl',
    'git',
    'python3-dev',
    'python3-pip',
    'build-essential',
    'apache2',
    'libapache2-mod-wsgi-py3',
    'python3-setuptools',
    'libssl-dev',
    'libffi-dev',
]

def new_server():
    setup()
    deploy()


def setup():
    _get_latest_apt()
    _install_apt_requirements(apt_requirements)
    _make_virtualenv()


def deploy():
    _get_latest_source()
    _put_envs()
    _update_virtualenv()
    _make_virtualhost()
    _grant_apache2()
    _restart_apache2()

def _put_envs():
    pass  # activate for envs.json file
    # put('envs.json', '~/{}/envs.json'.format(PROJECT_NAME))

def _get_latest_apt():
    update_or_not = input('would you update?: [y/n]')
    if update_or_not == 'y':
        sudo('apt-get update && apt-get -y upgrade')

def _install_apt_requirements(apt_requirements):
    reqs = ''
    for req in apt_requirements:
        reqs += (' ' + req)
    sudo('apt-get -y install {}'.format(reqs))

def _make_virtualenv():
    if not exists('~/.virtualenvs'):
        script = '''"# python virtualenv settings
                    export WORKON_HOME=~/.virtualenvs
                    export VIRTUALENVWRAPPER_PYTHON="$(command \which python3)"  # location of python3
                    source /usr/local/bin/virtualenvwrapper.sh"'''
        run('mkdir ~/.virtualenvs')
        sudo('pip3 install virtualenv virtualenvwrapper')
        run('echo {} >> ~/.bashrc'.format(script))

def _get_latest_source():
    if exists(project_folder + '/.git'):
        run('cd %s && git fetch' % (project_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, project_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (project_folder, current_commit))
    #run('cd %s && git reset --hard' % (project_folder, ))

def _update_virtualenv():
    virtualenv_folder = project_folder + '/../.virtualenvs/{}'.format(PROJECT_NAME)
    if not exists(virtualenv_folder + '/bin/pip'):
        run('cd /home/%s/.virtualenvs && virtualenv %s' % (env.user, PROJECT_NAME))
    run('%s/bin/pip install -r %s/requirements.txt' % (
        virtualenv_folder, project_folder
    ))

def _ufw_allow():
    sudo("ufw allow 'Apache Full'")
    sudo("ufw reload")

def _make_virtualhost():
    script = """'<VirtualHost *:80>
    ServerName {servername}
    <Directory /home/{username}/{project_name}>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    WSGIDaemonProcess {project_name} python-home=/home/{username}/.virtualenvs/{project_name} python-path=/home/{username}/{project_name}
    WSGIProcessGroup {project_name}
    WSGIScriptAlias / /home/{username}/{project_name}/wsgi.py
    
    ErrorLog ${{APACHE_LOG_DIR}}/error.log
    CustomLog ${{APACHE_LOG_DIR}}/access.log combined
    
    </VirtualHost>'""".format(
        username=REMOTE_USER,
        project_name=PROJECT_NAME,
        servername=REMOTE_HOST,
    )
    sudo('echo {} > /etc/apache2/sites-available/{}.conf'.format(script, PROJECT_NAME))
    sudo('a2ensite {}.conf'.format(PROJECT_NAME))

def _grant_apache2():
    sudo('chown -R :www-data ~/{}'.format(PROJECT_NAME))
    sudo('chmod -R 775 ~/{}'.format(PROJECT_NAME))

def _restart_apache2():
    sudo('sudo service apache2 restart')
```    

---

# deploy from git 
---
## 세팅절차 
1. git 새로운 저장소 생성 
    - https://github.com/jsrrykim91/deploy.git

2. 로컬 PC에서 aws폴더를 vscode 에서 오픈 
3. 터미널 오픈
4. `$ git clone https://github.com/유저아이디/deploy.git`
5. 터미널에서 경로 이동 => `cd deploy`

## 파일 세팅 (~/aws/deploy)
1. deploy.json, fabfile.py 두 파일을 deploy에 옮긴다 
2. 서버파일 생성  
3. run.py, wsgi.py 생성
4. 코드작성 
5. 배포관련 환경 변수 파일 수정(deploy.json) 

```json
// deploy.json 수정 
{
    //  깃허브 경로 
    "REPO_URL":"https://github.com/유저아이디/deploy",
    // 이름 
    "PROJECT_NAME":"이름",
    //  IPv4 :아마존 퍼플릭 도메인 - 만약 도매인 구매하면 : 아이피를 집어 넣으면 됨 
    "REMOTE_HOST":" 주소 ",
    //  IPv4 퍼블릭 IP
    "REMOTE_HOST_SSH":"IP",
    "REMOTE_USER":"ubuntu"
  }
```
---

6. requirements.txt 
    - 본서비스를 구동하기 위해 필요 

```txt
<!-- 버전정보입력 -->
flask ==  1.0.2  
```
---
## 구동 
- python3 버전 기반으로 수행 
- 운영 체계 및 서버 세팅 및 배포, 업데이트 관리등을 자동화 하는 모듈 => fabric3 => 설치 
- `$ pip3 install fabric3`

```py
#  fabfile.py 수정 
# line 24
env.use_ssh_config = True
env.key_filename = '../내파일이름.pem' # 변경
project_folder = '/home/{}/{}'.format(env.user, PROJECT_NAME)
apt_requirements = [
    'curl',
    'git',
    'python3-dev',
    'python3-pip',
    'build-essential',
    'apache2',
    'libapache2-mod-wsgi-py3',
    'python3-setuptools',
    'libssl-dev',
    'libffi-dev',
]
```
---

```bash

PS C:\Users\admin\Desktop\aws\deploy> fab new_server
[13.209.97.183] Executing task 'new_server'

Warning: Unable to load SSH config file 'C:\Users\admin\.ssh\config'

would you update?: [y/n]y

```
---

3. 브라우저 가동 : http://13.209.97.183/
    - 브라우저 접속 

4. 접속 로그 확인 (리눅스에서 진행 )
    - $ tail -f /var/log/apache2/access.log
    - 모니터링하다가 
    - 종료 : ctrl +c 
    
5. 에러 로그 
    - $ tail -f /var/log/apache2/error.log
    - 종료 : ctrl +c 

``` bash
ubuntu@ip-***:~$ ls
deploy
ubuntu@ip-***:~$ cd deploy
ubuntu@ip-***:~/deploy$ ls
README.md  deploy.json  fabfile.py  reguirements.txt  run.py  wsgi.py
ubuntu@ip-***:~/deploy$

# 로그 확인 
ubuntu@ip-***:~/deploy$ tail -f /var/log/apache2/access.log
tail: cannot open '/var/log/apache2/access.log' for reading: No such file or directory
tail: no files remaining
ubuntu@ip-***:~/deploy$ # 동작 안함 - 서버 요청이 막힘 

```
- 인바운드 룰 
- 새로 생성 
    - http -> anywhere
---
## 이후 과정 
- 업데이트 
    - `$ fab deploy`
---

## 잘 안될때 
- 소스 코드상에 , 파일 명, 설정 값등 오타가 없어야 한다. 
- git에 최종 소스코드가 올라 가있어야 한다 
- 리눅스에서 기존의 흔적을 모드 삭제 해야한다 
```
$ls -a 
$ rm -r -f .virtualenvs
- 로컬 PC
$ fab new_server
```
---

## 가상호스트가 설정된 부분 
- deploy 프로젝트 명 - json에 정의 되어 있음 
    - $ cat /etc/apache2/sites-available/deploy.conf

    ```bash
    <VirtualHost *:80>
    ServerName 13.209.97.183
    <Directory /home/ubuntu/deploy>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    WSGIDaemonProcess deploy python-home=/home/ubuntu/.virtualenvs/deploy python-path=/home/ubuntu/deploy
    WSGIProcessGroup deploy
    WSGIScriptAlias / /home/ubuntu/deploy/wsgi.py

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>
    ```
- 서버 주소 변경 
    - git 업로드

- 변경후 
    - 업데이트 
        - `$ fab deploy`
        
- 변경 됨 
#### 여기까지 배포 운영 
---