import sys

def initial_phonebook():
  rows, cols = int(input("plese check initial number of contacts")),5

  phone_book = []
  print(phone_book)
  for i in range(rows):
    print("\nenter contact %d details in the following order (ONLY):"% (i+1))
    print("NOTE: * indicates mandatory fields")
    print("................................................................................")
    temp = []
    for j in range(cols):

     if j== 0:
      temp.append(str(input("enter name*:")))


      if temp[j] == '' or temp[j]=='':
        sys.exit
        "name is a manditory firld. process exiting due to blanks field"
        if j ==1:
          temp.append(int(input("enter number*:")))

          if j == 2:
            temp.append(str(input("enter email address")))

          if j == 3:
            temp.append(str(input("enter date of birth (dd/mm/yy)")))
