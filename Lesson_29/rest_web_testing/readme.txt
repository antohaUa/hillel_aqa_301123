1) Correct path to your dir in ./bin/test file
2) start flask app or python http server
3) Run tests:
./bin/test -m "web_selenium" --setup_cfg=configs/cfg_local.json  # run web tests
./bin/test -m "rest_api" --setup_cfg=configs/cfg_local.json