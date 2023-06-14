from socketify import App

from db import Database

db = Database().conn

app = App()

def get(res, req):
  records = db.execute("select name from groups limit 1").fetchall()

  print(len(records))

  res.send(records)

async def post(res, req):
  data = await res.get_json()

  try:

    query = """
      insert into groups (name, total, saved) 
      values 
        (
          %(name)s, 
          %(total)s, 
          %(saved)s
        ) on conflict (name) do 
      update 
      set 
        (total, saved) = (excluded.total, excluded.saved) returning id
    """

    record = db.execute(query, data).fetchone()
    print(record['id'])

  except RuntimeError: raise RuntimeError(db.DatabaseError)

  else:
    db.commit()

    res.end(True)

  finally:
    print('Transação encerrada')


async def put(res, req):

  try:

    id = req.get_parameter(0)
    
    params = await res.get_json()

    params['id'] = id

    query = "update groups set name = %(name)s where id = %(id)s"

    db.execute(query, params)

    db.commit()

    res.end(True)

  except RuntimeError: 
    raise(RuntimeError)

def delete(res, req):
  db.execute("delete from groups where id = (%s)", (req.get_parameter(0),))
  db.commit()

  res.end(True)

def on_error(error, res, req):
  print(str(error))

  if res != None:
    res.write_status(500).end('Algo deu errado')

app.get("/", get)
app.post("/", post)
app.put("/:id", put)
app.delete("/:id", delete)

app.set_error_handler(on_error)

app.listen(3000)
app.run()
