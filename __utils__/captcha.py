import string

import random

frasaf = [
  "night",
  "sun",
  "milk",
  "raft",
  "rice",
  "field",
  "chicken"
  ]
  
async def get_captcha():
  
  captc = "".join(random.choice(string.ascii_uppercase) for _ in range(5))
  
  captc += f" {random.choice(frasaf)}"
  
  return captc
