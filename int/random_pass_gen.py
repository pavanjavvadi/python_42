#program to generate strong mixed alphanumeric random passwords
import uuid,random
passwd = str(uuid.uuid4())
passwd = passwd.replace("-","")
spec = ['!',"@","#","$","%","&","*"]
passwd = str(random.choice(spec)) + str(passwd[:9:4])+str(passwd[9:18:4]).upper()+str(passwd[19:27:4])+str(passwd[28:36:4]).upper()
print("Random Password: ",passwd)
