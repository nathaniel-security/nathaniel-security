import os
import random
# git@github.com:nathaniel-security/nathaniel-security.git
from datetime import date

today = date.today()
#print("Today's date:", today)
current_active_date = "Latest Activity " + str(today)
#print(current_active_date)

#1 * * * * /usr/bin/python3 /home/groot/code/nathaniel-repo/main.py
data = '''
- 👋 Hi, I’m @nathaniel-security
- 👀 I’m interested in cybersecuirty
- 🌱 I’m currently learning networking
- 📫 How to reach me contact@wehost.co.in

- For More info you can visit wehost.co.in/links



<!---
nathaniel-security/nathaniel-security is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

'''

data = data + str(current_active_date)
data = data + "\n" + "<!---"
data = data + str(round(random.random()*1000))
data = data + "--->"
data = data + "\n"

#print(data)

#path = '/home/groot/code/nathaniel-repo/nathaniel-security/'
#os.chdir(path)

os.system('rm README.md')
with open("README.md", "w") as file:
    file.write(data)

os.system("git add .")

os.system('git commit -m "UPDATE"')
os.system("git status")
os.system("sudo git push")
