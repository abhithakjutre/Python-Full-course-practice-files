Q : 6 # Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects. 


from random import randint
class Train:

    def __init__(slf,trainNo):
        slf.trainNo = trainNo
        
    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(harry):
        print(f"Train no:{harry.trainNo} to running on time")

    def getFare(self, fro,to):
        print(f"Ticket is fare in train no:{self.trainNo} from {fro} to {to} is {randint(222, 5555)} ")

t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")

