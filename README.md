# DevMetrics


`python -m venv venv`

`venv/bin/activate`

`pip install -r requirements.txt`

rename `.env.example` to `.env` and paste your github token inside

`docker build -t image-name .`

`docker create --name container-name -p local-port:8000 image-name`