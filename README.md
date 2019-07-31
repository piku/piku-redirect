A simple [piku](https://github.com/rcarmo/piku) application to redirect every request from one domain to another.

Useful when you have moved your `piku` app's domain.

```
git remote add piku piku@youserver.net:redirector
git push piku
piku config:set NGINX_SERVER_NAME=your-source-domain.net REDIRECT_URL=https://some-destination-url.net/
```

Replace `your-source-domain.net` and `some-destination-url.net` with your own values.
