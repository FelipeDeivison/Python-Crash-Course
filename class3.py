#Importado um modulo do arquivo "class1.py"

# import class1

# felipe = class1.Admin('Felipe', 'Angelo', 23, 'São Paulo', )
# felipe.describe_user()
# print()
# felipe.show_privileges()

#Importsndo a classe "Admin" do modulo "class1.py"

from class1 import Admin

felipe = Admin('Felipe', 'Angelo', 23, 'São Paulo',)
felipe.describe_user()
print()
felipe.show_privileges()

