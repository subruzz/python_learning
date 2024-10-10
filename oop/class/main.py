class User:
  """ when we dont want a function or class 
  to do nothing use pass"""
  # pass
  def __init__(self,user_id,user_name) :
    '''here we can use any name we want in the init
    but what we declared below will be accessible through object
    for eg : it wont be user.user_id but user.id'''
    self.id=user_id
    self.user_name=user_name
    self.followers=0
    self.following=0
  
  def follow(self,user):
    user.followers+=1
    self.following+=1
    
     
  
user_1=User('001','subru')
print(user_1.id)
'''adding attribute dynamically like this is not possible in Dart'''
# user_1.id='dslkfjs'
# print(user_1.id)

