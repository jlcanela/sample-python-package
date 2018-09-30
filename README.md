# Setup the environment

```
sudo apt-get install python3-venv
python3 -m venv .env
source .env/bin/activate
pip install wheel
pip install Flask
```

# Test tool

Taurus : https://github.com/Blazemeter/taurus

Install dependency: 
```
sudo apt install python3.5-dev
```
 
Install bzt:
```
pip install bzt
```

Run tests:
```
bzt perf-test.yml -report
```

# Reference

Some urls:
* https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
* https://realpython.com/offline-python-deployments-with-docker/
* https://packaging.python.org/tutorials/packaging-projects/
* https://pypi.org/project/pip-bundle/

