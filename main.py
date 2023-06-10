from socketify import App

import psycopg2

conn = psycopg2.connect("user=postgres password=123456 host=localhost dbname=blocks")

cursor = conn.cursor()

app = App()

async def home(res, req):
  cursor.execute("select * from users limit 2000000")
  cursor.fetchall()

  res.end("socketify and psycopg2 - Python")

app.get("/", home)

app.listen(3000)
app.run()