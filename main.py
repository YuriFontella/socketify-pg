from socketify import App

from db import Database

db = Database().conn

app = App()

def home(res, req):
  records = db.execute("select name from users limit 1").fetchall()

  print(len(records))

  res.send(records)

app.get("/", home)

app.listen(3000)
app.run()
