datacenter = "security"
data_dir = "/opt/consul"
client_addr = "0.0.0.0"
ui_config{
  enabled = true
}
server = true
bind_addr = "0.0.0.0" # Listen on all IPv4
advertise_addr = "192.168.1.111"
bootstrap_expect=3
encrypt = "..."
retry_join = ["192.168.1.111", "192.168.1.101", "192.168.1.102", "192.168.1.103"]
 
