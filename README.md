A simple [piku](https://github.com/piku/piku) application to redirect every request from one domain to another.

Useful when you have moved your `piku` app's domain.

Set the old domain in `ENV`:

```
NGINX_INCLUDE_FILE=nginx.conf
NGINX_SERVER_NAME=my-old-domain.com www.my-old-domain.com
```

Set the new domain in `nginx.conf`

```
return 301 $scheme://my-new-domain.com$request_uri;
```

```shell
git remote add piku piku@yourserver.net:redirector
git push piku
```

Replace `my-old-domain.com` and `my-new-domain.com` with your own values.

Replace `yourserver.net` with your Piku instance, and `redirector` with
your custom app name, if desired.
