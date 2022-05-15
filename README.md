# Hướng dẫn sử dụng
Docker và Magento2

## Một số yêu cầu về phần cài đặt
EC2 aws linux 2

- [Git]
```bash
+ sudo yum update -y
+ sudo yum install git -y
```

- [Docker]
```bash
+ sudo yum search docker
+ sudo yum info docker
+ sudo yum install docker
```

- [Docker-compose]
```bash
+ wget https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)
+ sudo mv docker-compose-$(uname -s)-$(uname -m) /usr/local/bin/docker-compose
+ sudo chmod -v +x /usr/local/bin/docker-compose
+ sudo systemctl enable docker.service
+ sudo systemctl start docker.service
```
## Docker

Các service mà sử dụng trong docker

    nginx
    php7.4-fpm
    mysql
    redis
    elasticsearch

Build docker bằng lệnh

```bash
docker-compose up --build
sudo chown -R 1000:root data/elasticsearch/
docker-compose up -d
docker-compose ps
```

Import database
```bash
docker exec -it tmdt_mysql bash
mysql -u root -p magento2 < database.sql
exit
```

Deploy project
```bash
docker exec -it tmdt bash
php bin/magento module:disable Magento_TwoFactorAuth
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

Check uri admin
```bash
php bin/magento info:adminuri ->> {adminuri}
```

Fix 404 page admin
```bash
php bin/magento cache:clean
rm -rf var/cache/*
rm -rf var/generation/*
chmod -R 777 var/ generated/
```

Add && update module (add module into app/code/)
```bash
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```