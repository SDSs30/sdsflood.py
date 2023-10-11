# sds.py - Coded in Python

## What is SDS flood?
SDS flood  is basically an HTTP Denial of Service attack that affects threaded servers. 

 We send headers periodically (every ~15 seconds) to keep the connections open.
 We never close the connection unless the server does so.

```sds
@asds{sdsflood,
  title = "SDS",
  author = "Dhananjaya Silva",
  journal = "https://syber-defense-system.business.site/",
  year = "2018",
  url = "https://github.com/SDSs30?tab=repositories
}
```

## Install sds.py .

 `sudo pip3 install sds.py`
 `sds example.com`

Install and run sds.py.

If you want to clone using my git page instead of pip,

 `git clone https://github.com/SDSs30?tab=repositories
 `cd sds.py`
 `python3 sds.py example.com`

### SOCKS5 proxy support

If you plan on using the `-x` `PySocks` library (or any other implementation of the `socks` library) as well. [`PySocks`] is a fork from [`SocksiPy``PySocks` to the `pip` 

* `sudo pip3 install PySocks`



## Configuration options 
* -p, --port
* * Port of webserver, usually 80
* -s, --sockets
* * Number of sockets to use in the test
* -v, --verbose
* * Increases logging (output on terminal)
* -ua, --randuseragents
* * Randomizes user-agents with each request
* -x, --useproxy
* * Use a SOCKS5 proxy for connecting
* --https
* * Use HTTPS for the requests
* --sleeptime
* * Time to sleep between each header sent

## License
The code is licensed under the MIT License.

