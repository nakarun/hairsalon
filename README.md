# 概要
- ポイントカード機能がついた美容室用のHPをDjangoで作成してみました。
- https://sample-hair-salon.com/
- testuser: やざわ
- password: 9ijn8uhb

# Features
- サロン側の管理画面を作成します。

# カバレッジ率
```
Name                             Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------
accounts/__init__.py                 0      0      0      0   100%
accounts/admin.py                    3      0      0      0   100%
accounts/apps.py                     4      0      0      0   100%
accounts/models.py                   9      0      0      0   100%
accounts/tests.py                    1      0      0      0   100%
config/__init__.py                   1      0      0      0   100%
config/settings/base.py             32      0      0      0   100%
config/settings/local.py             5      0      0      0   100%
config/urls.py                       5      0      0      0   100%
hairsalon/__init__.py                0      0      0      0   100%
hairsalon/admin.py                   5      0      0      0   100%
hairsalon/apps.py                    4      0      0      0   100%
hairsalon/models.py                 31      3      0      0    90%
hairsalon/tests/__init__.py          0      0      0      0   100%
hairsalon/tests/test_views.py        7      0      0      0   100%
hairsalon/urls.py                    3      0      0      0   100%
hairsalon/views.py                  13      6      0      0    54%
manage.py                           15      2      2      1    82%
pointcard/__init__.py                0      0      0      0   100%
pointcard/admin.py                   9      0      0      0   100%
pointcard/apps.py                    4      0      0      0   100%
pointcard/models.py                 38      3      0      0    92%
pointcard/tests/__init__.py          0      0      0      0   100%
pointcard/tests/test_models.py      21      0      4      0   100%
pointcard/tests/test_view.py        38      0      8      0   100%
pointcard/urls.py                    3      0      0      0   100%
pointcard/views.py                  22      1      6      1    93%
------------------------------------------------------------------
TOTAL                              273     15     20      2    94%
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

# 参考一覧
- Top画像 : https://pixabay.com/ja/vectors/%e7%90%86%e5%ae%b9-haircutting-%e9%a0%ad-33118/
- Docker : https://qiita.com/str416yb/items/7324b99b9f05b9089b80
  - cryptography install : https://cryptography.io/en/latest/installation/#alpine
- SSL化 : 
  - https://github.com/SteveLTN/https-portal
- CSS : https://f-tpl.com/tpl_087/
- 現場で使えるDjangoの教科書シリーズ : https://zenn.dev/akiyoko/articles/6bc03e7f954570