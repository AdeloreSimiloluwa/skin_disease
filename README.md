# skin_disease

## How to use the web-server
<br>

- navigate to web-server folder

~~~
    cd web-server
~~~

- build docker image locally

~~~
    docker build -t [username]/[image_name] .

    eg: docker build -t jayefee/skin-disease .
~~~

- run a container

~~~
    docker run -p 8000:8000 --name container_name image_name

    e.g. docker run -p 8000:8000 --name healthbox jayefee/skin-disease
~~~

- open api on your browser

~~~
    127.0.0.1:8000/swagger
~~~