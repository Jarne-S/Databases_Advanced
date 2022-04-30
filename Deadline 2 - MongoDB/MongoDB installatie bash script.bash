# Installeren MongoDB

$ wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

$ sudo apt update

$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

$ sudo apt-get update

$ sudo apt-get install -y mongodb-org

$ sudo systemctl start mongod

$ systemctl status mongod

$ sudo systemctl enable mongod


# Installeren MongoDB compass

$ wget https://downloads.mongodb.com/compass/mongodb-compass_1.31.1_amd64.deb

$ sudo dpkg -i mongodb-compass_1.31.1_amd64.deb

# Opstarten MongoDB compass:

$ mongodb-compass