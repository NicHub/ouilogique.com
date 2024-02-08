import base64

favicon_path = "favicon.svg"


with open(favicon_path, "rt") as _f:
    favicon = _f.read()
faviconb64 = base64.b64encode(bytes(favicon, "utf-8")).decode("utf-8")
print(f"""<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,{faviconb64}">""")


