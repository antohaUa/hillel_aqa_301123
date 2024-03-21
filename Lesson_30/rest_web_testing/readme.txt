./bin/test -m "internal" --setup_cfg=configs/cfg_local.json


# to
sudo setenforce 0   # disable SELINUX
docker-compose up -d allure allure-ui

./bin/test --setup_cfg=configs/cfg_local.json --alluredir=x_allure_results