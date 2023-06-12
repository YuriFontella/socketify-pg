from socketify import App

from db import Database

db = Database().conn

app = App()

def get(res, req):
  records = db.execute("select name from users limit 1").fetchall()

  print(len(records))

  res.send(records)

async def post(res, req):
  data = await res.get_json()

  try:

    db.execute('insert into groups (name, total, saved) values (%(name)s, %(total)s, %(saved)s)', data)

  except: res.end(False)

  finally:

    db.commit()

    res.end(True)

app.get("/", get)
app.post("/", post)

app.listen(3000)
app.run()
