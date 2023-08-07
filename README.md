# LightningRod

An asynchronous command-line parsing servcie built on the [JC parser](https://github.com/kellyjonbrazil/jc)

Output is formatted in JSON.

## Install and Run

LightningRod currently supports a local dev version of the service with `docker`. Begin by cloning this repository.

Run `docker compose up -d`.

If an error occurs with the following message:
```
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json?all=1&filters=%7B%22label%22%3A%7B%22com.docker.compose.config-hash%22%3Atrue%2C%22com.docker.compose.project%3Dlightningrod%22%3Atrue%7D%7D": dial unix /var/run/docker.sock: connect: permission denied 
```
Then, follow these steps under **Manage Docker as a non-root user** at https://docs.docker.com/engine/install/linux-postinstall/.

If migrations are needed, run:
`docker compose run parser python api/manage.py migrate`

The service will be accessible at http://localhost:8000/api/

Once the service has been started, you can access the post, get, and get parsers command through the following curl commands respectively.

New Parse request, `curl --location 'http://localhost:8000/api/submit/?=' \ --form 'parser="blank"' \ --form 'file=@"/path_to_file/blank.txt"'`
    Here replace the 'parser=blank', with the name of the parser you wish to use. Then also replace the 'file=@"/path_to_file/blank.txt" path with the absolute path to the file you wish to run the command with.

Get request, `curl --location 'http://localhost:8000/api/status/?ticket_number=00000000-00000000-00000000-00000000'`
    Here replace the 'ticket_number=00000000-00000000-00000000-00000000', with the ticket provided by any previous post request.

Get parsers, `curl --location 'http://localhost:8000/api/parsers'`

To stop, `docker compose down`

## Testing

LightningRod has unit tests in the tests.py file and currently tests the functions in views.py.

To run tests, use the command `coverage run --source='.' manage.py test parserAPI`

To see the result and coverage, use `coverage report`

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

<details>
<summary>Click to open list of parsers.</summary>
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
    "find",
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
    "lsattr",
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
    "srt",
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
    "veracrypt",
    "vmstat",
    "w",
    "wc",
    "who",
    "x509_cert",
    "x509_csr",
    "xml",
    "xrandr",
    "yaml",
    "zipinfo",
    "zpool_iostat",
    "zpool_status"
  ]
}
```
</details>