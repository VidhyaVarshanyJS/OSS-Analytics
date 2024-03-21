# OSS-Analytics
Kibana Data Visualization using OSSInsight API to derive realtime insights of incoming data 

## Installation 
- Install python and other required packages beforehand using  `sudo apt-get python`
- Install elastic search
  '''
  sudo apt update && sudo apt upgrade
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt install elasticsearch
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch

curl localhost:9200
'''
- Install kibana
  '''
service elasticsearch restart
./elasticsearch-setup-passwords interactive
  sudo systemctl start elasticsearch
  sudo apt install kibana
    sudo systemctl start kibana
sudo systemctl status kibana

  '''
