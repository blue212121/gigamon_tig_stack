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
![Screenshot 2024-06-27 at 14-10-32 Gigamon General - Dashboards - Grafana-gimped](https://github.com/blue212121/gigamon_tig_stack/assets/73847562/80eb153f-b93c-4b66-ba86-11ce5ad70aa8)
![Screenshot 2024-06-27 at 14-11-18 Gigamon Ports - Dashboards - Grafana](https://github.com/blue212121/gigamon_tig_stack/assets/73847562/10d2be55-4bde-40fe-8ac0-465062301cc9)
