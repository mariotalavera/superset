# Customizing Superset

## Features, Scoped/Customizable

- [ ] Put Superset Project into version control
  - [*] Fork Superset Project From Github
  - [*] Project Loc https://github.com/mariotalavera/superset
  - [ ] Note from Moses - https://docs.github.com/en/github/using-git/adding-a-remote
  - [ ] Bitbucket LOC - Pick loc on Bitbucket to host our version of Superset

- [ ] Runs on Docker Compose
  - [*] Setup docker network to talk to mysql database
  - [*] Edit docker-compose.yml to use preexisting network
  - [ ] Change implementation for dev and for prod. (Ops)

- [ ] Change admin password
- [ ] superset_config.py
  - [*] SECRET_KEY
  - [ ] SQL_ALCHEMY_DATABASE_URI ... superset.db
  - [ ] Custom HTTP Port
  - [*] ROW_LEVEL_SECURITY=True
- [ ] Branding
  - [ ] CSS
  - [ ] Images And Animations
- [ ] API
- [ ] Do Not Install Examples On Prod

- [*] MySQL Connector
  - https://superset.apache.org/docs/databases/dockeradddrivers
  ```bash
    # from superset_app
    touch ./docker/requirements-local.txt
    echo "mysqlclient" >> ./docker/requirements-local.txt 
    echo "pymysql" >> ./docker/requirements-local.txt
    echo "mysqlclient" >> ./docker/requirements-local.txt
    echo "pymysql" >> ./docker/requirements-local.txt
    
    # from project
    docker-compose build --force-rm
    ```

## Features, Additional Available
- [ ] docker-compose -f docker-compose-non-dev.yml up (non dev mode)
- [ ] Can do Helm/Kubernetes
- [ ] LOAD_BALANCER
- [ ] OAuth
- [ ] CORS
- [ ] Domain Sharding
- [ ] Catching RESULTS_BACKEND
  - [ ] ... see async queries
- [ ] Celery superset/tasks/cache.py
- [ ] StatsD Logging
- [ ] Updating From Upstream
- [ ] Async If For Long Running Queries
- [ ] CELERY_CONFIG
- [ ] All REDIS Endpoint(s)
  - Can leverage existing REDIS
- [ ] MySQL 
    - Can leverage existing MySQL
- [ ] Configure Email
- [ ] SQLite Metadata Won't Work In Cluster
- [ ] SQLLab Async If Setting In DB Settings
- [ ] Celery Flower Monitoring
- [ ] Alerts & Reports
- [ ] SQL Jinja Templates
- [ ] Country Map Tools
- [ ] Import / Export Log Data