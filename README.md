# 美容室用のHPをDjangoで作成してみました。
- http://54.185.229.174/

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
- CSS : https://f-tpl.com/tpl_087/
- 現場で使えるDjangoの教科書シリーズ : https://zenn.dev/akiyoko/articles/6bc03e7f954570