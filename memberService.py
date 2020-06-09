from member import Member
from repository import Repository


class MemberService():
    def get_memberList(self):
        print("LISTAR PERSONAS")
        return Repository.membersList

    def crearMember(self):
        name = input("Ingrese el nombre de la persona: ")
        surname = input("ingrese el apellido de la persona")
        age = int(input("Ingrese una edad: "))
        phone = int(input("Ingrese el numero de telefono: "))
        return Member(name, surname, age, phone)

    def add_member(self, member=None):
        print("\n----AGREGAR PERSONA")
        if member is None:
            member = self.crearLibro
            KeyMember = -1
        for memberKey in Repository.booksList:
            KeyMember = memberKey
        KeyMember = KeyMember + 1
        Repository.memberList[KeyMember] = member.__dict__

    def update_book(self, memberKey=None, member=None):
        print("\n----MODIFICAR PERSONA")
        if memberKey is None:
            memberKey = int(input("Ingrese una key: "))
        if member is None:
            member = self.crearLibro()
        Repository.memberList[memberKey] = member.__dict__

    def delete_member(self, memberKey=None):
        print("\n----ELIMINAR PERSONA")
        if memberKey is None:
            memberKey = int(input("Ingrese una key: "))
        del Repository.membersList[memberKey]
