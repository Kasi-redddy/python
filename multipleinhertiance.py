class Father():
    def gardening(self):
        print("I enjoy gardening")
  
class mother():
    def cooking(self):
        print("i enjoy cookimng")
    
class child(Father,mother):
    def sports(self):
        print("i enjoy sports")   
c=child()   
c.gardening()
c.cooking()
c.sports()                     
        
        