import glob
import os
import sys
import shutil
def Main():
    input_mod = input("Please Write You're .mod file or folder and example.mod(you need check name of .mod file): ")
    if(os.path.isdir("C:\\Program Files(x86)\\Steam\\steamapps\\common\\Toribash\\data\\mod") == True):
        datamod_str = str("C:\\Program Files(x86)\\Steam\\steamapps\\common\\Toribash\\data\\mod")
        shutil.copy(input_mod, datamod_str)
        os._exit(133)
    else:
        print("Toribash Is Not Installed... Pls Install Toribash in this Directory(Steam Version)")
        os._exit(126)
    os._exit(112)

if __name__ == "__main__":
    Main()