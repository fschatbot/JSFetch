# JSFetch

**JSFetch** is a simple python library that allows you to make HTTP requests in python exactly the way you would in JavaScript. This allows for sending in requests faster and easier than it's competitors. You also get access to a lot of inbuilt functions to lower the amount of code you need to write.

```python
>>> from jsfetch import fetch
>>> res = fetch("http://httpbin.org/uuid").toJSON()
Promise {<fulfilled>: {…}}
>>> res.then(print)
{uuid: '41ddb42d-5d13-406a-a7f1-8fa0419c9267'}
>>> res.status_code
200
>>> res.headers
{'content-type': 'application/json'}
```

## Installing Requests and Supported Versions

JSFetch is available on PyPI:

```console
$ pip install JSFetch --upgrade
```

JSFetch is currently only tested on Python 3.10 and above.

## Todo

- Static Type the language
- Make the fetch function return a proper promise
- Callbacks to be given more data than just the mapped data
- A fetch class for making requests and returning a promises
- Fetch should be able to be called in top level without async and can be blocking in that use
- Fetch can be awaitable when called in an async function and also not be blocking
