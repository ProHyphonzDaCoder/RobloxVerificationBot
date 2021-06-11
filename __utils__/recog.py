import aiohttp

from __utils__ import userdb

import json

async def send_req(robloxName, types, ids = 0):
  
  URL_Post = "https://users.roblox.com/v1/usernames/users"
  
  async with aiohttp.ClientSession() as ses:
    
    if types.lower() == 'get_name':
        
      get_url_name = f"https://users.roblox.com/v1/users/{ids}"
      
      get_name = await ses.get(get_url_name) 
      
      fetch_name = await get_name.json() 
      
      try: 
        
        name = fetch_name["displayName"]
        
        return name 
        
      except IndexError:
        
        return ":x: **| User not found.**"
        
    if types.lower() == "after_code":
      
      try:
        
        get_url = f"https://users.roblox.com/v1/users/{ids}"
        
        get_bio = await ses.get(get_url)
        
        fetch_bio = await get_bio.json() 
        
        try:
          
          bio = fetch_bio["description"]
          return bio 
          
        except IndexError: 
          
          return ":x: | **Roblox users not found.**"
        
      except IndexError:
        
        return ":x: | **Roblox users not found.**"  
    
    user = {
      "usernames": [
        f"{robloxName}"
      ],
      "excludeBannedUser": False
    }
    
    send_reqs = await ses.post(URL_Post, data = user)
    
    resp = await send_reqs.json()
    
    
    try:
      
      data = resp["data"][0]["id"]
    
      return data
      
    except IndexError:
      
      return ":x: | **Roblox users not found.**"
