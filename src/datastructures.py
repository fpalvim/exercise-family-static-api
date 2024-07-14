
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []
        self.next_id = 1

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member.last_name = self.last_name
        member.id = self.next_id
        self.next_id = self.next_id +1
        self._members.append(member)
        

    def delete_member(self, id):
        # fill this method and update the return
        # def func(x):
        #     return x.id != id
        # self._members = filter(func, self._members)
        for i, member in enumerate(self._members):
            if member.id == id:
                del self._members[i]
                return member


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member.id == id:
                return member.to_dict()

    # this method is done, it returns a list with all the family members
    # def get_all_members(self):
    #     return self._members
    
    def get_all_members(self):
        return [member.to_dict() for member in self._members]

class FamilyMember:
    last_name = None
    id = None
    def __init__(self, first_name, age, lucky_numbers):
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
            # "last_name": self.last_name,
            "lucky_numbers": self.lucky_numbers
        }
    
    def __str__(self):
        return f"{self.first_name} {self.age} {self.last_name}"