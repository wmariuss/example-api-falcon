Simple REST API using falcon
----------------------------

#### py version
`3.6.1`

#### Create virtual env
* `mkdir [any_project_name]`
* `cd [any_project_name]`
* `pip install virtualenv`
* `python -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`

#### Using existing env
* `source .venv/bin/activate`

#### Run the server
* `gunicorn -b 127.0.0.1:8038 things.app` or `./run`

#### Usage
* `curl http://127.0.0.1:8083/images`
