import shutil

def backup():
    shutil.rmtree("backups/2014")
    shutil.copytree("2014", "backups/2014")

cont = raw_input("Warning: this will delete previous 2014 backup. Continue? y/n: ")
if cont == "y":
    backup()
else:
    pass