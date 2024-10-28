● run-credentials-systemd\x2dtmpfiles\x2dsetup\x2ddev.service.mount - /run/credentials/systemd-tmpfiles-setup-dev.service
     Loaded: loaded (/proc/self/mountinfo)
     Active: active (mounted) since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:12 +07; 2h 34min ago
      Where: /run/credentials/systemd-tmpfiles-setup-dev.service
       What: none

● -.slice - Root Slice
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:50:57 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:50:57 +07; 2h 34min ago
       Docs: man:systemd.special(7)
      Tasks: 287
     Memory: 1.1G
        CPU: 38min 51.390s
     CGroup: /
             ├─init.scope
             │ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 31
             ├─system.slice
             │ ├─NetworkManager.service
             │ │ └─651 /usr/sbin/NetworkManager --no-daemon
             │ ├─alertmanager.service
             │ │ └─664 /usr/bin/alertmanager --config.file=/etc/prometheus/alertmanager.yml --storage.path=/var/lib/prometheus/alertmanager
             │ ├─auditd.service
             │ │ └─589 /sbin/auditd
             │ ├─blackbox_exporter.service
             │ │ └─668 /usr/bin/blackbox_exporter --config.file=/etc/prometheus/blackbox.yml
             │ ├─chronyd.service
             │ │ └─629 /usr/sbin/chronyd -F 2
             │ ├─containerd.service
             │ │ └─691 /usr/bin/containerd
             │ ├─crond.service
             │ │ └─868 /usr/sbin/crond -n
             │ ├─dbus-broker.service
             │ │ ├─612 /usr/bin/dbus-broker-launch --scope system --audit
             │ │ └─616 dbus-broker --log 4 --controller 9 --machine-id ec20f5ba53a6e950674ad204defd7591 --max-bytes 536870912 --max-fds 4096 --max-matches 131072 --audit
             │ ├─docker.service
             │ │ └─938 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
             │ ├─grafana-server.service
             │ │ └─1087 /usr/share/grafana/bin/grafana server --config=/etc/grafana/grafana.ini --pidfile=/var/run/grafana/grafana-server.pid --packaging=rpm cfg:default.paths.logs=/var/log/grafana cfg:default.paths.data=/var/lib/grafana cfg:default.paths.plugins=/var/lib/grafana/plugins cfg:default.paths.provisioning=/etc/grafana/provisioning
             │ ├─grok_exporter.service
             │ │ └─672 /usr/local/bin/grok_exporter -config=/etc/grok_exporter/config.yml
             │ ├─influxdb.service
             │ │ └─829 /usr/bin/influxd -config /etc/influxdb/influxdb.conf
             │ ├─influxdb_exporter.service
             │ │ └─684 /usr/bin/influxdb_exporter
             │ ├─irqbalance.service
             │ │ └─619 /usr/sbin/irqbalance --foreground
             │ ├─mysqld_exporter.service
             │ │ └─685 /usr/bin/mysqld_exporter --config.my-cnf /etc/my.cnf.d/client.cnf --collect.global_status --collect.info_schema.innodb_metrics --collect.auto_increment.columns --collect.info_schema.processlist --collect.binlog_size --collect.info_schema.tablestats --collect.global_variables --collect.info_schema.query_response_time --collect.info_schema.userstats --collect.info_schema.tables --collect.perf_schema.tablelocks --collect.perf_schema.file_events --collect.perf_schema.eventswaits --collect.perf_schema.indexiowaits --collect.perf_schema.tableiowaits --collect.slave_status --web.listen-address=0.0.0.0:9104
             │ ├─node_exporter.service
             │ │ └─687 /usr/bin/node_exporter
             │ ├─polkit.service
             │ │ └─826 /usr/lib/polkit-1/polkitd --no-debug
             │ ├─prometheus.service
             │ │ └─688 /usr/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/var/lib/prometheus/data --web.console.libraries=/usr/share/prometheus/console_libraries --web.console.templates=/usr/share/prometheus/consoles --web.config.file=/etc/prometheus/web.yml
             │ ├─pushgateway.service
             │ │ └─689 /usr/bin/pushgateway
             │ ├─rngd.service
             │ │ └─620 /usr/sbin/rngd -f --fill-watermark=0 -x pkcs11 -x nist -x qrypt -D daemon:daemon
             │ ├─rsyslog.service
             │ │ └─822 /usr/sbin/rsyslogd -n
             │ ├─sshd.service
             │ │ └─823 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
             │ ├─system-getty.slice
             │ │ └─getty@tty1.service
             │ │   └─869 /sbin/agetty -o "-p -- \\u" --noclear - linux
             │ ├─system-serial\x2dgetty.slice
             │ │ └─serial-getty@ttyS0.service
             │ │   └─870 /sbin/agetty -o "-p -- \\u" --keep-baud 115200,57600,38400,9600 - vt220
             │ ├─systemd-journald.service
             │ │ └─519 /usr/lib/systemd/systemd-journald
             │ ├─systemd-logind.service
             │ │ └─621 /usr/lib/systemd/systemd-logind
             │ ├─systemd-udevd.service
             │ │ └─udev
             │ │   └─536 /usr/lib/systemd/systemd-udevd
             │ ├─telegraf.service
             │ │ └─824 /usr/bin/telegraf -config /etc/telegraf/telegraf.conf -config-directory /etc/telegraf/telegraf.d
             │ ├─telegrafv2.service
             │ │ └─825 /usr/bin/telegraf --config http://4225a859241c.mylabserver.com:8086/api/v2/telegrafs/0dca759669f3c000
             │ └─tuned.service
             │   └─690 /usr/bin/python3 -Es /usr/sbin/tuned -l -P
             └─user.slice
               └─user-1000.slice
                 ├─session-8.scope
                 │ ├─ 2144 "sshd: man-sinh-lee [priv]"
                 │ ├─ 2146 "sshd: man-sinh-lee@notty"
                 │ ├─ 2147 -bash
                 │ ├─ 2169 sh
                 │ ├─ 2187 /home/man-sinh-lee/.vscode-server/code-384ff7382de624fb94dbaf6da11977bba1ecd427 command-shell --cli-data-dir /home/man-sinh-lee/.vscode-server/cli --parent-process-id 2169 --on-host=127.0.0.1 --on-port
                 │ ├─ 2221 sh /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/bin/code-server --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
                 │ ├─ 2225 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/server-main.js --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
                 │ ├─ 2258 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node --dns-result-order=ipv4first /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
                 │ ├─ 2269 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=ptyHost --logsPath /home/man-sinh-lee/.vscode-server/data/logs/20241011T185424
                 │ ├─ 8905 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
                 │ ├─17899 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
                 │ ├─23310 sleep 180
                 │ ├─23637 /bin/bash /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/base/node/cpuUsage.sh 8905
                 │ ├─23640 sleep 1
                 │ └─23642 systemctl status "*" --no-pager -l
                 └─user@1000.service
                   └─init.scope
                     ├─1644 /usr/lib/systemd/systemd --user
                     └─1645 "(sd-pam)"

Oct 11 21:22:20 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:23:20 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:23:20 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:23:30 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:24:26 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:24:26 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:24:36 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:25:36 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:25:36 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:25:46 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.

● swap.target - Swaps
     Loaded: loaded (/usr/lib/systemd/system/swap.target; static)
     Active: active since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Reached target Swaps.

● NetworkManager-wait-online.service - Network Manager Wait Online
     Loaded: loaded (/usr/lib/systemd/system/NetworkManager-wait-online.service; enabled; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:29 +07; 2h 34min ago
       Docs: man:NetworkManager-wait-online.service(8)
   Main PID: 663 (code=exited, status=0/SUCCESS)
        CPU: 22ms

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Wait Online...
Oct 11 18:51:29 4225a859241c.mylabserver.com systemd[1]: Finished Network Manager Wait Online.

● sys-devices-platform-serial8250-tty-ttyS3.device - /sys/devices/platform/serial8250/tty/ttyS3
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/platform/serial8250/tty/ttyS3

● getty@tty1.service - Getty on tty1
     Loaded: loaded (/usr/lib/systemd/system/getty@.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:agetty(8)
             man:systemd-getty-generator(8)
             http://0pointer.de/blog/projects/serial-console.html
   Main PID: 869 (agetty)
      Tasks: 1 (limit: 24437)
     Memory: 204.0K
        CPU: 142ms
     CGroup: /system.slice/system-getty.slice/getty@tty1.service
             └─869 /sbin/agetty -o "-p -- \\u" --noclear - linux

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Started Getty on tty1.

● certbot-renew.timer - This is the timer to set the schedule for automated renewals
     Loaded: loaded (/usr/lib/systemd/system/certbot-renew.timer; enabled; preset: enabled)
     Active: active (waiting) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
    Trigger: Sat 2024-10-12 06:50:06 +07; 9h left
   Triggers: ● certbot-renew.service

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started This is the timer to set the schedule for automated renewals.

● lvm2-lvmpolld.socket - LVM2 poll daemon socket
     Loaded: loaded (/usr/lib/systemd/system/lvm2-lvmpolld.socket; enabled; preset: enabled)
     Active: active (listening) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● lvm2-lvmpolld.service
       Docs: man:lvmpolld(8)
     Listen: /run/lvm/lvmpolld.socket (Stream)
     CGroup: /system.slice/lvm2-lvmpolld.socket

● user-1000.slice - User Slice of UID 1000
     Loaded: loaded
    Drop-In: /usr/lib/systemd/system/user-.slice.d
             └─10-defaults.conf
     Active: active since Fri 2024-10-11 18:53:02 +07; 2h 32min ago
      Until: Fri 2024-10-11 18:53:02 +07; 2h 32min ago
       Docs: man:user@.service(5)
      Tasks: 52 (limit: 10080)
     Memory: 1.4G
        CPU: 6min 8.808s
     CGroup: /user.slice/user-1000.slice
             ├─session-8.scope
             │ ├─ 2144 "sshd: man-sinh-lee [priv]"
             │ ├─ 2146 "sshd: man-sinh-lee@notty"
             │ ├─ 2147 -bash
             │ ├─ 2169 sh
             │ ├─ 2187 /home/man-sinh-lee/.vscode-server/code-384ff7382de624fb94dbaf6da11977bba1ecd427 command-shell --cli-data-dir /home/man-sinh-lee/.vscode-server/cli --parent-process-id 2169 --on-host=127.0.0.1 --on-port
             │ ├─ 2221 sh /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/bin/code-server --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
             │ ├─ 2225 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/server-main.js --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
             │ ├─ 2258 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node --dns-result-order=ipv4first /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
             │ ├─ 2269 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=ptyHost --logsPath /home/man-sinh-lee/.vscode-server/data/logs/20241011T185424
             │ ├─ 8905 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
             │ ├─17899 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
             │ ├─23310 sleep 180
             │ ├─23637 /bin/bash /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/base/node/cpuUsage.sh 8905
             │ ├─23640 sleep 1
             │ └─23642 systemctl status "*" --no-pager -l
             └─user@1000.service
               └─init.scope
                 ├─1644 /usr/lib/systemd/systemd --user
                 └─1645 "(sd-pam)"

Oct 11 21:22:51 4225a859241c.mylabserver.com sudo[23005]: pam_unix(sudo:session): session closed for user root
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee ; USER=root ; COMMAND=/bin/systemctl cat elasticsearch-in-action-2e-2023 learn-grafana-10 prometheus-up-and-running-2e
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: pam_unix(sudo:session): session closed for user root
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee/prometheus-up-and-running-2e ; USER=root ; COMMAND=/bin/chown -R . man-sinh-lee
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: pam_unix(sudo:session): session closed for user root
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee ; USER=root ; COMMAND=/bin/chown man-sinh-lee: . -R
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: pam_unix(sudo:session): session closed for user root

● sys-kernel-config.mount - Kernel Configuration File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /sys/kernel/config
       What: configfs
       Docs: https://docs.kernel.org/filesystems/configfs.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 2ms
     CGroup: /sys-kernel-config.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounting Kernel Configuration File System...
Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted Kernel Configuration File System.

● docker.socket - Docker Socket for the API
     Loaded: loaded (/usr/lib/systemd/system/docker.socket; disabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
   Triggers: ● docker.service
     Listen: /run/docker.sock (Stream)
      Tasks: 0 (limit: 24437)
     Memory: 0B
        CPU: 1ms
     CGroup: /system.slice/docker.socket

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Starting Docker Socket for the API...
Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Listening on Docker Socket for the API.

● chronyd.service - NTP client/server
     Loaded: loaded (/usr/lib/systemd/system/chronyd.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:18 +07; 2h 34min ago
       Docs: man:chronyd(8)
             man:chrony.conf(5)
   Main PID: 629 (chronyd)
      Tasks: 1 (limit: 24437)
     Memory: 3.0M
        CPU: 102ms
     CGroup: /system.slice/chronyd.service
             └─629 /usr/sbin/chronyd -F 2

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Starting NTP client/server...
Oct 11 18:51:18 4225a859241c.mylabserver.com chronyd[629]: chronyd version 4.5 starting (+CMDMON +NTP +REFCLOCK +RTC +PRIVDROP +SCFILTER +SIGND +ASYNCDNS +NTS +SECHASH +IPV6 +DEBUG)
Oct 11 18:51:18 4225a859241c.mylabserver.com chronyd[629]: Loaded 0 symmetric keys
Oct 11 18:51:18 4225a859241c.mylabserver.com chronyd[629]: Frequency -13.822 +/- 0.335 ppm read from /var/lib/chrony/chrony.drift
Oct 11 18:51:18 4225a859241c.mylabserver.com chronyd[629]: Using right/UTC timezone to obtain leap second data
Oct 11 18:51:18 4225a859241c.mylabserver.com chronyd[629]: Loaded seccomp filter (level 2)
Oct 11 18:51:18 4225a859241c.mylabserver.com systemd[1]: Started NTP client/server.
Oct 11 18:51:32 4225a859241c.mylabserver.com chronyd[629]: Selected source 169.254.169.123
Oct 11 18:51:32 4225a859241c.mylabserver.com chronyd[629]: System clock TAI offset set to 37 seconds

● sys-subsystem-net-devices-eth0.device - Elastic Network Adapter (ENA)
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:05.0/net/eth0

● dnf-makecache.timer - dnf makecache --timer
     Loaded: loaded (/usr/lib/systemd/system/dnf-makecache.timer; enabled; preset: enabled)
     Active: active (waiting) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
    Trigger: Fri 2024-10-11 22:28:07 +07; 1h 2min left
   Triggers: ● dnf-makecache.service

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started dnf makecache --timer.

● systemd-ask-password-console.path - Dispatch Password Requests to Console Directory Watch
     Loaded: loaded (/usr/lib/systemd/system/systemd-ask-password-console.path; static)
     Active: active (waiting) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● systemd-ask-password-console.service
       Docs: man:systemd-ask-password-console.path(8)

● kmod-static-nodes.service - Create List of Static Device Nodes
     Loaded: loaded (/usr/lib/systemd/system/kmod-static-nodes.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
   Main PID: 513 (code=exited, status=0/SUCCESS)
        CPU: 3ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Create List of Static Device Nodes.

● system.slice - System Slice
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:50:57 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:50:57 +07; 2h 34min ago
       Docs: man:systemd.special(7)
      Tasks: 153
     Memory: 1.2G
        CPU: 28min 31.811s
     CGroup: /system.slice
             ├─NetworkManager.service
             │ └─651 /usr/sbin/NetworkManager --no-daemon
             ├─alertmanager.service
             │ └─664 /usr/bin/alertmanager --config.file=/etc/prometheus/alertmanager.yml --storage.path=/var/lib/prometheus/alertmanager
             ├─auditd.service
             │ └─589 /sbin/auditd
             ├─blackbox_exporter.service
             │ └─668 /usr/bin/blackbox_exporter --config.file=/etc/prometheus/blackbox.yml
             ├─chronyd.service
             │ └─629 /usr/sbin/chronyd -F 2
             ├─containerd.service
             │ └─691 /usr/bin/containerd
             ├─crond.service
             │ └─868 /usr/sbin/crond -n
             ├─dbus-broker.service
             │ ├─612 /usr/bin/dbus-broker-launch --scope system --audit
             │ └─616 dbus-broker --log 4 --controller 9 --machine-id ec20f5ba53a6e950674ad204defd7591 --max-bytes 536870912 --max-fds 4096 --max-matches 131072 --audit
             ├─docker.service
             │ └─938 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
             ├─grafana-server.service
             │ └─1087 /usr/share/grafana/bin/grafana server --config=/etc/grafana/grafana.ini --pidfile=/var/run/grafana/grafana-server.pid --packaging=rpm cfg:default.paths.logs=/var/log/grafana cfg:default.paths.data=/var/lib/grafana cfg:default.paths.plugins=/var/lib/grafana/plugins cfg:default.paths.provisioning=/etc/grafana/provisioning
             ├─grok_exporter.service
             │ └─672 /usr/local/bin/grok_exporter -config=/etc/grok_exporter/config.yml
             ├─influxdb.service
             │ └─829 /usr/bin/influxd -config /etc/influxdb/influxdb.conf
             ├─influxdb_exporter.service
             │ └─684 /usr/bin/influxdb_exporter
             ├─irqbalance.service
             │ └─619 /usr/sbin/irqbalance --foreground
             ├─mysqld_exporter.service
             │ └─685 /usr/bin/mysqld_exporter --config.my-cnf /etc/my.cnf.d/client.cnf --collect.global_status --collect.info_schema.innodb_metrics --collect.auto_increment.columns --collect.info_schema.processlist --collect.binlog_size --collect.info_schema.tablestats --collect.global_variables --collect.info_schema.query_response_time --collect.info_schema.userstats --collect.info_schema.tables --collect.perf_schema.tablelocks --collect.perf_schema.file_events --collect.perf_schema.eventswaits --collect.perf_schema.indexiowaits --collect.perf_schema.tableiowaits --collect.slave_status --web.listen-address=0.0.0.0:9104
             ├─node_exporter.service
             │ └─687 /usr/bin/node_exporter
             ├─polkit.service
             │ └─826 /usr/lib/polkit-1/polkitd --no-debug
             ├─prometheus.service
             │ └─688 /usr/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/var/lib/prometheus/data --web.console.libraries=/usr/share/prometheus/console_libraries --web.console.templates=/usr/share/prometheus/consoles --web.config.file=/etc/prometheus/web.yml
             ├─pushgateway.service
             │ └─689 /usr/bin/pushgateway
             ├─rngd.service
             │ └─620 /usr/sbin/rngd -f --fill-watermark=0 -x pkcs11 -x nist -x qrypt -D daemon:daemon
             ├─rsyslog.service
             │ └─822 /usr/sbin/rsyslogd -n
             ├─sshd.service
             │ └─823 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
             ├─system-getty.slice
             │ └─getty@tty1.service
             │   └─869 /sbin/agetty -o "-p -- \\u" --noclear - linux
             ├─system-serial\x2dgetty.slice
             │ └─serial-getty@ttyS0.service
             │   └─870 /sbin/agetty -o "-p -- \\u" --keep-baud 115200,57600,38400,9600 - vt220
             ├─systemd-journald.service
             │ └─519 /usr/lib/systemd/systemd-journald
             ├─systemd-logind.service
             │ └─621 /usr/lib/systemd/systemd-logind
             ├─systemd-udevd.service
             │ └─udev
             │   └─536 /usr/lib/systemd/systemd-udevd
             ├─telegraf.service
             │ └─824 /usr/bin/telegraf -config /etc/telegraf/telegraf.conf -config-directory /etc/telegraf/telegraf.d
             ├─telegrafv2.service
             │ └─825 /usr/bin/telegraf --config http://4225a859241c.mylabserver.com:8086/api/v2/telegrafs/0dca759669f3c000
             └─tuned.service
               └─690 /usr/bin/python3 -Es /usr/sbin/tuned -l -P

Oct 11 21:25:36 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656736.7784] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:25:36 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:36.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:25:41 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:41Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:41 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:41Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:41 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:41 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" b1c2c6d3-87dc-11ef-83a6-0a816498216b 12193
Oct 11 21:25:51 4225a859241c.mylabserver.com sshd[23620]: Connection closed by 172.31.42.197 port 42806 [preauth]
Oct 11 21:25:51 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:51Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:51 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:51Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:51 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:51 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" b7b8b5f8-87dc-11ef-83a7-0a816498216b 12742
Oct 11 21:25:51 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:51.807Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"

● local-fs.target - Local File Systems
     Loaded: loaded (/usr/lib/systemd/system/local-fs.target; static)
     Active: active since Fri 2024-10-11 18:51:15 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:15 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Reached target Local File Systems.

● sysinit.target - System Initialization
     Loaded: loaded (/usr/lib/systemd/system/sysinit.target; static)
     Active: active since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Reached target System Initialization.

● serial-getty@ttyS0.service - Serial Getty on ttyS0
     Loaded: loaded (/usr/lib/systemd/system/serial-getty@.service; enabled-runtime; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:agetty(8)
             man:systemd-getty-generator(8)
             http://0pointer.de/blog/projects/serial-console.html
   Main PID: 870 (agetty)
      Tasks: 1 (limit: 24437)
     Memory: 284.0K
        CPU: 3ms
     CGroup: /system.slice/system-serial\x2dgetty.slice/serial-getty@ttyS0.service
             └─870 /sbin/agetty -o "-p -- \\u" --keep-baud 115200,57600,38400,9600 - vt220

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Started Serial Getty on ttyS0.

● sys-devices-pci0000:00-0000:00:04.0-nvme-nvme0-nvme0n1.device - Amazon Elastic Block Store
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:04.0/nvme/nvme0/nvme0n1

● user.slice - User and Session Slice
     Loaded: loaded (/usr/lib/systemd/system/user.slice; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)
      Tasks: 52
     Memory: 1.4G
        CPU: 6min 9.464s
     CGroup: /user.slice
             └─user-1000.slice
               ├─session-8.scope
               │ ├─ 2144 "sshd: man-sinh-lee [priv]"
               │ ├─ 2146 "sshd: man-sinh-lee@notty"
               │ ├─ 2147 -bash
               │ ├─ 2169 sh
               │ ├─ 2187 /home/man-sinh-lee/.vscode-server/code-384ff7382de624fb94dbaf6da11977bba1ecd427 command-shell --cli-data-dir /home/man-sinh-lee/.vscode-server/cli --parent-process-id 2169 --on-host=127.0.0.1 --on-port
               │ ├─ 2221 sh /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/bin/code-server --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
               │ ├─ 2225 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/server-main.js --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
               │ ├─ 2258 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node --dns-result-order=ipv4first /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
               │ ├─ 2269 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=ptyHost --logsPath /home/man-sinh-lee/.vscode-server/data/logs/20241011T185424
               │ ├─ 8905 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
               │ ├─17899 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
               │ ├─23310 sleep 180
               │ ├─23637 /bin/bash /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/base/node/cpuUsage.sh 8905
               │ ├─23640 sleep 1
               │ └─23642 systemctl status "*" --no-pager -l
               └─user@1000.service
                 └─init.scope
                   ├─1644 /usr/lib/systemd/systemd --user
                   └─1645 "(sd-pam)"

● nis-domainname.service - Read and set NIS domainname from /etc/sysconfig/network
     Loaded: loaded (/usr/lib/systemd/system/nis-domainname.service; enabled; preset: enabled)
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
   Main PID: 518 (code=exited, status=0/SUCCESS)
        CPU: 3ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Read and set NIS domainname from /etc/sysconfig/network.

● systemd-user-sessions.service - Permit User Sessions
     Loaded: loaded (/usr/lib/systemd/system/systemd-user-sessions.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:systemd-user-sessions.service(8)
   Main PID: 866 (code=exited, status=0/SUCCESS)
        CPU: 6ms

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Starting Permit User Sessions...
Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Finished Permit User Sessions.

● systemd-tmpfiles-setup-dev.service - Create Static Device Nodes in /dev
     Loaded: loaded (/usr/lib/systemd/system/systemd-tmpfiles-setup-dev.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:tmpfiles.d(5)
             man:systemd-tmpfiles(8)
   Main PID: 534 (code=exited, status=0/SUCCESS)
        CPU: 13ms

Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Starting Create Static Device Nodes in /dev...
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd-tmpfiles[534]: /usr/lib/tmpfiles.d/elasticsearch.conf:1: Line references path below legacy directory /var/run/, updating /var/run/elasticsearch → /run/elasticsearch; please update the tmpfiles.d/ drop-in file accordingly.
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Finished Create Static Device Nodes in /dev.

● telegraf.service - Telegraf
     Loaded: loaded (/usr/lib/systemd/system/telegraf.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:50 +07; 2h 34min ago
       Docs: https://github.com/influxdata/telegraf
   Main PID: 824 (telegraf)
      Tasks: 11 (limit: 24437)
     Memory: 73.7M
        CPU: 31.685s
     CGroup: /system.slice/telegraf.service
             └─824 /usr/bin/telegraf -config /etc/telegraf/telegraf.conf -config-directory /etc/telegraf/telegraf.d

Oct 11 18:51:50 4225a859241c.mylabserver.com telegraf[824]: 2024-10-11T11:51:50Z I! Loaded secretstores:
Oct 11 18:51:50 4225a859241c.mylabserver.com telegraf[824]: 2024-10-11T11:51:50Z I! Loaded outputs: influxdb
Oct 11 18:51:50 4225a859241c.mylabserver.com telegraf[824]: 2024-10-11T11:51:50Z I! Tags enabled: host=4225a859241c.mylabserver.com
Oct 11 18:51:50 4225a859241c.mylabserver.com telegraf[824]: 2024-10-11T11:51:50Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"4225a859241c.mylabserver.com", Flush Interval:10s
Oct 11 18:51:50 4225a859241c.mylabserver.com systemd[1]: Started Telegraf.
Oct 11 20:16:38 4225a859241c.mylabserver.com systemd[1]: /usr/lib/systemd/system/telegraf.service:12: Unknown key name 'ImportCredential' in section 'Service', ignoring.
Oct 11 20:22:28 4225a859241c.mylabserver.com systemd[1]: /usr/lib/systemd/system/telegraf.service:12: Unknown key name 'ImportCredential' in section 'Service', ignoring.
Oct 11 20:35:42 4225a859241c.mylabserver.com systemd[1]: /usr/lib/systemd/system/telegraf.service:12: Unknown key name 'ImportCredential' in section 'Service', ignoring.
Oct 11 20:37:34 4225a859241c.mylabserver.com systemd[1]: /usr/lib/systemd/system/telegraf.service:12: Unknown key name 'ImportCredential' in section 'Service', ignoring.
Oct 11 21:17:06 4225a859241c.mylabserver.com systemd[1]: /usr/lib/systemd/system/telegraf.service:12: Unknown key name 'ImportCredential' in section 'Service', ignoring.

● node_exporter.service - Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.
     Loaded: loaded (/usr/lib/systemd/system/node_exporter.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://github.com/prometheus/node_exporter
   Main PID: 687 (node_exporter)
      Tasks: 6 (limit: 24437)
     Memory: 16.9M
        CPU: 34.747s
     CGroup: /system.slice/node_exporter.service
             └─687 /usr/bin/node_exporter

Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=time
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=timex
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=udp_queues
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=uname
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=vmstat
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=watchdog
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=xfs
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.306Z caller=node_exporter.go:118 level=info collector=zfs
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.409Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9100
Oct 11 18:51:30 4225a859241c.mylabserver.com node_exporter[687]: ts=2024-10-11T11:51:30.409Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9100

● systemd-random-seed.service - Load/Save OS Random Seed
     Loaded: loaded (/usr/lib/systemd/system/systemd-random-seed.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:systemd-random-seed.service(8)
             man:random(4)
   Main PID: 533 (code=exited, status=0/SUCCESS)
        CPU: 7ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Starting Load/Save OS Random Seed...
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Finished Load/Save OS Random Seed.

● run-credentials-systemd\x2dsysctl.service.mount - /run/credentials/systemd-sysctl.service
     Loaded: loaded (/proc/self/mountinfo)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /run/credentials/systemd-sysctl.service
       What: none

● dev-hugepages.mount - Huge Pages File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /dev/hugepages
       What: hugetlbfs
       Docs: https://docs.kernel.org/admin-guide/mm/hugetlbpage.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 52.0K
        CPU: 2ms
     CGroup: /dev-hugepages.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted Huge Pages File System.

● prometheus.service - The Prometheus monitoring system and time series database.
     Loaded: loaded (/usr/lib/systemd/system/prometheus.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://prometheus.io
   Main PID: 688 (prometheus)
      Tasks: 8 (limit: 24437)
     Memory: 118.3M
        CPU: 59.929s
     CGroup: /system.slice/prometheus.service
             └─688 /usr/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/var/lib/prometheus/data --web.console.libraries=/usr/share/prometheus/console_libraries --web.console.templates=/usr/share/prometheus/consoles --web.config.file=/etc/prometheus/web.yml

Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.715Z caller=main.go:1172 level=info msg="TSDB started"
Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.715Z caller=main.go:1354 level=info msg="Loading configuration file" filename=/etc/prometheus/prometheus.yml
Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.717Z caller=main.go:1391 level=info msg="updated GOGC" old=100 new=75
Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.717Z caller=main.go:1402 level=info msg="Completed loading of configuration file" filename=/etc/prometheus/prometheus.yml totalDuration=2.410446ms db_storage=1.32µs remote_storage=1.98µs web_handler=740ns query_engine=1.4µs scrape=439.017µs scrape_sd=444.426µs notify=39.763µs notify_sd=50.343µs rules=23.261µs tracing=6.061µs
Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.717Z caller=main.go:1133 level=info msg="Server is ready to receive web requests."
Oct 11 18:51:42 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T11:51:42.717Z caller=manager.go:164 level=info component="rule manager" msg="Starting rule manager..."
Oct 11 20:00:10 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T13:00:10.023Z caller=compact.go:576 level=info component=tsdb msg="write block" mint=1728640800000 maxt=1728648000000 ulid=01J9XTMGP1CKB3AN990CEFXKA8 duration=1.253260987s ooo=false
Oct 11 20:00:10 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T13:00:10.184Z caller=head.go:1355 level=info component=tsdb msg="Head GC completed" caller=truncateMemory duration=133.864186ms
Oct 11 20:00:10 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T13:00:10.198Z caller=checkpoint.go:101 level=info component=tsdb msg="Creating checkpoint" from_segment=74 to_segment=75 mint=1728648000000
Oct 11 20:00:11 4225a859241c.mylabserver.com prometheus[688]: ts=2024-10-11T13:00:11.100Z caller=head.go:1317 level=info component=tsdb msg="WAL checkpoint complete" first=74 last=75 duration=908.276824ms

● sockets.target - Socket Units
     Loaded: loaded (/usr/lib/systemd/system/sockets.target; static)
     Active: active since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Reached target Socket Units.

● -.mount - Root Mount
     Loaded: loaded (/etc/fstab; generated)
     Active: active (mounted)
      Where: /
       What: /dev/nvme0n1p2
       Docs: man:fstab(5)
             man:systemd-fstab-generator(8)

● sys-devices-pci0000:00-0000:00:1f.0-nvme-nvme2-nvme2n1.device - Amazon Elastic Block Store
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:1f.0/nvme/nvme2/nvme2n1

● sys-module-fuse.device - /sys/module/fuse
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/module/fuse

Oct 11 18:50:57 localhost systemd[1]: sys-module-fuse.device: Failed to enqueue SYSTEMD_WANTS= job, ignoring: Unit sys-fs-fuse-connections.mount not found.

● systemd-logind.service - User Login Management
     Loaded: loaded (/usr/lib/systemd/system/systemd-logind.service; static)
    Drop-In: /usr/lib/systemd/system/systemd-logind.service.d
             └─10-grub2-logind-service.conf
     Active: active (running) since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
       Docs: man:sd-login(3)
             man:systemd-logind.service(8)
             man:logind.conf(5)
             man:org.freedesktop.login1(5)
   Main PID: 621 (systemd-logind)
     Status: "Processing requests..."
      Tasks: 1 (limit: 24437)
     Memory: 2.0M
        CPU: 332ms
     CGroup: /system.slice/systemd-logind.service
             └─621 /usr/lib/systemd/systemd-logind

Oct 11 20:23:29 4225a859241c.mylabserver.com systemd-logind[621]: Removed session 19.
Oct 11 20:35:40 4225a859241c.mylabserver.com systemd-logind[621]: New session 20 of user man-sinh-lee.
Oct 11 20:37:02 4225a859241c.mylabserver.com systemd-logind[621]: Session 20 logged out. Waiting for processes to exit.
Oct 11 20:37:02 4225a859241c.mylabserver.com systemd-logind[621]: Removed session 20.
Oct 11 20:39:20 4225a859241c.mylabserver.com systemd-logind[621]: New session 21 of user man-sinh-lee.
Oct 11 20:40:23 4225a859241c.mylabserver.com systemd-logind[621]: Session 21 logged out. Waiting for processes to exit.
Oct 11 20:40:23 4225a859241c.mylabserver.com systemd-logind[621]: Removed session 21.
Oct 11 21:11:20 4225a859241c.mylabserver.com systemd-logind[621]: New session 22 of user man-sinh-lee.
Oct 11 21:12:22 4225a859241c.mylabserver.com systemd-logind[621]: Session 22 logged out. Waiting for processes to exit.
Oct 11 21:12:22 4225a859241c.mylabserver.com systemd-logind[621]: Removed session 22.

● system-getty.slice - Slice /system/getty
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Tasks: 1
     Memory: 212.0K
        CPU: 142ms
     CGroup: /system.slice/system-getty.slice
             └─getty@tty1.service
               └─869 /sbin/agetty -o "-p -- \\u" --noclear - linux

● systemd-udevd-control.socket - udev Control Socket
     Loaded: loaded (/usr/lib/systemd/system/systemd-udevd-control.socket; static)
     Active: active (running) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● systemd-udevd.service
       Docs: man:systemd-udevd-control.socket(8)
             man:udev(7)
     Listen: /run/udev/control (SequentialPacket)
     CGroup: /system.slice/systemd-udevd-control.socket

● systemd-journald.socket - Journal Socket
     Loaded: loaded (/usr/lib/systemd/system/systemd-journald.socket; static)
     Active: active (running) since Fri 2024-10-11 18:50:57 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:50:57 +07; 2h 34min ago
   Triggers: ● systemd-journald.service
       Docs: man:systemd-journald.service(8)
             man:journald.conf(5)
     Listen: /run/systemd/journal/socket (Datagram)
             /run/systemd/journal/stdout (Stream)
     CGroup: /system.slice/systemd-journald.socket

Notice: journal has been rotated since unit was started, output may be incomplete.

● sys-devices-pci0000:00-0000:00:05.0-net-eth0.device - Elastic Network Adapter (ENA)
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:05.0/net/eth0

● systemd-sysctl.service - Apply Kernel Variables
     Loaded: loaded (/usr/lib/systemd/system/systemd-sysctl.service; static)
     Active: active (exited) since Fri 2024-10-11 21:16:49 +07; 9min ago
       Docs: man:systemd-sysctl.service(8)
             man:sysctl.d(5)
   Main PID: 22146 (code=exited, status=0/SUCCESS)
        CPU: 9ms

Oct 11 21:16:49 4225a859241c.mylabserver.com systemd[1]: Starting Apply Kernel Variables...
Oct 11 21:16:49 4225a859241c.mylabserver.com systemd[1]: Finished Apply Kernel Variables.

● grok_exporter.service - Grok Exporter
     Loaded: loaded (/usr/lib/systemd/system/grok_exporter.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
   Main PID: 672 (grok_exporter)
      Tasks: 8 (limit: 24437)
     Memory: 18.0M
        CPU: 3.590s
     CGroup: /system.slice/grok_exporter.service
             └─672 /usr/local/bin/grok_exporter -config=/etc/grok_exporter/config.yml

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Started Grok Exporter.
Oct 11 18:51:29 4225a859241c.mylabserver.com grok_exporter[672]: Starting server on http://4225a859241c.mylabserver.com:9144/metrics

● veritysetup.target - Local Verity Protected Volumes
     Loaded: loaded (/usr/lib/systemd/system/veritysetup.target; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● timers.target - Timer Units
     Loaded: loaded (/usr/lib/systemd/system/timers.target; static)
     Active: active since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Reached target Timer Units.

● blackbox_exporter.service - Blackbox prober exporter
     Loaded: loaded (/usr/lib/systemd/system/blackbox_exporter.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://github.com/prometheus/blackbox_exporter
   Main PID: 668 (blackbox_export)
      Tasks: 9 (limit: 24437)
     Memory: 27.7M
        CPU: 42.082s
     CGroup: /system.slice/blackbox_exporter.service
             └─668 /usr/bin/blackbox_exporter --config.file=/etc/prometheus/blackbox.yml

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Started Blackbox prober exporter.
Oct 11 18:51:30 4225a859241c.mylabserver.com blackbox_exporter[668]: ts=2024-10-11T11:51:30.413Z caller=main.go:87 level=info msg="Starting blackbox_exporter" version="(version=0.25.0, branch=HEAD, revision=ef3ff4fef195333fb8ee0039fb487b2f5007908f)"
Oct 11 18:51:30 4225a859241c.mylabserver.com blackbox_exporter[668]: ts=2024-10-11T11:51:30.413Z caller=main.go:88 level=info build_context="(go=go1.22.2, platform=linux/amd64, user=root@47d5b0d99f18, date=20240409-12:58:39, tags=unknown)"
Oct 11 18:51:30 4225a859241c.mylabserver.com blackbox_exporter[668]: ts=2024-10-11T11:51:30.458Z caller=main.go:100 level=info msg="Loaded config file"
Oct 11 18:51:30 4225a859241c.mylabserver.com blackbox_exporter[668]: ts=2024-10-11T11:51:30.578Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9115
Oct 11 18:51:30 4225a859241c.mylabserver.com blackbox_exporter[668]: ts=2024-10-11T11:51:30.578Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9115

● network.target - Network
     Loaded: loaded (/usr/lib/systemd/system/network.target; static)
     Active: active since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: man:systemd.special(7)
             https://systemd.io/NETWORK_ONLINE

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Reached target Network.

● system-serial\x2dgetty.slice - Slice /system/serial-getty
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Tasks: 1
     Memory: 292.0K
        CPU: 3ms
     CGroup: /system.slice/system-serial\x2dgetty.slice
             └─serial-getty@ttyS0.service
               └─870 /sbin/agetty -o "-p -- \\u" --keep-baud 115200,57600,38400,9600 - vt220

● system-sshd\x2dkeygen.slice - Slice /system/sshd-keygen
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Tasks: 0
     Memory: 0B
        CPU: 0
     CGroup: /system.slice/system-sshd\x2dkeygen.slice

● sys-devices-pci0000:00-0000:00:04.0-nvme-nvme0-nvme0n1-nvme0n1p2.device - Amazon Elastic Block Store root
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:04.0/nvme/nvme0/nvme0n1/nvme0n1p2

● sys-fs-fuse-connections.mount - FUSE Control File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /sys/fs/fuse/connections
       What: fusectl
       Docs: https://docs.kernel.org/filesystems/fuse.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 2ms
     CGroup: /sys-fs-fuse-connections.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounting FUSE Control File System...
Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted FUSE Control File System.

● cloud-init.target - Cloud-init target
     Loaded: loaded (/usr/lib/systemd/system/cloud-init.target; enabled-runtime; preset: disabled)
     Active: active since Fri 2024-10-11 18:54:10 +07; 2h 31min ago
      Until: Fri 2024-10-11 18:54:10 +07; 2h 31min ago

Oct 11 18:54:10 4225a859241c.mylabserver.com systemd[1]: Reached target Cloud-init target.

● systemd-initctl.socket - initctl Compatibility Named Pipe
     Loaded: loaded (/usr/lib/systemd/system/systemd-initctl.socket; static)
     Active: active (listening) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● systemd-initctl.service
       Docs: man:systemd-initctl.socket(8)
     Listen: /run/initctl (FIFO)
     CGroup: /system.slice/systemd-initctl.socket

● mysqld_exporter.service - Prometheus MySQL Exporter
     Loaded: loaded (/usr/lib/systemd/system/mysqld_exporter.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
   Main PID: 685 (mysqld_exporter)
      Tasks: 5 (limit: 24437)
     Memory: 14.7M
        CPU: 1.718s
     CGroup: /system.slice/mysqld_exporter.service
             └─685 /usr/bin/mysqld_exporter --config.my-cnf /etc/my.cnf.d/client.cnf --collect.global_status --collect.info_schema.innodb_metrics --collect.auto_increment.columns --collect.info_schema.processlist --collect.binlog_size --collect.info_schema.tablestats --collect.global_variables --collect.info_schema.query_response_time --collect.info_schema.userstats --collect.info_schema.tables --collect.perf_schema.tablelocks --collect.perf_schema.file_events --collect.perf_schema.eventswaits --collect.perf_schema.indexiowaits --collect.perf_schema.tableiowaits --collect.slave_status --web.listen-address=0.0.0.0:9104

Oct 11 21:23:36 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:23:36.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:23:51 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:23:51.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:24:06 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:24:06.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:24:21 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:24:21.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:24:36 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:24:36.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:24:51 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:24:51.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:25:06 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:06.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:25:21 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:21.807Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:25:36 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:36.806Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"
Oct 11 21:25:51 4225a859241c.mylabserver.com mysqld_exporter[685]: ts=2024-10-11T14:25:51.807Z caller=exporter.go:152 level=error msg="Error pinging mysqld" err="dial tcp [::1]:3306: connect: connection refused"

● cloud-config.target - Cloud-config availability
     Loaded: loaded (/usr/lib/systemd/system/cloud-config.target; static)
     Active: active since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:31 +07; 2h 34min ago

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Reached target Cloud-config availability.

● NetworkManager.service - Network Manager
     Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: man:NetworkManager(8)
   Main PID: 651 (NetworkManager)
      Tasks: 3 (limit: 24437)
     Memory: 7.7M
        CPU: 1.080s
     CGroup: /system.slice/NetworkManager.service
             └─651 /usr/sbin/NetworkManager --no-daemon

Oct 11 21:16:26 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656186.7737] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:17:36 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656256.7743] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:18:46 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656326.7751] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:19:56 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656396.7755] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:21:06 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656466.7760] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:21:28 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656488.3935] dhcp4 (eth0): state changed new lease, address=172.31.42.197
Oct 11 21:22:10 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656530.8240] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:23:20 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656600.8239] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:24:26 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656666.7776] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75
Oct 11 21:25:36 4225a859241c.mylabserver.com NetworkManager[651]: <info>  [1728656736.7784] dhcp6 (eth0): state changed new lease, address=2406:da18:77c:6103:497e:1479:fdd9:2d75

● remote-fs.target - Remote File Systems
     Loaded: loaded (/usr/lib/systemd/system/remote-fs.target; enabled; preset: enabled)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● influxdb.service - InfluxDB is an open-source, distributed, time series database
     Loaded: loaded (/usr/lib/systemd/system/influxdb.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:39 +07; 2h 34min ago
       Docs: https://docs.influxdata.com/influxdb/
   Main PID: 829 (influxd)
      Tasks: 10 (limit: 24437)
     Memory: 164.7M
        CPU: 20.801s
     CGroup: /system.slice/influxdb.service
             └─829 /usr/bin/influxd -config /etc/influxdb/influxdb.conf

Oct 11 21:24:21 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:24:21 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 82131594-87dc-11ef-839e-0a816498216b 14774
Oct 11 21:24:31 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:24:31 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 8809102e-87dc-11ef-839f-0a816498216b 12883
Oct 11 21:24:41 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:24:41 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 8dff0928-87dc-11ef-83a0-0a816498216b 13037
Oct 11 21:24:51 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:24:51 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 93f5077d-87dc-11ef-83a1-0a816498216b 41128
Oct 11 21:25:01 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:01 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 99eaebd6-87dc-11ef-83a2-0a816498216b 18264
Oct 11 21:25:11 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:11 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" 9fe0eac5-87dc-11ef-83a3-0a816498216b 22779
Oct 11 21:25:21 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:21 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" a5d6c75c-87dc-11ef-83a4-0a816498216b 13401
Oct 11 21:25:31 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:31 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" abccc000-87dc-11ef-83a5-0a816498216b 13168
Oct 11 21:25:41 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:41 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" b1c2c6d3-87dc-11ef-83a6-0a816498216b 12193
Oct 11 21:25:51 4225a859241c.mylabserver.com influxd-systemd-start.sh[829]: [httpd] 172.31.42.197 - admin [11/Oct/2024:21:25:51 +0700] "POST /write?db=telegraf HTTP/1.1 " 204 0 "-" "Telegraf/1.32.1 Go/1.23.1" b7b8b5f8-87dc-11ef-83a7-0a816498216b 12742

● sys-subsystem-net-devices-docker0.device - /sys/subsystem/net/devices/docker0
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:40 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:40 +07; 2h 34min ago
     Device: /sys/devices/virtual/net/docker0

● local-fs-pre.target - Preparation for Local File Systems
     Loaded: loaded (/usr/lib/systemd/system/local-fs-pre.target; static)
     Active: active since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Reached target Preparation for Local File Systems.

● polkit.service - Authorization Manager
     Loaded: loaded (/usr/lib/systemd/system/polkit.service; static)
     Active: active (running) since Fri 2024-10-11 18:51:33 +07; 2h 34min ago
       Docs: man:polkit(8)
   Main PID: 826 (polkitd)
      Tasks: 6 (limit: 24437)
     Memory: 6.4M
        CPU: 258ms
     CGroup: /system.slice/polkit.service
             └─826 /usr/lib/polkit-1/polkitd --no-debug

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Starting Authorization Manager...
Oct 11 18:51:31 4225a859241c.mylabserver.com polkitd[826]: Started polkitd version 0.117
Oct 11 18:51:33 4225a859241c.mylabserver.com polkitd[826]: Loading rules from directory /etc/polkit-1/rules.d
Oct 11 18:51:33 4225a859241c.mylabserver.com polkitd[826]: Loading rules from directory /usr/share/polkit-1/rules.d
Oct 11 18:51:33 4225a859241c.mylabserver.com polkitd[826]: Finished loading, compiling and executing 2 rules
Oct 11 18:51:33 4225a859241c.mylabserver.com systemd[1]: Started Authorization Manager.
Oct 11 18:51:33 4225a859241c.mylabserver.com polkitd[826]: Acquired the name org.freedesktop.PolicyKit1 on the system bus

● systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch
     Loaded: loaded (/usr/lib/systemd/system/systemd-ask-password-wall.path; static)
     Active: active (waiting) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● systemd-ask-password-wall.service
       Docs: man:systemd-ask-password-wall.path(8)

● sys-devices-pci0000:00-0000:00:1e.0-nvme-nvme1-nvme1n1.device - Amazon Elastic Block Store
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:1e.0/nvme/nvme1/nvme1n1

● dbus.socket - D-Bus System Message Bus Socket
     Loaded: loaded (/usr/lib/systemd/system/dbus.socket; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
   Triggers: ● dbus-broker.service
     Listen: /run/dbus/system_bus_socket (Stream)
     CGroup: /system.slice/dbus.socket

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Listening on D-Bus System Message Bus Socket.

● nss-user-lookup.target - User and Group Name Lookups
     Loaded: loaded (/usr/lib/systemd/system/nss-user-lookup.target; static)
     Active: active since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:17 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Reached target User and Group Name Lookups.

● dracut-shutdown.service - Restore /run/initramfs on shutdown
     Loaded: loaded (/usr/lib/systemd/system/dracut-shutdown.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
       Docs: man:dracut-shutdown.service(8)
   Main PID: 618 (code=exited, status=0/SUCCESS)
        CPU: 1ms

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Starting Restore /run/initramfs on shutdown...
Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Finished Restore /run/initramfs on shutdown.

● systemd-boot-update.service - Automatic Boot Loader Update
     Loaded: loaded (/usr/lib/systemd/system/systemd-boot-update.service; enabled; preset: enabled)
     Active: active (exited) since Fri 2024-10-11 18:51:15 +07; 2h 34min ago
       Docs: man:bootctl(1)
   Main PID: 585 (code=exited, status=0/SUCCESS)
        CPU: 6ms

Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Starting Automatic Boot Loader Update...
Oct 11 18:51:15 4225a859241c.mylabserver.com bootctl[585]: Couldn't find EFI system partition, skipping.
Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Finished Automatic Boot Loader Update.

● system-modprobe.slice - Slice /system/modprobe
     Loaded: loaded
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Tasks: 0
     Memory: 56.0K
        CPU: 87ms
     CGroup: /system.slice/system-modprobe.slice

● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:41 +07; 2h 34min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 938 (dockerd)
      Tasks: 12
     Memory: 52.5M
        CPU: 1.969s
     CGroup: /system.slice/docker.service
             └─938 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Oct 11 18:51:37 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:37.486404155+07:00" level=info msg="[graphdriver] using prior storage driver: overlay2"
Oct 11 18:51:37 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:37.980728905+07:00" level=info msg="Loading containers: start."
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.107962290+07:00" level=info msg="Loading containers: done."
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.224046796+07:00" level=warning msg="WARNING: bridge-nf-call-iptables is disabled"
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.224079283+07:00" level=warning msg="WARNING: bridge-nf-call-ip6tables is disabled"
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.224111930+07:00" level=info msg="Docker daemon" commit=41ca978 containerd-snapshotter=false storage-driver=overlay2 version=27.3.1
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.224215668+07:00" level=info msg="Daemon has completed initialization"
Oct 11 18:51:41 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T18:51:41.775789674+07:00" level=info msg="API listen on /run/docker.sock"
Oct 11 18:51:41 4225a859241c.mylabserver.com systemd[1]: Started Docker Application Container Engine.
Oct 11 19:09:15 4225a859241c.mylabserver.com dockerd[938]: time="2024-10-11T19:09:15.826567383+07:00" level=info msg="ignoring event" container=566ac8fc1acb2f325568e00fcb598b1c439abeb7651f8488963d7e89990a64ec module=libcontainerd namespace=moby topic=/tasks/delete type="*events.TaskDelete"

● crond.service - Command Scheduler
     Loaded: loaded (/usr/lib/systemd/system/crond.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
   Main PID: 868 (crond)
      Tasks: 1 (limit: 24437)
     Memory: 1.9M
        CPU: 89ms
     CGroup: /system.slice/crond.service
             └─868 /usr/sbin/crond -n

Oct 11 19:01:01 4225a859241c.mylabserver.com CROND[3860]: (root) CMDEND (run-parts /etc/cron.hourly)
Oct 11 19:12:01 4225a859241c.mylabserver.com crond[868]: (man-sinh-lee) RELOAD (/var/spool/cron/man-sinh-lee)
Oct 11 20:01:01 4225a859241c.mylabserver.com CROND[10748]: (root) CMD (run-parts /etc/cron.hourly)
Oct 11 20:01:01 4225a859241c.mylabserver.com run-parts[10751]: (/etc/cron.hourly) starting 0anacron
Oct 11 20:01:01 4225a859241c.mylabserver.com run-parts[10757]: (/etc/cron.hourly) finished 0anacron
Oct 11 20:01:01 4225a859241c.mylabserver.com CROND[10747]: (root) CMDEND (run-parts /etc/cron.hourly)
Oct 11 21:01:01 4225a859241c.mylabserver.com CROND[19683]: (root) CMD (run-parts /etc/cron.hourly)
Oct 11 21:01:01 4225a859241c.mylabserver.com run-parts[19686]: (/etc/cron.hourly) starting 0anacron
Oct 11 21:01:02 4225a859241c.mylabserver.com run-parts[19692]: (/etc/cron.hourly) finished 0anacron
Oct 11 21:01:02 4225a859241c.mylabserver.com CROND[19682]: (root) CMDEND (run-parts /etc/cron.hourly)

● influxdb_exporter.service - InfluxDB stats exporter for Prometheus.
     Loaded: loaded (/usr/lib/systemd/system/influxdb_exporter.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://github.com/prometheus/influxdb_exporter
   Main PID: 684 (influxdb_export)
      Tasks: 4 (limit: 24437)
     Memory: 4.5M
        CPU: 37ms
     CGroup: /system.slice/influxdb_exporter.service
             └─684 /usr/bin/influxdb_exporter

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Started InfluxDB stats exporter for Prometheus..
Oct 11 18:51:30 4225a859241c.mylabserver.com influxdb_exporter[684]: ts=2024-10-11T11:51:30.283Z caller=main.go:342 level=info msg="Starting influxdb_exporter" version="(version=0.11.5, branch=HEAD, revision=26f65dc9f49572ddb1b7fcb2e502412eef8ac300)"
Oct 11 18:51:30 4225a859241c.mylabserver.com influxdb_exporter[684]: ts=2024-10-11T11:51:30.283Z caller=main.go:343 level=info msg="Build context" context="(go=go1.21.4, platform=linux/amd64, user=root@e2814de855b0, date=20231206-10:58:06, tags=netgo)"

● cloud-config.service - Apply the settings specified in cloud-config
     Loaded: loaded (/usr/lib/systemd/system/cloud-config.service; enabled; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
   Main PID: 815 (code=exited, status=0/SUCCESS)
        CPU: 580ms

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Starting Apply the settings specified in cloud-config...
Oct 11 18:51:31 4225a859241c.mylabserver.com cloud-init[857]: Cloud-init v. 23.4-7.el9_4.6.alma.1 running 'modules:config' at Fri, 11 Oct 2024 11:51:31 +0000. Up 36.85 seconds.
Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Finished Apply the settings specified in cloud-config.

● systemd-update-utmp.service - Record System Boot/Shutdown in UTMP
     Loaded: loaded (/usr/lib/systemd/system/systemd-update-utmp.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
       Docs: man:systemd-update-utmp.service(8)
             man:utmp(5)
   Main PID: 609 (code=exited, status=0/SUCCESS)
        CPU: 6ms

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Starting Record System Boot/Shutdown in UTMP...
Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Finished Record System Boot/Shutdown in UTMP.

● slices.target - Slice Units
     Loaded: loaded (/usr/lib/systemd/system/slices.target; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● mlocate-updatedb.timer - Updates mlocate database every day
     Loaded: loaded (/usr/lib/systemd/system/mlocate-updatedb.timer; enabled; preset: enabled)
     Active: active (waiting) since Fri 2024-10-11 20:37:34 +07; 48min ago
      Until: Fri 2024-10-11 20:37:34 +07; 48min ago
    Trigger: Sat 2024-10-12 00:00:00 +07; 2h 34min left
   Triggers: ● mlocate-updatedb.service

Oct 11 20:37:34 4225a859241c.mylabserver.com systemd[1]: Started Updates mlocate database every day.

● nm-cloud-setup.timer - Periodically run nm-cloud-setup
     Loaded: loaded (/usr/lib/systemd/system/nm-cloud-setup.timer; enabled; preset: disabled)
     Active: active (waiting) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
    Trigger: Fri 2024-10-11 21:26:28 +07; 33s left
   Triggers: ● nm-cloud-setup.service

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started Periodically run nm-cloud-setup.

● sshd-keygen.target
     Loaded: loaded (/usr/lib/systemd/system/sshd-keygen.target; static)
     Active: active since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:17 +07; 2h 34min ago

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Reached target sshd-keygen.target.

● dev-mqueue.mount - POSIX Message Queue File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /dev/mqueue
       What: mqueue
       Docs: man:mq_overview(7)
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 2ms
     CGroup: /dev-mqueue.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted POSIX Message Queue File System.

● sssd-kcm.socket - SSSD Kerberos Cache Manager responder socket
     Loaded: loaded (/usr/lib/systemd/system/sssd-kcm.socket; enabled; preset: enabled)
     Active: active (listening) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
   Triggers: ● sssd-kcm.service
       Docs: man:sssd-kcm(8)
     Listen: /run/.heim_org.h5l.kcm-socket (Stream)
     CGroup: /system.slice/sssd-kcm.socket

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Listening on SSSD Kerberos Cache Manager responder socket.

● systemd-udevd-kernel.socket - udev Kernel Socket
     Loaded: loaded (/usr/lib/systemd/system/systemd-udevd-kernel.socket; static)
     Active: active (running) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● systemd-udevd.service
       Docs: man:systemd-udevd-kernel.socket(8)
             man:udev(7)
     Listen: kobject-uevent 1 (Netlink)
     CGroup: /system.slice/systemd-udevd-kernel.socket

● cloud-init.service - Initial cloud-init job (metadata service crawler)
     Loaded: loaded (/usr/lib/systemd/system/cloud-init.service; enabled; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
   Main PID: 750 (code=exited, status=0/SUCCESS)
        CPU: 838ms

Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: |   1   | 172.31.32.0 |   0.0.0.0   | 255.255.240.0 |    eth0   |   U   |
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: +-------+-------------+-------------+---------------+-----------+-------+
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: +++++++++++++++++++Route IPv6 info+++++++++++++++++++
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: +-------+-------------+---------+-----------+-------+
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: | Route | Destination | Gateway | Interface | Flags |
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: +-------+-------------+---------+-----------+-------+
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: |   1   |  fe80::/64  |    ::   |    eth0   |   U   |
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: |   3   |  multicast  |    ::   |    eth0   |   U   |
Oct 11 18:51:30 4225a859241c.mylabserver.com cloud-init[766]: ci-info: +-------+-------------+---------+-----------+-------+
Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Finished Initial cloud-init job (metadata service crawler).

● sys-kernel-tracing.mount - Kernel Trace File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /sys/kernel/tracing
       What: tracefs
       Docs: https://docs.kernel.org/trace/ftrace.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 2ms
     CGroup: /sys-kernel-tracing.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted Kernel Trace File System.

● sys-devices-virtual-block-dm\x2d0.device - /sys/devices/virtual/block/dm-0
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:14 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:14 +07; 2h 34min ago
     Device: /sys/devices/virtual/block/dm-0

● cryptsetup.target - Local Encrypted Volumes
     Loaded: loaded (/usr/lib/systemd/system/cryptsetup.target; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● dm-event.socket - Device-mapper event daemon FIFOs
     Loaded: loaded (/usr/lib/systemd/system/dm-event.socket; enabled; preset: enabled)
     Active: active (listening) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● dm-event.service
       Docs: man:dmeventd(8)
     Listen: /run/dmeventd-server (FIFO)
             /run/dmeventd-client (FIFO)
     CGroup: /system.slice/dm-event.socket

● irqbalance.service - irqbalance daemon
     Loaded: loaded (/usr/lib/systemd/system/irqbalance.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
       Docs: man:irqbalance(1)
             https://github.com/Irqbalance/irqbalance
   Main PID: 619 (irqbalance)
      Tasks: 2 (limit: 24437)
     Memory: 2.6M
        CPU: 333ms
     CGroup: /system.slice/irqbalance.service
             └─619 /usr/sbin/irqbalance --foreground

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Started irqbalance daemon.
Oct 11 18:51:27 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: Cannot change IRQ 32 affinity: Input/output error
Oct 11 18:51:27 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: IRQ 32 affinity is now unmanaged
Oct 11 18:51:27 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: Cannot change IRQ 26 affinity: Input/output error
Oct 11 18:51:27 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: IRQ 26 affinity is now unmanaged
Oct 11 19:03:57 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: Cannot change IRQ 27 affinity: Input/output error
Oct 11 19:03:57 4225a859241c.mylabserver.com /usr/sbin/irqbalance[619]: IRQ 27 affinity is now unmanaged

● rsyslog.service - System Logging Service
     Loaded: loaded (/usr/lib/systemd/system/rsyslog.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:32 +07; 2h 34min ago
       Docs: man:rsyslogd(8)
             https://www.rsyslog.com/doc/
   Main PID: 822 (rsyslogd)
      Tasks: 4 (limit: 24437)
     Memory: 5.8M
        CPU: 1.809s
     CGroup: /system.slice/rsyslog.service
             └─822 /usr/sbin/rsyslogd -n

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Starting System Logging Service...
Oct 11 18:51:32 4225a859241c.mylabserver.com rsyslogd[822]: [origin software="rsyslogd" swVersion="8.2310.0-4.el9" x-pid="822" x-info="https://www.rsyslog.com"] start
Oct 11 18:51:32 4225a859241c.mylabserver.com systemd[1]: Started System Logging Service.
Oct 11 18:51:32 4225a859241c.mylabserver.com rsyslogd[822]: imjournal: journal files changed, reloading...  [v8.2310.0-4.el9 try https://www.rsyslog.com/e/0 ]
Oct 11 21:22:10 4225a859241c.mylabserver.com rsyslogd[822]: imjournal: journal files changed, reloading...  [v8.2310.0-4.el9 try https://www.rsyslog.com/e/0 ]
Oct 11 21:22:10 4225a859241c.mylabserver.com rsyslogd[822]: imjournal: journal files changed, reloading...  [v8.2310.0-4.el9 try https://www.rsyslog.com/e/0 ]

● proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point
     Loaded: loaded (/usr/lib/systemd/system/proc-sys-fs-binfmt_misc.automount; static)
     Active: active (waiting) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
   Triggers: ● proc-sys-fs-binfmt_misc.mount
      Where: /proc/sys/fs/binfmt_misc
       Docs: https://docs.kernel.org/admin-guide/binfmt-misc.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems

● network-pre.target - Preparation for Network
     Loaded: loaded (/usr/lib/systemd/system/network-pre.target; static)
     Active: active since Fri 2024-10-11 18:51:26 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:26 +07; 2h 34min ago
       Docs: man:systemd.special(7)
             https://systemd.io/NETWORK_ONLINE

Oct 11 18:51:26 4225a859241c.mylabserver.com systemd[1]: Reached target Preparation for Network.

● auditd.service - Security Auditing Service
     Loaded: loaded (/usr/lib/systemd/system/auditd.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
       Docs: man:auditd(8)
             https://github.com/linux-audit/audit-documentation
   Main PID: 589 (auditd)
      Tasks: 2 (limit: 24437)
     Memory: 5.5M
        CPU: 371ms
     CGroup: /system.slice/auditd.service
             └─589 /sbin/auditd

Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: enabled 1
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: failure 1
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: pid 589
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: rate_limit 0
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: backlog_limit 8192
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: lost 0
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: backlog 4
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: backlog_wait_time 60000
Oct 11 18:51:16 4225a859241c.mylabserver.com augenrules[602]: backlog_wait_time_actual 0
Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started Security Auditing Service.

● containerd.service - containerd container runtime
     Loaded: loaded (/usr/lib/systemd/system/containerd.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:34 +07; 2h 34min ago
       Docs: https://containerd.io
   Main PID: 691 (containerd)
      Tasks: 8
     Memory: 23.0M
        CPU: 3.208s
     CGroup: /system.slice/containerd.service
             └─691 /usr/bin/containerd

Oct 11 18:51:34 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:34.498880379+07:00" level=info msg="Start streaming server"
Oct 11 18:51:34 4225a859241c.mylabserver.com systemd[1]: Started containerd container runtime.
Oct 11 18:51:34 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:34.504685900+07:00" level=info msg="containerd successfully booted in 0.752420s"
Oct 11 18:51:42 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:42.871004380+07:00" level=info msg="loading plugin \"io.containerd.event.v1.publisher\"..." runtime=io.containerd.runc.v2 type=io.containerd.event.v1
Oct 11 18:51:42 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:42.871111187+07:00" level=info msg="loading plugin \"io.containerd.internal.v1.shutdown\"..." runtime=io.containerd.runc.v2 type=io.containerd.internal.v1
Oct 11 18:51:42 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:42.871134188+07:00" level=info msg="loading plugin \"io.containerd.ttrpc.v1.task\"..." runtime=io.containerd.runc.v2 type=io.containerd.ttrpc.v1
Oct 11 18:51:42 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T18:51:42.871244925+07:00" level=info msg="loading plugin \"io.containerd.ttrpc.v1.pause\"..." runtime=io.containerd.runc.v2 type=io.containerd.ttrpc.v1
Oct 11 19:09:15 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T19:09:15.830796262+07:00" level=info msg="shim disconnected" id=566ac8fc1acb2f325568e00fcb598b1c439abeb7651f8488963d7e89990a64ec namespace=moby
Oct 11 19:09:15 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T19:09:15.830863762+07:00" level=warning msg="cleaning up after shim disconnected" id=566ac8fc1acb2f325568e00fcb598b1c439abeb7651f8488963d7e89990a64ec namespace=moby
Oct 11 19:09:15 4225a859241c.mylabserver.com containerd[691]: time="2024-10-11T19:09:15.830881103+07:00" level=info msg="cleaning up dead shim" namespace=moby

● sys-devices-pci0000:00-0000:00:04.0-nvme-nvme0-nvme0n1-nvme0n1p1.device - Amazon Elastic Block Store biosboot
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pci0000:00/0000:00:04.0/nvme/nvme0/nvme0n1/nvme0n1p1

● systemd-tmpfiles-setup.service - Create Volatile Files and Directories
     Loaded: loaded (/usr/lib/systemd/system/systemd-tmpfiles-setup.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:15 +07; 2h 34min ago
       Docs: man:tmpfiles.d(5)
             man:systemd-tmpfiles(8)
   Main PID: 586 (code=exited, status=0/SUCCESS)
        CPU: 19ms

Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Starting Create Volatile Files and Directories...
Oct 11 18:51:15 4225a859241c.mylabserver.com systemd-tmpfiles[586]: /usr/lib/tmpfiles.d/elasticsearch.conf:1: Line references path below legacy directory /var/run/, updating /var/run/elasticsearch → /run/elasticsearch; please update the tmpfiles.d/ drop-in file accordingly.
Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Finished Create Volatile Files and Directories.

● sys-devices-platform-serial8250-tty-ttyS2.device - /sys/devices/platform/serial8250/tty/ttyS2
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/platform/serial8250/tty/ttyS2

● getty.target - Login Prompts
     Loaded: loaded (/usr/lib/systemd/system/getty.target; static)
     Active: active since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:systemd.special(7)
             man:systemd-getty-generator(8)
             http://0pointer.de/blog/projects/serial-console.html

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Reached target Login Prompts.

● systemd-remount-fs.service - Remount Root and Kernel File Systems
     Loaded: loaded (/usr/lib/systemd/system/systemd-remount-fs.service; enabled-runtime; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
       Docs: man:systemd-remount-fs.service(8)
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
   Main PID: 522 (code=exited, status=0/SUCCESS)
        CPU: 13ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Remount Root and Kernel File Systems.

● mnt-lvdata.mount - /mnt/lvdata
     Loaded: loaded (/etc/fstab; generated)
     Active: active (mounted) since Fri 2024-10-11 18:51:15 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:15 +07; 2h 34min ago
      Where: /mnt/lvdata
       What: /dev/mapper/vgelk-lvdata
       Docs: man:fstab(5)
             man:systemd-fstab-generator(8)
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 13ms
     CGroup: /system.slice/mnt-lvdata.mount

Oct 11 18:51:14 4225a859241c.mylabserver.com systemd[1]: Mounting /mnt/lvdata...
Oct 11 18:51:15 4225a859241c.mylabserver.com systemd[1]: Mounted /mnt/lvdata.

● dbus-broker.service - D-Bus System Message Bus
     Loaded: loaded (/usr/lib/systemd/system/dbus-broker.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
TriggeredBy: ● dbus.socket
       Docs: man:dbus-broker-launch(1)
   Main PID: 612 (dbus-broker-lau)
      Tasks: 2 (limit: 24437)
     Memory: 2.4M
        CPU: 815ms
     CGroup: /system.slice/dbus-broker.service
             ├─612 /usr/bin/dbus-broker-launch --scope system --audit
             └─616 dbus-broker --log 4 --controller 9 --machine-id ec20f5ba53a6e950674ad204defd7591 --max-bytes 536870912 --max-fds 4096 --max-matches 131072 --audit

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Starting D-Bus System Message Bus...
Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Started D-Bus System Message Bus.
Oct 11 18:51:17 4225a859241c.mylabserver.com dbus-broker-lau[612]: Ready

● lvm2-monitor.service - Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling
     Loaded: loaded (/usr/lib/systemd/system/lvm2-monitor.service; enabled; preset: enabled)
     Active: active (exited) since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:dmeventd(8)
             man:lvcreate(8)
             man:lvchange(8)
             man:vgchange(8)
   Main PID: 514 (code=exited, status=0/SUCCESS)
        CPU: 16ms

Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Finished Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.

● systemd-journal-flush.service - Flush Journal to Persistent Storage
     Loaded: loaded (/usr/lib/systemd/system/systemd-journal-flush.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       Docs: man:systemd-journald.service(8)
             man:journald.conf(5)
   Main PID: 532 (code=exited, status=0/SUCCESS)
        CPU: 7ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Starting Flush Journal to Persistent Storage...
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Finished Flush Journal to Persistent Storage.

● pushgateway.service - Prometheus push acceptor for ephemeral and batch jobs.
     Loaded: loaded (/usr/lib/systemd/system/pushgateway.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://github.com/prometheus/pushgateway
   Main PID: 689 (pushgateway)
      Tasks: 8 (limit: 24437)
     Memory: 18.5M
        CPU: 1.264s
     CGroup: /system.slice/pushgateway.service
             └─689 /usr/bin/pushgateway

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Started Prometheus push acceptor for ephemeral and batch jobs..
Oct 11 18:51:30 4225a859241c.mylabserver.com pushgateway[689]: ts=2024-10-11T11:51:30.551Z caller=main.go:87 level=info msg="starting pushgateway" version="(version=1.9.0, branch=HEAD, revision=d1ca1a6a426126a09a21f745e8ffbaba550f9643)"
Oct 11 18:51:30 4225a859241c.mylabserver.com pushgateway[689]: ts=2024-10-11T11:51:30.551Z caller=main.go:88 level=info build_context="(go=go1.22.4, platform=linux/amd64, user=root@2167597b1e9c, date=20240608-15:04:08, tags=unknown)"
Oct 11 18:51:30 4225a859241c.mylabserver.com pushgateway[689]: ts=2024-10-11T11:51:30.744Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9091
Oct 11 18:51:30 4225a859241c.mylabserver.com pushgateway[689]: ts=2024-10-11T11:51:30.744Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9091

● sshd.service - OpenSSH server daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 823 (sshd)
      Tasks: 1 (limit: 24437)
     Memory: 10.2M
        CPU: 21.392s
     CGroup: /system.slice/sshd.service
             └─823 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Oct 11 21:23:36 4225a859241c.mylabserver.com sshd[23154]: Connection closed by 172.31.42.197 port 37764 [preauth]
Oct 11 21:23:51 4225a859241c.mylabserver.com sshd[23207]: Connection closed by 172.31.42.197 port 52354 [preauth]
Oct 11 21:24:06 4225a859241c.mylabserver.com sshd[23259]: Connection closed by 172.31.42.197 port 48586 [preauth]
Oct 11 21:24:21 4225a859241c.mylabserver.com sshd[23300]: Connection closed by 172.31.42.197 port 53592 [preauth]
Oct 11 21:24:36 4225a859241c.mylabserver.com sshd[23364]: Connection closed by 172.31.42.197 port 53156 [preauth]
Oct 11 21:24:51 4225a859241c.mylabserver.com sshd[23418]: Connection closed by 172.31.42.197 port 51418 [preauth]
Oct 11 21:25:06 4225a859241c.mylabserver.com sshd[23469]: Connection closed by 172.31.42.197 port 42792 [preauth]
Oct 11 21:25:21 4225a859241c.mylabserver.com sshd[23548]: Connection closed by 172.31.42.197 port 49038 [preauth]
Oct 11 21:25:36 4225a859241c.mylabserver.com sshd[23568]: Connection closed by 172.31.42.197 port 41126 [preauth]
Oct 11 21:25:51 4225a859241c.mylabserver.com sshd[23620]: Connection closed by 172.31.42.197 port 42806 [preauth]

● cloud-final.service - Execute cloud user/final scripts
     Loaded: loaded (/usr/lib/systemd/system/cloud-final.service; enabled; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:32 +07; 2h 34min ago
   Main PID: 865 (code=exited, status=0/SUCCESS)
        CPU: 669ms

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Starting Execute cloud user/final scripts...
Oct 11 18:51:32 4225a859241c.mylabserver.com cloud-init[901]: Cloud-init v. 23.4-7.el9_4.6.alma.1 running 'modules:final' at Fri, 11 Oct 2024 11:51:32 +0000. Up 37.62 seconds.
Oct 11 18:51:32 4225a859241c.mylabserver.com cloud-init[901]: 2024-10-11 11:51:32,564 - modules.py[WARNING]: Could not find module named cc_refresh_rmc_and_interface (searched ['cc_refresh_rmc_and_interface', 'cloudinit.config.cc_refresh_rmc_and_interface'])
Oct 11 18:51:32 4225a859241c.mylabserver.com cloud-init[901]: Cloud-init v. 23.4-7.el9_4.6.alma.1 finished at Fri, 11 Oct 2024 11:51:32 +0000. Datasource DataSourceEc2Local.  Up 37.90 seconds
Oct 11 18:51:32 4225a859241c.mylabserver.com systemd[1]: Finished Execute cloud user/final scripts.

● systemd-journald-dev-log.socket - Journal Socket (/dev/log)
     Loaded: loaded (/usr/lib/systemd/system/systemd-journald-dev-log.socket; static)
     Active: active (running) since Fri 2024-10-11 18:50:57 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:50:57 +07; 2h 34min ago
   Triggers: ● systemd-journald.service
       Docs: man:systemd-journald.service(8)
             man:journald.conf(5)
     Listen: /run/systemd/journal/dev-log (Datagram)
     CGroup: /system.slice/systemd-journald-dev-log.socket

Notice: journal has been rotated since unit was started, output may be incomplete.

● sys-devices-platform-serial8250-tty-ttyS1.device - /sys/devices/platform/serial8250/tty/ttyS1
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/platform/serial8250/tty/ttyS1

● sys-devices-virtual-net-br\x2d84ca61d89962.device - /sys/devices/virtual/net/br-84ca61d89962
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:40 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:40 +07; 2h 34min ago
     Device: /sys/devices/virtual/net/br-84ca61d89962

● basic.target - Basic System
     Loaded: loaded (/usr/lib/systemd/system/basic.target; static)
     Active: active since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:17 +07; 2h 34min ago
       Docs: man:systemd.special(7)

Oct 11 18:51:17 4225a859241c.mylabserver.com systemd[1]: Reached target Basic System.

● session-8.scope - Session 8 of User man-sinh-lee
     Loaded: loaded (/run/systemd/transient/session-8.scope; transient)
  Transient: yes
     Active: active (running) since Fri 2024-10-11 18:54:20 +07; 2h 31min ago
      Tasks: 50
     Memory: 1.2G
        CPU: 4min 52.623s
     CGroup: /user.slice/user-1000.slice/session-8.scope
             ├─ 2144 "sshd: man-sinh-lee [priv]"
             ├─ 2146 "sshd: man-sinh-lee@notty"
             ├─ 2147 -bash
             ├─ 2169 sh
             ├─ 2187 /home/man-sinh-lee/.vscode-server/code-384ff7382de624fb94dbaf6da11977bba1ecd427 command-shell --cli-data-dir /home/man-sinh-lee/.vscode-server/cli --parent-process-id 2169 --on-host=127.0.0.1 --on-port
             ├─ 2221 sh /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/bin/code-server --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
             ├─ 2225 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/server-main.js --connection-token=remotessh --accept-server-license-terms --start-server --enable-remote-auto-shutdown --socket-path=/tmp/code-67929e8b-7b94-4ef6-bd8a-59c6b77ca32a
             ├─ 2258 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node --dns-result-order=ipv4first /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=extensionHost --transformURIs --useHostProxy=false
             ├─ 2269 /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/node /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/bootstrap-fork --type=ptyHost --logsPath /home/man-sinh-lee/.vscode-server/data/logs/20241011T185424
             ├─ 8905 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
             ├─17899 /bin/bash --init-file /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh
             ├─23310 sleep 180
             ├─23637 /bin/bash /home/man-sinh-lee/.vscode-server/cli/servers/Stable-384ff7382de624fb94dbaf6da11977bba1ecd427/server/out/vs/base/node/cpuUsage.sh 8905
             ├─23640 sleep 1
             └─23642 systemctl status "*" --no-pager -l

Oct 11 21:22:51 4225a859241c.mylabserver.com sudo[23005]: pam_unix(sudo:session): session closed for user root
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee ; USER=root ; COMMAND=/bin/systemctl cat elasticsearch-in-action-2e-2023 learn-grafana-10 prometheus-up-and-running-2e
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:23:17 4225a859241c.mylabserver.com sudo[23072]: pam_unix(sudo:session): session closed for user root
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee/prometheus-up-and-running-2e ; USER=root ; COMMAND=/bin/chown -R . man-sinh-lee
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:24:13 4225a859241c.mylabserver.com sudo[23273]: pam_unix(sudo:session): session closed for user root
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: man-sinh-lee : TTY=pts/3 ; PWD=/home/man-sinh-lee ; USER=root ; COMMAND=/bin/chown man-sinh-lee: . -R
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: pam_unix(sudo:session): session opened for user root(uid=0) by man-sinh-lee(uid=1000)
Oct 11 21:24:50 4225a859241c.mylabserver.com sudo[23415]: pam_unix(sudo:session): session closed for user root

● run-credentials-systemd\x2dtmpfiles\x2dsetup.service.mount - /run/credentials/systemd-tmpfiles-setup.service
     Loaded: loaded (/proc/self/mountinfo)
     Active: active (mounted) since Fri 2024-10-11 18:51:15 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:15 +07; 2h 34min ago
      Where: /run/credentials/systemd-tmpfiles-setup.service
       What: none

● systemd-udev-trigger.service - Coldplug All udev Devices
     Loaded: loaded (/usr/lib/systemd/system/systemd-udev-trigger.service; static)
    Drop-In: /usr/lib/systemd/system/systemd-udev-trigger.service.d
             └─systemd-udev-trigger-no-reload.conf
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
       Docs: man:udev(7)
             man:systemd-udevd.service(8)
   Main PID: 524 (code=exited, status=0/SUCCESS)
        CPU: 76ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Coldplug All udev Devices.

● paths.target - Path Units
     Loaded: loaded (/usr/lib/systemd/system/paths.target; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● run-user-1000.mount - /run/user/1000
     Loaded: loaded (/proc/self/mountinfo)
     Active: active (mounted) since Fri 2024-10-11 18:53:02 +07; 2h 32min ago
      Until: Fri 2024-10-11 18:53:02 +07; 2h 32min ago
      Where: /run/user/1000
       What: tmpfs

● logrotate.timer - Daily rotation of log files
     Loaded: loaded (/usr/lib/systemd/system/logrotate.timer; enabled; preset: enabled)
     Active: active (waiting) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
    Trigger: Sat 2024-10-12 00:00:00 +07; 2h 34min left
   Triggers: ● logrotate.service
       Docs: man:logrotate(8)
             man:logrotate.conf(5)

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started Daily rotation of log files.

● tuned.service - Dynamic System Tuning Daemon
     Loaded: loaded (/usr/lib/systemd/system/tuned.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:tuned(8)
             man:tuned.conf(5)
             man:tuned-adm(8)
   Main PID: 690 (tuned)
      Tasks: 4 (limit: 24437)
     Memory: 14.6M
        CPU: 1.763s
     CGroup: /system.slice/tuned.service
             └─690 /usr/bin/python3 -Es /usr/sbin/tuned -l -P

Oct 11 18:51:28 4225a859241c.mylabserver.com systemd[1]: Starting Dynamic System Tuning Daemon...
Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Started Dynamic System Tuning Daemon.

● systemd-coredump.socket - Process Core Dump Socket
     Loaded: loaded (/usr/lib/systemd/system/systemd-coredump.socket; static)
     Active: active (listening) since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd-coredump(8)
     Listen: /run/systemd/coredump (SequentialPacket)
   Accepted: 0; Connected: 0;
     CGroup: /system.slice/systemd-coredump.socket

● sys-subsystem-net-devices-br\x2d84ca61d89962.device - /sys/subsystem/net/devices/br-84ca61d89962
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:40 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:40 +07; 2h 34min ago
     Device: /sys/devices/virtual/net/br-84ca61d89962

● systemd-network-generator.service - Generate network units from Kernel command line
     Loaded: loaded (/usr/lib/systemd/system/systemd-network-generator.service; enabled; preset: enabled)
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
       Docs: man:systemd-network-generator.service(8)
   Main PID: 521 (code=exited, status=0/SUCCESS)
        CPU: 6ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Generate network units from Kernel command line.

● init.scope - System and Service Manager
     Loaded: loaded
  Transient: yes
     Active: active (running) since Fri 2024-10-11 18:50:57 +07; 2h 34min ago
       Docs: man:systemd(1)

Oct 11 21:22:20 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:23:20 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:23:20 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:23:30 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:24:26 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:24:26 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:24:36 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Oct 11 21:25:36 4225a859241c.mylabserver.com systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 11 21:25:36 4225a859241c.mylabserver.com systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 11 21:25:46 4225a859241c.mylabserver.com systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.

● systemd-tmpfiles-clean.timer - Daily Cleanup of Temporary Directories
     Loaded: loaded (/usr/lib/systemd/system/systemd-tmpfiles-clean.timer; static)
     Active: active (waiting) since Fri 2024-10-11 18:51:16 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:16 +07; 2h 34min ago
    Trigger: Sat 2024-10-12 19:06:00 +07; 21h left
   Triggers: ● systemd-tmpfiles-clean.service
       Docs: man:tmpfiles.d(5)
             man:systemd-tmpfiles(8)

Oct 11 18:51:16 4225a859241c.mylabserver.com systemd[1]: Started Daily Cleanup of Temporary Directories.

● telegrafv2.service - Telegraf
     Loaded: loaded (/usr/lib/systemd/system/telegrafv2.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:50 +07; 2h 34min ago
       Docs: https://github.com/influxdata/telegraf
   Main PID: 825 (telegraf)
      Tasks: 8 (limit: 24437)
     Memory: 44.5M
        CPU: 9.129s
     CGroup: /system.slice/telegrafv2.service
             └─825 /usr/bin/telegraf --config http://4225a859241c.mylabserver.com:8086/api/v2/telegrafs/0dca759669f3c000

Oct 11 21:25:11 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:11Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:11 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:11Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:21 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:21Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:21 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:21Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:31 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:31Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:31 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:31Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:41 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:41Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:41 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:41Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)
Oct 11 21:25:51 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:51Z E! [outputs.influxdb_v2] When writing to [http://4225a859241c.mylabserver.com:8086/api/v2/write]: Post "http://4225a859241c.mylabserver.com:8086/api/v2/write?bucket=grafana-influxdb-bucket&org=MyLabServer": dial tcp 172.31.42.197:8086: connect: connection refused
Oct 11 21:25:51 4225a859241c.mylabserver.com telegraf[825]: 2024-10-11T14:25:51Z E! [agent] Error writing to outputs.influxdb_v2: failed to send metrics to any configured server(s)

● user-runtime-dir@1000.service - User Runtime Directory /run/user/1000
     Loaded: loaded (/usr/lib/systemd/system/user-runtime-dir@.service; static)
     Active: active (exited) since Fri 2024-10-11 18:53:02 +07; 2h 32min ago
       Docs: man:user@.service(5)
   Main PID: 1643 (code=exited, status=0/SUCCESS)
        CPU: 8ms

Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1]: Starting User Runtime Directory /run/user/1000...
Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1]: Finished User Runtime Directory /run/user/1000.

● cloud-init-local.service - Initial cloud-init job (pre-networking)
     Loaded: loaded (/usr/lib/systemd/system/cloud-init-local.service; enabled; preset: disabled)
     Active: active (exited) since Fri 2024-10-11 18:51:26 +07; 2h 34min ago
   Main PID: 615 (code=exited, status=0/SUCCESS)
        CPU: 974ms

Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: 
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: Listening on LPF/eth0/0a:81:64:98:21:6b
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: Sending on   LPF/eth0/0a:81:64:98:21:6b
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: Sending on   Socket/fallback
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: DHCPDISCOVER on eth0 to 255.255.255.255 port 67 interval 4 (xid=0x5be2612e)
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: DHCPOFFER of 172.31.42.197 from 172.31.32.1
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: DHCPREQUEST for 172.31.42.197 on eth0 to 255.255.255.255 port 67 (xid=0x5be2612e)
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: DHCPACK of 172.31.42.197 from 172.31.32.1 (xid=0x5be2612e)
Oct 11 18:51:25 4225a859241c.mylabserver.com dhclient[635]: bound to 172.31.42.197 -- renewal in 1464 seconds.
Oct 11 18:51:26 4225a859241c.mylabserver.com systemd[1]: Finished Initial cloud-init job (pre-networking).

● network-online.target - Network is Online
     Loaded: loaded (/usr/lib/systemd/system/network-online.target; static)
     Active: active since Fri 2024-10-11 18:51:31 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:31 +07; 2h 34min ago
       Docs: man:systemd.special(7)
             https://systemd.io/NETWORK_ONLINE

Oct 11 18:51:31 4225a859241c.mylabserver.com systemd[1]: Reached target Network is Online.

● user@1000.service - User Manager for UID 1000
     Loaded: loaded (/usr/lib/systemd/system/user@.service; static)
    Drop-In: /usr/lib/systemd/system/user@.service.d
             └─10-login-barrier.conf
     Active: active (running) since Fri 2024-10-11 18:53:02 +07; 2h 32min ago
       Docs: man:user@.service(5)
   Main PID: 1644 (systemd)
     Status: "Ready."
      Tasks: 2
     Memory: 2.5M
        CPU: 138ms
     CGroup: /user.slice/user-1000.slice/user@1000.service
             └─init.scope
               ├─1644 /usr/lib/systemd/systemd --user
               └─1645 "(sd-pam)"

Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1644]: Reached target Sockets.
Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1644]: Reached target Basic System.
Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1644]: Reached target Main User Target.
Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1644]: Startup finished in 101ms.
Oct 11 18:53:02 4225a859241c.mylabserver.com systemd[1]: Started User Manager for UID 1000.
Oct 11 18:56:00 4225a859241c.mylabserver.com systemd[1644]: Starting Mark boot as successful...
Oct 11 18:56:00 4225a859241c.mylabserver.com systemd[1644]: Finished Mark boot as successful.
Oct 11 18:59:00 4225a859241c.mylabserver.com systemd[1644]: Created slice User Background Tasks Slice.
Oct 11 18:59:00 4225a859241c.mylabserver.com systemd[1644]: Starting Cleanup of User's Temporary Files and Directories...
Oct 11 18:59:00 4225a859241c.mylabserver.com systemd[1644]: Finished Cleanup of User's Temporary Files and Directories.

● sys-devices-virtual-net-docker0.device - /sys/devices/virtual/net/docker0
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:40 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:40 +07; 2h 34min ago
     Device: /sys/devices/virtual/net/docker0

● sys-module-configfs.device - /sys/module/configfs
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/module/configfs

● systemd-modules-load.service - Load Kernel Modules
     Loaded: loaded (/usr/lib/systemd/system/systemd-modules-load.service; static)
     Active: active (exited) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
       Docs: man:systemd-modules-load.service(8)
             man:modules-load.d(5)
   Main PID: 520 (code=exited, status=0/SUCCESS)
        CPU: 8ms

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Finished Load Kernel Modules.

● var-swap-swapfile.swap - /var/swap/swapfile
     Loaded: loaded (/etc/fstab; generated)
     Active: active since Fri 2024-10-11 18:51:12 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:12 +07; 2h 34min ago
       What: /var/swap/swapfile
       Docs: man:fstab(5)
             man:systemd-fstab-generator(8)
      Tasks: 0 (limit: 24437)
     Memory: 356.0K
        CPU: 11ms
     CGroup: /system.slice/var-swap-swapfile.swap

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Activating swap /var/swap/swapfile...
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Activated swap /var/swap/swapfile.

● multi-user.target - Multi-User System
     Loaded: loaded (/usr/lib/systemd/system/multi-user.target; indirect; preset: disabled)
     Active: active since Fri 2024-10-11 18:54:10 +07; 2h 31min ago
      Until: Fri 2024-10-11 18:54:10 +07; 2h 31min ago
       Docs: man:systemd.special(7)

Oct 11 18:54:10 4225a859241c.mylabserver.com systemd[1]: Reached target Multi-User System.

● alertmanager.service - Prometheus Alertmanager.
     Loaded: loaded (/usr/lib/systemd/system/alertmanager.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:28 +07; 2h 34min ago
       Docs: https://github.com/prometheus/alertmanager
   Main PID: 664 (alertmanager)
      Tasks: 8 (limit: 24437)
     Memory: 21.3M
        CPU: 6.220s
     CGroup: /system.slice/alertmanager.service
             └─664 /usr/bin/alertmanager --config.file=/etc/prometheus/alertmanager.yml --storage.path=/var/lib/prometheus/alertmanager

Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.111Z caller=main.go:181 level=info msg="Starting Alertmanager" version="(version=0.27.0, branch=HEAD, revision=0aa3c2aad14cff039931923ab16b26b7481783b5)"
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.111Z caller=main.go:182 level=info build_context="(go=go1.21.7, platform=linux/amd64, user=root@22cd11f671e9, date=20240228-11:51:20, tags=netgo)"
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.124Z caller=cluster.go:186 level=info component=cluster msg="setting advertise address explicitly" addr=172.31.42.197 port=9094
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.127Z caller=cluster.go:683 level=info component=cluster msg="Waiting for gossip to settle..." interval=2s
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.497Z caller=coordinator.go:113 level=info component=configuration msg="Loading configuration file" file=/etc/prometheus/alertmanager.yml
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.613Z caller=coordinator.go:126 level=info component=configuration msg="Completed loading of configuration file" file=/etc/prometheus/alertmanager.yml
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.631Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9093
Oct 11 18:51:32 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:32.632Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9093
Oct 11 18:51:34 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:34.128Z caller=cluster.go:708 level=info component=cluster msg="gossip not settled" polls=0 before=0 now=1 elapsed=2.001070517s
Oct 11 18:51:42 4225a859241c.mylabserver.com alertmanager[664]: ts=2024-10-11T11:51:42.130Z caller=cluster.go:700 level=info component=cluster msg="gossip settled; proceeding" elapsed=10.003184628s

● integritysetup.target - Local Integrity Protected Volumes
     Loaded: loaded (/usr/lib/systemd/system/integritysetup.target; static)
     Active: active since Fri 2024-10-11 18:51:10 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:10 +07; 2h 34min ago
       Docs: man:systemd.special(7)

● systemd-journald.service - Journal Service
     Loaded: loaded (/usr/lib/systemd/system/systemd-journald.service; static)
     Active: active (running) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
TriggeredBy: ● systemd-journald-dev-log.socket
             ● systemd-journald.socket
       Docs: man:systemd-journald.service(8)
             man:journald.conf(5)
   Main PID: 519 (systemd-journal)
     Status: "Processing requests..."
      Tasks: 1 (limit: 24437)
     Memory: 19.8M
        CPU: 3.029s
     CGroup: /system.slice/systemd-journald.service
             └─519 /usr/lib/systemd/systemd-journald

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd-journald[519]: Journal started
Oct 11 18:51:11 4225a859241c.mylabserver.com systemd-journald[519]: Runtime Journal (/run/log/journal/ec20f5ba53a6e950674ad204defd7591) is 8.0M, max 77.4M, 69.4M free.
Oct 11 18:51:10 4225a859241c.mylabserver.com systemd[1]: systemd-journald.service: Deactivated successfully.
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd-journald[519]: Runtime Journal (/run/log/journal/ec20f5ba53a6e950674ad204defd7591) is 8.0M, max 77.4M, 69.4M free.
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd-journald[519]: Received client request to flush runtime journal.
Oct 11 21:22:10 4225a859241c.mylabserver.com systemd-journald[519]: Data hash table of /run/log/journal/ec20f5ba53a6e950674ad204defd7591/system.journal has a fill level at 75.0 (13212 of 17614 items, 8388608 file size, 634 bytes per hash table item), suggesting rotation.
Oct 11 21:22:10 4225a859241c.mylabserver.com systemd-journald[519]: /run/log/journal/ec20f5ba53a6e950674ad204defd7591/system.journal: Journal header limits reached or header out-of-date, rotating.

● grafana-server.service - Grafana instance
     Loaded: loaded (/usr/lib/systemd/system/grafana-server.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-11 18:51:49 +07; 2h 34min ago
       Docs: http://docs.grafana.org
   Main PID: 1087 (grafana)
      Tasks: 16 (limit: 24437)
     Memory: 235.2M
        CPU: 13.378s
     CGroup: /system.slice/grafana-server.service
             └─1087 /usr/share/grafana/bin/grafana server --config=/etc/grafana/grafana.ini --pidfile=/var/run/grafana/grafana-server.pid --packaging=rpm cfg:default.paths.logs=/var/log/grafana cfg:default.paths.data=/var/lib/grafana cfg:default.paths.plugins=/var/lib/grafana/plugins cfg:default.paths.provisioning=/etc/grafana/provisioning

Oct 11 21:19:43 4225a859241c.mylabserver.com grafana[1087]: logger=live t=2024-10-11T21:19:43.292101492+07:00 level=info msg="Initialized channel handler" channel=grafana/dashboard/uid/000000127 address=grafana/dashboard/uid/000000127
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.54433051+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=1155 duration=1.155421093s size=64 referer="https://4225a859241c.mylabserver.com:3000/d/000000127/telegraf3a-system-dashboard?orgId=1&refresh=1m" handler=/api/ds/query status_source=downstream
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.546299887+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=1156 duration=1.156370271s size=64 referer="https://4225a859241c.mylabserver.com:3000/d/000000127/telegraf3a-system-dashboard?orgId=1&refresh=1m" handler=/api/ds/query status_source=downstream
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.548847929+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=1140 duration=1.140325213s size=64 referer="https://4225a859241c.mylabserver.com:3000/d/000000127/telegraf3a-system-dashboard?orgId=1&refresh=1m" handler=/api/ds/query status_source=downstream
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.548903979+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=944 duration=944.953205ms size=380 referer="https://4225a859241c.mylabserver.com:3000/d/000000127/telegraf3a-system-dashboard?orgId=1&refresh=1m" handler=/api/ds/query status_source=downstream
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.550905767+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=1144 duration=1.144117465s size=64 referer="https://4225a859241c.mylabserver.com:3000/d/000000127/telegraf3a-system-dashboard?orgId=1&refresh=1m" handler=/api/ds/query status_source=downstream
Oct 11 21:19:44 4225a859241c.mylabserver.com grafana[1087]: logger=context userId=1 orgId=1 uname=admin t=2024-10-11T21:19:44.552326059+07:00 level=info msg="Request Completed" method=POST path=/api/ds/query status=400 remote_addr=115.76.54.83 time_ms=38 duration=38.686325ms size=426 referer=https://4225a859241c.mylabserver.com:3000/connections/datasources handler=/api/ds/query status_source=downstream
Oct 11 21:21:49 4225a859241c.mylabserver.com grafana[1087]: logger=cleanup t=2024-10-11T21:21:49.084653436+07:00 level=info msg="Completed cleanup jobs" duration=7.244591ms
Oct 11 21:21:49 4225a859241c.mylabserver.com grafana[1087]: logger=plugins.update.checker t=2024-10-11T21:21:49.765214245+07:00 level=info msg="Update check succeeded" duration=215.501025ms
Oct 11 21:22:41 4225a859241c.mylabserver.com grafana[1087]: logger=infra.usagestats t=2024-10-11T21:22:41.157488356+07:00 level=info msg="Usage stats are ready to report"

● systemd-udevd.service - Rule-based Manager for Device Events and Files
     Loaded: loaded (/usr/lib/systemd/system/systemd-udevd.service; static)
     Active: active (running) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
TriggeredBy: ● systemd-udevd-kernel.socket
             ● systemd-udevd-control.socket
       Docs: man:systemd-udevd.service(8)
             man:udev(7)
   Main PID: 536 (systemd-udevd)
     Status: "Processing with 20 children at max"
      Tasks: 1
     Memory: 5.7M
        CPU: 930ms
     CGroup: /system.slice/systemd-udevd.service
             └─udev
               └─536 /usr/lib/systemd/systemd-udevd

Oct 11 18:51:12 4225a859241c.mylabserver.com systemd[1]: Starting Rule-based Manager for Device Events and Files...
Oct 11 18:51:12 4225a859241c.mylabserver.com systemd-udevd[536]: Using default interface naming scheme 'rhel-9.0'.
Oct 11 18:51:13 4225a859241c.mylabserver.com systemd[1]: Started Rule-based Manager for Device Events and Files.
Oct 11 18:51:13 4225a859241c.mylabserver.com systemd-udevd[550]: Network interface NamePolicy= disabled on kernel command line.
Oct 11 18:51:13 4225a859241c.mylabserver.com lvm[566]: PV /dev/nvme1n1 online, VG vgelk incomplete (need 1).
Oct 11 18:51:13 4225a859241c.mylabserver.com lvm[567]: PV /dev/nvme2n1 online, VG vgelk is complete.
Oct 11 18:51:40 4225a859241c.mylabserver.com systemd-udevd[1091]: Network interface NamePolicy= disabled on kernel command line.
Oct 11 18:51:40 4225a859241c.mylabserver.com systemd-udevd[1019]: Network interface NamePolicy= disabled on kernel command line.
Oct 11 18:51:42 4225a859241c.mylabserver.com systemd-udevd[1307]: Network interface NamePolicy= disabled on kernel command line.

● rngd.service - Hardware RNG Entropy Gatherer Daemon
     Loaded: loaded (/usr/lib/systemd/system/rngd.service; enabled; preset: enabled)
     Active: active (running) since Fri 2024-10-11 18:51:17 +07; 2h 34min ago
   Main PID: 620 (rngd)
      Tasks: 1 (limit: 24437)
     Memory: 3.3M
        CPU: 8.401s
     CGroup: /system.slice/rngd.service
             └─620 /usr/sbin/rngd -f --fill-watermark=0 -x pkcs11 -x nist -x qrypt -D daemon:daemon

Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: Disabling 9: Qrypt quantum entropy beacon (qrypt)
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: Initializing available sources
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: [hwrng ]: Initialization Failed
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: [rdrand]: Enabling RDSEED rng support
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: [rdrand]: Initialized
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: [jitter]: JITTER timeout set to 5 sec
Oct 11 18:51:18 4225a859241c.mylabserver.com rngd[620]: [jitter]: Initializing AES buffer
Oct 11 18:51:23 4225a859241c.mylabserver.com rngd[620]: [jitter]: Unable to obtain AES key, disabling JITTER source
Oct 11 18:51:23 4225a859241c.mylabserver.com rngd[620]: [jitter]: Initialization Failed
Oct 11 18:51:23 4225a859241c.mylabserver.com rngd[620]: Process privileges have been dropped to 2:2

● sys-kernel-debug.mount - Kernel Debug File System
     Loaded: loaded (/proc/self/mountinfo; static)
     Active: active (mounted) since Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:11 +07; 2h 34min ago
      Where: /sys/kernel/debug
       What: debugfs
       Docs: https://docs.kernel.org/filesystems/debugfs.html
             https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems
      Tasks: 0 (limit: 24437)
     Memory: 4.0K
        CPU: 2ms
     CGroup: /sys-kernel-debug.mount

Oct 11 18:51:11 4225a859241c.mylabserver.com systemd[1]: Mounted Kernel Debug File System.

● sys-devices-pnp0-00:04-tty-ttyS0.device - /sys/devices/pnp0/00:04/tty/ttyS0
     Loaded: loaded
     Active: active (plugged) since Fri 2024-10-11 18:51:13 +07; 2h 34min ago
      Until: Fri 2024-10-11 18:51:13 +07; 2h 34min ago
     Device: /sys/devices/pnp0/00:04/tty/ttyS0
