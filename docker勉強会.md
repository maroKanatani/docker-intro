# Docker勉強会

    windows版dockerの話はしません
    Docker for macで動かしています

## コンテナとは
ひとことで言えば、アプリ部分に最適化された仮想化技術。

従来の仮想化技術に比べて省リソースで爆速に環境を作れる。

## なぜDocker?

|コマンド・ツール|役割|
|--|--|
|dockerコマンド|一つのコンテナを操作する、基礎となるコマンド|
|docker-compose|一つのアプリを構築する（単純なdockerコマンドだけで実現できないもの。複数コンテナ使用、データ永続化など）|
|dokcer-machine|Dockerを動かす仮想マシンの設定|
|kubernetes(or docker swarm)|コンテナのクラスタリングや負荷分散等のスケーリング時に使う（大規模用）|

今回はdokcerコマンドとdocker-composeの話
  

## HelloWorld

Hello Worldする前に

```
docker ps -a
```

### docker ps
現在起動しているコンテナの一覧を表示する。
(-aオプションで起動していないものも含めて表示する)

いざHello World

### docker run
dockerインスタンスの実行
```
docker run hello-world
```

MySQLのインスタンスを実行する

MySQL dockerとかで検索すると、
DockerHubにMySQLの公式イメージが見つかるので使い方を確認する

https://hub.docker.com/_/mysql

![DockerHub_MySql](./img/01.PNG "01")

設定部分をちょっと変えて実行する
```
docker run --name sample_mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```

|オプション|意味|
|--|--|
|--name|名前を付ける|
|-e|環境変数を設定する|
|-d|デタッチドモードで起動する（これ無しだと起動してコンテナが実行された後停止してしまう）|

今立てたインスタンスにsshする

```
docker exec -it sample_mysql /bin/bash 
```

入れたら
```
mysql -uroot -p
```

不要になったら
```
docker stop sample_mysql
docker rm sample_mysql
```

```
docker start sample_mysql
```

## docker-compose

docker pull


dockerコマンドでpandocを使う
dockerコマンドでDBを立てる
