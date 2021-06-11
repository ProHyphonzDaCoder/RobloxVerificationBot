import aiosqlite 

async def create_rblx():
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  await cursor.execute("""
  CREATE TABLE IF NOT EXISTS main(
  userid BIGINT DEFAULT 0, 
  robloxid BIGINT DEFAULT 0, 
  verified text DEFAULT no, 
  confirm text NOT NULL,
  PRIMARY KEY(userid)
  )
  """)
  
  await db.commit() 
  await cursor.close()

async def verify(userid, robloxId, verified, confirm):
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  await cursor.execute("INSERT INTO main(userid, robloxid, verified, confirm) values(?,?,?,?)", (userid, robloxId, verified, confirm))
  
  await db.commit() 
  await cursor.close()
  
async def readDB(userid):
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor()
  
  get = await cursor.execute(f"SELECT * FROM main WHERE userid = {userid}")
  
  fetch = await get.fetchone() 
  
  await db.commit() 
  await cursor.close() 
  
  return fetch

async def checkRBLX(rblxId):
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  get = await cursor.execute(f"SELECT * FROM main WHERE robloxid = {rblxId}")
  
  res = await get.fetchall() 
  
  await db.commit() 
  await cursor.close() 
  
  return res 
  
async def update_verify_status(uid, rblxId, v):
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  await cursor.execute("UPDATE main SET verified = ? WHERE userid = ? AND robloxid = ?", (v, uid, rblxId))
  
  await db.commit() 
  await cursor.close()
  
async def logout(uid): 
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  await cursor.execute(f"UPDATE MAIN SET robloxid = 0, verified = 0, confirm='none' WHERE userid = {uid} ")
  
  await db.commit() 
  await cursor.close()
  
async def update_status(uid, rblxID, v, c):
  
  db = await aiosqlite.connect("rblx.sqlite")
  cursor = await db.cursor() 
  
  await cursor.execute("UPDATE MAIN SET robloxid = ?, verified = ?, confirm = ? WHERE userid = ?", (rblxID, v, c, uid)) 
  
  await db.commit() 
  await cursor.close()
