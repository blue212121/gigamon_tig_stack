# Gigamon TIG monitor stack
## Install
- edit the data/telegraf/telegraf.conf file the management ip addresses of your monitored devices
- in the gigamon folder issue the command
```
docker compose up -d
```
-  this will automatically build a telegraf image with python installed (this is needed for the custom processors to work)
- open the grafana instance and add the influxdb as a datasource
- import the dashboards from data/grafana-dashboards/

======
tested on GigaVUE-TA10 Chassis
