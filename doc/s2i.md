# Use s2i to generate the docker image

## Download s2i 

S2 is available [here](https://github.com/openshift/source-to-image/releases/tag/v1.1.12).

## Build

```
s2i build https://github.com/sclorg/django-ex centos/python-35-centos7 hello-python
docker run -p 8080:8080 hello-python
```
