#!/usr/bin/env python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# author: Arne Preuß
# github: sl0wl1
# email: arne.preuss@posteo.de
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import exifread
import os
import time

# C:\\Users\\arne_\\OneDrive\\Python_projects\\Automate\\safety

def rename_files_temporarily(list_of_files, data_type = ".jpg"):

    """
    This function renames all files in the current working directory with a temporary file ending.
    After that, the files can be sorted and renamed. A rename_files_definitly() call 
    should follow for end result.
    """
        
    #index for "for file in list_of_files" loop
    index_a = 1

    # loops over every file in wd
    for file in list_of_files:
        
        # open files
        f = open(file, "rb")

        # EXIF tag read out
        tags = exifread.process_file(f, stop_tag = "DateTimeOriginal")
        f.close()
        
        # loops over tags
        for tag in tags.keys():     

            if tag == "EXIF DateTimeOriginal":
                
                # converts the tag type object into a string
                date_time = str(tags[tag])
                
                # using string slice to extract date from date_time for for temporary file name
                # the files need a temporary ending, otherwise they cannot be renamed
                temporary_file_name = f"{date_time[0:4]}{date_time[5:7]}{date_time[8:10]}_{index_a}_temporary_ending{input_data_type}"
                
                index_a +=1

                os.rename(file, temporary_file_name)

    
def rename_files_definitly(list_of_files, data_type = ".jpg"):

    """
    The function definitly changes the file names with the correct index.
    The temporary ending gets deleted. The temporary ending was neccessary for sorting
    the list and to avoid name clashes while renaming.
    """
    
    # sortes the files with the same time stamp  
    sorted_files = sorted(list_of_files)
    
    # index counter for definitly renaming
    index_b = 1

    # index counter for the sorted_list
    counting_index = 0
    
    for file in sorted_files:

        # the very first file in the list get its correct renaming
        # this if-statement should be executed only once        
        if file == sorted_files[0]:

            new_file_name = f"{file[:8]}_{index_b}{data_type}"
            os.rename(file, new_file_name) 


        # the if-statement checks if the current file in the loop has the same time stamp as the file one loop before.
         # if a definitly renamed file with the same time stamp exists in the list, the index is increased 
        elif file[0:8] == sorted_files[counting_index][0:8]:
            
            index_b += 1
            new_file_name = f"{file[:8]}_{index_b}{data_type}"
            os.rename(file, new_file_name)

            counting_index += 1

        # if there is no definitly renamed file with the same time stamp, the index is set to 1 again
        else:

            index_b = 1
            new_file_name = f"{file[:8]}_{index_b}{data_type}"
            os.rename(file, new_file_name)
            counting_index += 1

def main():

    print("***************Caution***************\n")
    print("Please cosnider that the directory should only contain the photo files!")
    print("The renaming is permanent. You cannot undo it with this program\n")
    print("*************************************\n")
    
    input_path = input("Please enter path: ")
    input_data_type = input("Please enter a data type (e.g.: .jpg, .png,....): ")

    # setting working directory (wd)
    os.chdir(input_path) 
    

    # lists every file in current wd
    file_list = os.listdir()
    
    rename_files_temporarily(file_list, input_data_type)

    # lists again every file in current wd after renaming
    file_list_after_renaming = os.listdir()

    rename_files_definitly(file_list_after_renaming, input_data_type)


    print("Done!")     
        
            
if __name__ == "__main__":
    for i in range(1,10):
        print(i)
        time.sleep(0.5)
    
    main()


                
                
                
                
                
                
