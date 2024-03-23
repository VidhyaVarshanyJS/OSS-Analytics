# OSS-Analytics
Kibana Data Visualization using OSSInsight API to derive realtime insights of incoming data 

## Installation 
- Install python and other required packages beforehand using  `sudo apt-get python`
- Update the packages
```
  sudo apt update && sudo apt upgrade
```
- Install elasticsearch
```
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt install elasticsearch
 ```
-  Further on elastic search
```
 // in home directory 
 sudo nano etc/elasticsearch/elasticsearch.yml
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch
curl localhost:9200

# Othes
service elasticsearch restart
./elasticsearch-setup-passwords interactive
```

- Install kibana

```
sudo apt install kibana
sudo systemctl start kibana
sudo systemctl status kibana
```

## Run 
```
cd <project-dir>
start elasticsearch , enable kibana, run the python script
```


