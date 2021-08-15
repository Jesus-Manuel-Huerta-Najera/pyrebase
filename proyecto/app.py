import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/Plist', 'mvc.controllers.list.List',
    '/Pinsert', 'mvc.controllers.insert.Insert',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()