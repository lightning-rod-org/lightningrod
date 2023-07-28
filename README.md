# LightningRod

An asynchronous command-line parsing servcie built on the [JC parser](https://github.com/kellyjonbrazil/jc)

Output is formatted in JSON.

## Install and Run

LightningRod currently supports a local dev version of the service with `docker`. Begin by cloning this repository.

Run `docker compose up -d`.

If migrations are needed, run:
`docker compose run parser python api/manage.py migrate`

The service will be accessible at http://localhost:8000/api/

To stop, `docker compose down`

## Endpoints

### POST /submit

Two required fields in the body of the request are `parser` and `file`.

`parser`: This is a string of the selection of how to interpret the command result. See the JC documentation for a list of supported parsers.

`file`: This is the command result that needs to be parsed.

Save the `ticket_number` number value to request the status.

### GET /submit

This returns the status of a submitted ticket. This takes one query parameter.

`ticket_number`: This is the number value returned from the initial POST request.

The output will be reutrned in JSON format in the field `p_output`.

### GET /parsers

Returns a list of parsers that are currently supported under a `parsers` JSON key.

```
{
  "parsers": [
    "acpi",
    "airport",
    "airport_s",
    "arp",
    "asciitable",
    "asciitable_m",
    "blkid",
    "bluetoothctl",
    "cbt",
    "cef",
    "certbot",
    "chage",
    "cksum",
    "clf",
    "crontab",
    "crontab_u",
    "csv",
    "date",
    "datetime_iso",
    "df",
    "dig",
    "dir",
    "dmidecode",
    "dpkg_l",
    "du",
    "email_address",
    "env",
    "file",
    "findmnt",
    "finger",
    "free",
    "fstab",
    "git_log",
    "git_ls_remote",
    "gpg",
    "group",
    "gshadow",
    "hash",
    "hashsum",
    "hciconfig",
    "history",
    "hosts",
    "id",
    "ifconfig",
    "ini",
    "ini_dup",
    "iostat",
    "ip_address",
    "iptables",
    "iw_scan",
    "iwconfig",
    "jar_manifest",
    "jobs",
    "jwt",
    "kv",
    "last",
    "ls",
    "lsblk",
    "lsmod",
    "lsof",
    "lspci",
    "lsusb",
    "m3u",
    "mdadm",
    "mount",
    "mpstat",
    "netstat",
    "nmcli",
    "ntpq",
    "openvpn",
    "os_prober",
    "passwd",
    "pci_ids",
    "pgpass",
    "pidstat",
    "ping",
    "pip_list",
    "pip_show",
    "plist",
    "postconf",
    "proc",
    "ps",
    "route",
    "rpm_qi",
    "rsync",
    "semver",
    "sfdisk",
    "shadow",
    "ss",
    "ssh_conf",
    "sshd_conf",
    "stat",
    "sysctl",
    "syslog",
    "syslog_bsd",
    "systemctl",
    "systemctl_lj",
    "systemctl_ls",
    "systemctl_luf",
    "systeminfo",
    "time",
    "timedatectl",
    "timestamp",
    "toml",
    "top",
    "tracepath",
    "traceroute",
    "udevadm",
    "ufw",
    "ufw_appinfo",
    "uname",
    "update_alt_gs",
    "update_alt_q",
    "upower",
    "uptime",
    "url",
    "ver",
    "vmstat",
    "w",
    "wc",
    "who",
    "x509_cert",
    "xml",
    "xrandr",
    "yaml",
    "zipinfo",
    "zpool_iostat",
    "zpool_status"
  ]
}
```