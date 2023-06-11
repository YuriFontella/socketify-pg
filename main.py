from socketify import App

from db import Database

db = Database()

app = App()

async def home(res, req):
  records = db.query("select name from users limit 2000000")
  records = records.fetchall()

  res.send(records)

app.get("/", home)

app.listen(3000)
app.run()
