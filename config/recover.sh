#!/bin/bash
sed -i 's/^safe_to_bootstrap: 0/safe_to_bootstrap: 1/' /var/lib/mysql/grastate.dat
sed -i 's|^wsrep_cluster_address="gcomm://172.31.25.97,172.31.31.227,172.31.26.156"|wsrep_cluster_address="gcomm://"|' /etc/my.cnf.d/server.cnf
systemctl restart mariadb
sleep 300
sed -i 's|^wsrep_cluster_address="gcomm://"|wsrep_cluster_address="gcomm://172.31.25.97,172.31.31.227,172.31.26.156"|' /etc/my.cnf.d/server.cnf
systemctl restart mariadb