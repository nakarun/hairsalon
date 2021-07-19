# 概要
- ポイントカード機能がついた美容室用のHPをDjangoで作成しました。
- 利用者側画面
  - https://sample-hair-salon.com/
  - testuser: 利用者太郎
  - password: 9ijn8uhb
- サロン側管理画面
  - https://sample-hair-salon.com/owner/
  - teststaff: サロンスタッフ
  - password: 9ijn8uhb

# 機能追加予定
- 

# カバレッジ率
```
Name                             Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------
accounts/__init__.py                 0      0      0      0   100%
accounts/admin.py                   32     29      0      0     9%
accounts/apps.py                     4      0      0      0   100%
accounts/models.py                  21     15      0      0    29%
accounts/tests.py                    1      0      0      0   100%
config/__init__.py                   1      0      0      0   100%
config/settings/base.py             36     18      0      0    50%
config/settings/local.py             9      4      0      0    56%
config/urls.py                       6      1      0      0    83%
hairsalon/__init__.py                0      0      0      0   100%
hairsalon/admin.py                   8      3      0      0    62%
hairsalon/apps.py                    4      0      0      0   100%
hairsalon/models.py                 25      6      0      0    76%
hairsalon/tests/__init__.py          0      0      0      0   100%
hairsalon/tests/test_views.py        7      0      0      0   100%
hairsalon/urls.py                    3      0      0      0   100%
hairsalon/views.py                  18     12      0      0    33%
manage.py                           15      2      2      1    82%
pointcard/__init__.py                0      0      0      0   100%
pointcard/admin.py                   8      0      0      0   100%
pointcard/apps.py                    4      0      0      0   100%
pointcard/models.py                 32      9      0      0    72%
pointcard/tests/__init__.py          0      0      0      0   100%
pointcard/tests/test_models.py      22      6      4      2    69%
pointcard/tests/test_view.py        39     12      8      4    66%
pointcard/urls.py                    3      0      0      0   100%
pointcard/views.py                  22      8      6      5    54%
------------------------------------------------------------------
TOTAL                              320    125     20     12    60%

```

# 環境構築

- user追加
  - sudo adduser hairsalon
  - sudo usermod -aG sudo hairsalon // sudoが実行できるようにsudoグループに所属させる
  - sudo rsync -a --chown=hairsalon ~/.ssh /home/hairsalon // SSH鍵でログインできるように設定
- git install
  - sudo apt-get install git
  - git clone https://github.com/nakarun/hairsalon.git
- docker install
  - sudo apt install apt-transport-https ca-certificates curl software-properties-common
  - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
  - sudo apt install docker-ce
  - sudo usermod -aG docker hairsalon
- docker-compose install
  - sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
  - sudo chmod +x /usr/local/bin/docker-compose
  
# Email System
- AWS SES
- 送信ログを記録 : Amazon Elasticsearch Service (Amazon ES) と Amazon Kinesis を使用
  - https://blog.serverworks.co.jp/2020/12/04/190000
  - https://blog.denet.co.jp/amazon-ses-log/
  - X-SES-CONFIGURATION-SET : これを設定しないとfirehoseにデータ送信されない
    - https://github.com/django-ses/django-ses#ses-event-monitoring-with-configuration-sets
    - https://docs.aws.amazon.com/ja_jp/ses/latest/DeveloperGuide/using-configuration-sets-in-email.html
  - サンドボックス解除は未対応

# 参考一覧
- Top画像 : https://pixabay.com/ja/vectors/%e7%90%86%e5%ae%b9-haircutting-%e9%a0%ad-33118/
- Docker : https://qiita.com/str416yb/items/7324b99b9f05b9089b80
  - cryptography install : https://cryptography.io/en/latest/installation/#alpine
- SSL化 : https://github.com/SteveLTN/https-portal
- CSS : https://f-tpl.com/tpl_087/
- 現場で使えるDjangoの教科書シリーズ : https://zenn.dev/akiyoko/articles/6bc03e7f954570
