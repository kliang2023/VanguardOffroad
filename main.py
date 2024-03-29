import os 
import re

#Move directory to where all the Images are 
image_dir = "C:\\Users\\Admin\\Desktop\\vanguardphotos"
os.chdir(image_dir)

#Gets all the file names into a variable called file_list
file_list = os.listdir()

#Rename the files from PartNumber.Suffix.jpg/png -> PartNumber_Suffix.jpg/png
def rename_period():
    for filename in file_list:
        if filename.endswith((".jpg" , ".png")):
            parts = filename.split(".") #PN_a.jpg correct should be two parts
            if "(" in filename:
                print(f"Duplicate file found {filename}")
            elif len(parts) == 3 and len(parts[1]) == 1: #PN.a.jpg and duplicate naming
                part_number , suffix = parts[0] , parts[1]
                extension = parts[-1]
                new_filename = f"{part_number}_{suffix}.{extension}"
                old_path = os.path.join(image_dir, filename)
                new_path = os.path.join(image_dir, new_filename)
                if not os.path.exists(new_path):
                    #os.rename(old_path, new_path)
                    print(f"Renamed {filename} to {new_filename}")
                    continue
                else:
                    print(f"Skipped renaming {filename} (file {new_filename} already exists)")
            #still have to worry about PN-a.jpg and PN__a.jpg
            elif len(parts)==2 and parts[0][-2] == '-':
                part_number = parts[0][0:-2]
                suffix = parts[0][-1]
                extension = parts[1]
                new_filename = f"{part_number}_{suffix}.{extension}"
                old_path = os.path.join(image_dir, filename)
                new_path = os.path.join(image_dir, new_filename)
                if not os.path.exists(new_path):
                    print(f"Renamed {filename} to {new_filename}")
                    continue
                else:
                    print(f"Skipped renaming {filename} (file {new_filename} already exists)")
            elif len(parts)==2 and parts[0][-2]=="_" and parts[0][-3]=='_':
                part_number = parts[0][0:-3]
                suffix = parts[0][-1]
                extension = parts[1]
                new_filename = f"{part_number}_{suffix}.{extension}"
                old_path = os.path.join(image_dir, filename)
                new_path = os.path.join(image_dir, new_filename)
                if not os.path.exists(new_path):
                    print(f"Renamed {filename} to {new_filename}")
                else:
                    print(f"Skipped renaming {filename} (file {new_filename} already exists)")
            #elif len(filename.split("_"))==2 or len(filename.split("_"))==1: #naming should be correct
                #continue
            #else: print(f"{filename} should be correct")
rename_period()