### Comprehensive lab parser ### 
from lab_parser import * 
from tar_file import *
import shutil, os, argparse


def move_files(filename, src_folder):
    shutil.copy(filename[:-6] + ".xml", src_folder + "/sequential")
    for f in os.listdir("html"):
        shutil.copy("html/" + f, src_folder + "/html")
    for f in os.listdir("vertical"):
        shutil.copy("vertical/" + f, src_folder + "/vertical")

def stage_files(args, lst):
    path = "bjc-r/topic/berkeley_bjc/"
    print(args)
    if args == "":
        print(os.listdir(path))
        for folder in os.listdir(path):
            if "." not in folder:
                for f in os.listdir(path + "/" + folder):
                    if ".topic" in f:
                        lst.append(path + folder + "/" + f)
    else:
        for f in args:
            if ".topic" in f:
                for folder in os.listdir(path):
                    if ".topic" not in folder:
                        if f in os.listdir(path + folder):
                            lst.append(path + folder + "/" + f)
            else:
                for filename in os.listdir(path + f):
                    lst.append(path + f + "/" + filename)
    return lst


def bjc_to_edx(source, destination, files):
    for f in files:
        psuedo_topic = f.rsplit('/', 1)[1]
        print("Adding lab " + psuedo_topic + "...")
        prepare_file(psuedo_topic, destination)
        shutil.copy(f, psuedo_topic)
        convert_lab(psuedo_topic, destination)
        os.remove(destination + "/" + psuedo_topic)
        os.remove(psuedo_topic) #figure out why this is being created in the first place
        print("Parsed lab " + psuedo_topic + '.\n')

    print("Creating new .tar.gz file for import...")
    tarred_file = destination + ".tar.gz"
    if os.path.exists(tarred_file):
        os.remove(tarred_file)

    make_tarfile(tarred_file, destination)
    print("Course file ready for import.")




def main():
    """
    Parses command line arguments and runs the script appropriately.
    If nothing is passed in, the default values are used.
    """
    parser = argparse.ArgumentParser(
            description="Translates content from HTML source to edX compatible one based on XML.")
    parser.add_argument("-S", "--source", type=str, default="bjc-r",
            help="name of source folder")
    parser.add_argument("-O", "--destination", type=str, default="Course",
            help="name of the destination folder")
    parser.add_argument("-F", "--file", type=str, nargs='+', default="",
            help="files to parse")
    args = parser.parse_args()


    if args.source not in os.listdir('.'):
        print("---bjc-r folder not found in current directory. Parsing cancelled.")
        print("Closing program...")
        sys.exit()
    if args.destination not in os.listdir('.'):
        y, n = True, False
        temp = input("edX course folder '" + args.destination + "' not found. Create new folder in this directory? (y/n)")
        if temp:
            os.mkdir(args.destination)
        else:
            print("---edX course folder not found in current directory. Parsing cancelled.")
            print("Closing program...")
            sys.exit()


    files= []
    stage_files(args.file, files)
    print(files)


    # call parser
    bjc_to_edx(args.source, args.destination, files)



# begin execution if we are running this file directly
if __name__ == "__main__":
    main()