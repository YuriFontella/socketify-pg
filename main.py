from socketify import App
from psycopg.rows import dict_row

import psycopg

conn = psycopg.connect("user=postgres password=123456 host=localhost dbname=blocks", row_factory=dict_row)

cursor = conn.cursor()

app = App()

async def home(res, req):
  cursor.execute("select name from users limit 1")
  records = cursor.fetchall()

  res.send(records)

app.get("/", home)

app.listen(3000)
app.run()
