from jsfetch import fetch

res = fetch("http://httpbin.org/uuid").toJSON()
print(res)
res.then(print)
print(res.status_code)
print(res.headers)