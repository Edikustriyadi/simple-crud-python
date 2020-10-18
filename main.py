class Person:
    data = []
    chooseMenu = ''

    def __init__(self):
        pass

    def menu(self):
        print('---- Menu Person ---- ')
        print('1. Create')
        print('2. View')
        print('3. Edit')
        print('4. Delete')
        self.chooseMenu = int(input("Input menu : "))
        if self.chooseMenu == 1:
            self.create()
        elif self.chooseMenu == 2:
            self.view()
        elif self.chooseMenu == 3:
            self.edit()
        elif self.chooseMenu == 4:
            self.delete()
        else:
            print('Menu not found')

    def create(self):
        self.name = str(input('Input Name : '))
        self.age = int(input('Input Age : '))
        if self.age <= 5:
            self.status = 'Toddler'
        elif self.age >= 6 and self.age <= 10:
            self.status = 'Kids'
        elif self.age >= 11 and self.age <= 17:
            self.status = 'Teenager'
        elif self.age >= 18 and self.age <= 30:
            self.status = 'Adult'
        elif self.age >= 31 and self.age <= 50:
            self.status = 'Parents'
        elif self.age >= 51 and self.age <= 120:
            self.status = 'Old'
        else:
            self.status = 'Nothing'
        self.data.append([self.name, self.age, self.status])
        print('Data has been saved')
        self.menu()

    def view(self):
        if len(self.data) > 0:
            for i in self.data:
                print('Name     : ', i[0])
                print('Age      : ', i[1])
                print('Status   : ', i[2])
                print('-----------------')
        else:
            print('|-------------|')
            print('| Empty Person! |')
            print('|-------------|')
        self.menu()

    def edit(self):
        self.view()
        self.search = str(input('Search Name : '))
        for i in self.data:
            if i[0] == self.search:
                self.name = str(input('Input Name : '))
                self.age = int(input('Input Age : '))
                if self.age <= 5:
                    self.status = 'Balita'
                elif self.age >= 6 and self.age <= 10:
                    self.status = 'Anak-anak'
                elif self.age >= 11 and self.age <= 17:
                    self.status = 'Remaja'
                elif self.age >= 18 and self.age <= 30:
                    self.status = 'Dewasa'
                elif self.age >= 31 and self.age <= 50:
                    self.status = 'Tua'
                elif self.age >= 51 and self.age <= 100:
                    self.status = 'Lansia'
                else:
                    self.status = 'Nothing'
                i[0] = self.name
                i[1] = self.age
                i[2] = self.status
                self.menu()
            else:
                print('not found')

    def delete(self):
        self.view()
        self.search = str(input('Find Name for delete : '))
        for i in self.data:
            if i[0] == self.search:
                self.data.remove(i)
                print('' + self.search + ' success delete')
        self.view()

t = Person()
t.menu()
