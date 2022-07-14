# Dash App for Exploring `ccl.net` Message Posting Frequency

*(more description to come)*

To run the app, make sure you have Python 3.10 installed, and then:

For Linux:

```
$ git clone https://github.com/bskinn/ccldb-dash-msgfreqs
$ python3.10 -m venv env
$ source env/bin/activate
$ python -m pip install -r requirements.txt
$ python ccldb_dash_msgfreqs/app.py
```

Python will work for a while, and then provide you with a link.
Browse to this link to view the app. When done, use Ctrl+C to
kill the app's server.


## Notes

Heroku infrastructure adapted (and significantly reduced from)
the Heroku tutorial here:
https://devcenter.heroku.com/articles/flask-memcache

Syntax for the `gunicorn` call and server factory function from:
https://fizzy.cc/deploy-dash-on-server/
