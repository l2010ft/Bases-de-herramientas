import base64
from cryptography.fernet import Fernet
import random
class encrp:
   def Encrip_F(Mens):
      key = Fernet.generate_key()
      Enc = Fernet(key)
      Fn = Enc.encrypt(Mens.encode('utf_8'))
      return Fn,key
   def Desencrip_F(Mens,key):
      Enc = Fernet(key)
      Fn = Enc.decrypt(Mens)
      return Fn
   def Encrip_B(Mens):
        Fn = base64.b64encode(Mens.encode('utf_8'))
        return Fn
   def Desencrip_B(Mens):
        Fn = base64.b64decode(Mens)
        return Fn
   def Encrip_C(Mens):
       Ins = base64.b64encode(Mens.encode('utf_8'))
       key = Fernet.generate_key()
       Enc = Fernet(key)
       Mn = Enc.encrypt(Ins)
       return Mn,key
   def Desencrip_C(Mens,key):
         Enc = Fernet(key)
         Mn = Enc.decrypt(Mens)
         Fn = base64.b64decode(Mn)
         return Fn
   def Encrip_D(Mens):
       Item = random.randint(1,50)
       for i in range(Item):
           Key = []
           P =  Fernet.generate_key()
           Key.append(P)
           Enc = Fernet(P)
           Mens = Enc.encrypt(Mens)
   def Desencrip_D(Mens,key):
       for i in range(len(key)):
           Enc = Fernet(key[i])
           Mens = Enc.decrypt(Mens)
       return Mens        

