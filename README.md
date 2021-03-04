# Customizing Superset

## Features, Scoped/Customized

...
## Version Control, Project Location

- Location: https://bitbucket.org/tompkinsinc/superset.git

**Tasks**

- [x] Put Superset Project into version control
- [x] Fork Superset Project From Github
- [x] Project Loc 
- [x] Note from Moses - https://docs.github.com/en/github/using-git/adding-a-remote
- [x] Bitbucket LOC - Pick loc on Bitbucket to host our version of Superset

## Docker-Compose

**Tasks**

- [x] Setup docker network to talk to mysql database
- [x] Edit docker-compose.yml to use preexisting network
- [ ] Change implementation for dev and for prod. (Ops)

## MySQL Connector
[MySQL Connector](https://superset.apache.org/docs/databases/dockeradddrivers) Info.

**Tasks**
```bash
# from superset_app
touch ./docker/requirements-local.txt
echo "mysqlclient" >> ./docker/requirements-local.txt 
echo "pymysql" >> ./docker/requirements-local.txt

# from project
docker-compose build --force-rm
docker-compose up -d
```

## Customizing Superset (superset_config.py)

**Tasks**

- [x] SECRET_KEY
- [x] ROW_LEVEL_SECURITY=True
- [ ] Custom HTTP Port
- [ ] SQL_ALCHEMY_DATABASE_URI ... superset.db

## Change Default Admin Password

**Tasks**
- [ ] Change admin password

## Revise Branding

**Tasks**
- [ ] CSS
- [ ] Images And Animations

## Features, Additional Available
- [ ] API
- [ ] Do Not Install Examples On Prod
- [ ] docker-compose -f docker-compose-non-dev.yml up (non dev mode)
- [ ] Can do Helm/Kubernetes
- [ ] LOAD_BALANCER
- [ ] OAuth
- [ ] CORS
- [ ] Domain Sharding
- [ ] Catching RESULTS_BACKEND ... see async queries
- [ ] Celery superset/tasks/cache.py
- [ ] StatsD Logging
- [ ] Updating From Upstream
- [ ] Async If For Long Running Queries
- [ ] CELERY_CONFIG
- [ ] All REDIS Endpoint(s) ... Can leverage existing REDIS
- [ ] MySQL ... Can leverage existing MySQL
- [ ] Configure Email
- [ ] SQLite Metadata Won't Work In Cluster
- [ ] SQLLab Async If Setting In DB Settings
- [ ] Celery Flower Monitoring
- [ ] Alerts & Reports
- [ ] SQL Jinja Templates
- [ ] Country Map Tools
- [ ] Import / Export Log Data