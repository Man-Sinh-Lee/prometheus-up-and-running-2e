#!/bin/bash
sed -i 's/^safe_to_bootstrap: 0/safe_to_bootstrap: 1/' /var/lib/mysql/grastate.dat
sed -i 's|^wsrep_cluster_address="gcomm://172.31.33.153,172.31.34.145,172.31.42.187"|wsrep_cluster_address="gcomm://"|' /etc/my.cnf.d/server.cnf
systemctl restart mariadb
sleep 300
sed -i 's|^wsrep_cluster_address="gcomm://"|wsrep_cluster_address="gcomm://172.31.33.153,172.31.34.145,172.31.42.187"|' /etc/my.cnf.d/server.cnf
systemctl restart mariadb
