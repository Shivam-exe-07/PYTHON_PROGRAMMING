##########################################################
#
#  CVFS - Custom Virtual File System
#
##########################################################

import os
import sys

##########################################################
#
#  Constants / Macros
#
##########################################################

MAXFILESIZE = 50
MAXOPENFILES = 20
MAXINODE = 5

READ = 1
WRITE = 2
EXECUTE = 4

START = 0
CURRENT = 1
END = 2

EXECUTE_SUCCESS = 0

REGULARFILE = 1
SPECIALFILE = 2

# Error codes
ERR_INVALID_PARAMETER = -1
ERR_NO_INODES = -2
ERR_FILE_ALREADY_EXIST = -3
ERR_FILE_NOT_EXIST = -4
ERR_PERMISSION_DENIED = -5
ERR_INSUFFICIENT_SPACE = -6
ERR_INSUFFICIENT_DATA = -7
ERR_MAX_FILES_OPEN = -8


##########################################################
#
#  Class Name  : BootBlock
#  Description : Holds the information to boot the OS
#
##########################################################

class BootBlock:
    def __init__(self):
        self.Information = ""


##########################################################
#
#  Class Name  : SuperBlock
#  Description : Holds the information about the file system
#
##########################################################

class SuperBlock:
    def __init__(self):
        self.TotalInodes = 0
        self.FreeInodes = 0


##########################################################
#
#  Class Name  : Inode
#  Description : Holds the information about a file
#
##########################################################

class Inode:
    def __init__(self):
        self.FileName = ""
        self.InodeNumber = 0
        self.FileSize = 0
        self.ActualFileSize = 0
        self.FileType = 0
        self.ReferenceCount = 0
        self.Permission = 0
        self.Buffer = None   # Will be a bytearray
        self.next = None     # Linked list pointer


##########################################################
#
#  Class Name  : FileTable
#  Description : Holds the information about an opened file
#
##########################################################

class FileTable:
    def __init__(self):
        self.ReadOffset = 0
        self.WriteOffset = 0
        self.Mode = 0
        self.ptrinode = None   # Points to an Inode


##########################################################
#
#  Class Name  : UAREA
#  Description : Holds the information about process files
#
##########################################################

class UAREA:
    def __init__(self):
        self.ProcessName = ""
        self.UFDT = [None] * MAXOPENFILES   # Array of FileTable pointers


##########################################################
#
#  Global objects
#
##########################################################

bootobj = BootBlock()
superobj = SuperBlock()
uareaobj = UAREA()
head = None   # Head of the inode linked list


##########################################################
#
#  Function Name : initialise_uarea
#  Description   : Initialise UAREA members
#
##########################################################

def initialise_uarea():
    uareaobj.ProcessName = "Myexe"
    for i in range(MAXOPENFILES):
        uareaobj.UFDT[i] = None
    print("CVFS : UAREA gets initialised successfully")


##########################################################
#
#  Function Name : initialise_super_block
#  Description   : Initialise SuperBlock members
#
##########################################################

def initialise_super_block():
    superobj.TotalInodes = MAXINODE
    superobj.FreeInodes = MAXINODE
    print("CVFS : Super block gets initialised successfully")


##########################################################
#
#  Function Name : create_dilb
#  Description   : Create linked list of Inodes
#
##########################################################

def create_dilb():
    global head

    head = None
    temp = None

    for i in range(1, MAXINODE + 1):
        newn = Inode()
        newn.FileName = ""
        newn.InodeNumber = i
        newn.FileSize = 0
        newn.ActualFileSize = 0
        newn.FileType = 0
        newn.ReferenceCount = 0
        newn.Permission = 0
        newn.Buffer = None
        newn.next = None

        if head is None:
            head = newn
            temp = head
        else:
            temp.next = newn
            temp = temp.next

    print("CVFS : DILB created successfully")


##########################################################
#
#  Function Name : start_auxillary_data_initialisation
#  Description   : Initialise all auxillary data
#
##########################################################

def start_auxillary_data_initialisation():
    bootobj.Information = "Booting process of CVFS is done"
    print(bootobj.Information)

    initialise_super_block()
    create_dilb()
    initialise_uarea()

    print("CVFS : Auxillary data initialised successfully")


##########################################################
#
#  Function Name : display_help
#  Description   : Display the help page
#
##########################################################

def display_help():
    print("-----------------------------------------------")
    print("------------CVFS Project Help Page ------------")
    print("-----------------------------------------------")
    print("man    : It is used to display manual page")
    print("clear  : It is used to clear the terminal")
    print("creat  : It is used to create new file")
    print("write  : It is used to write the data into file")
    print("read   : It is used to read the data from the file")
    print("stat   : It is used to display statistical information")
    print("unlink : It is used to delete the file")
    print("exit   : It is used to terminate CVFS")
    print("-----------------------------------------------")


##########################################################
#
#  Function Name : man_page_display
#  Description   : Display the manual page for a command
#
##########################################################

def man_page_display(name):
    if name == "ls":
        print("About : It is used to list the names of all files")
        print("Usage : ls")
    elif name == "man":
        print("About : It is used to display manual page")
        print("Usage : man command_name")
        print("command_name : It is the name of command")
    elif name == "exit":
        print("About : It is used to terminate the shell")
        print("Usage : exit")
    elif name == "clear":
        print("About : It is used to clear the shell")
        print("Usage : clear")
    else:
        print(f"No manual entry for {name}")


##########################################################
#
#  Function Name : is_file_exist
#  Description   : Check whether file already exists
#  Returns       : True or False
#
##########################################################

def is_file_exist(name):
    temp = head
    while temp is not None:
        if temp.FileName == name and temp.FileType == REGULARFILE:
            return True
        temp = temp.next
    return False


##########################################################
#
#  Function Name : create_file
#  Description   : Create a new regular file
#  Input         : File name and permission
#  Output        : File descriptor (int) or error code
#
##########################################################

def create_file(name, permission):
    global superobj

    temp = head

    print(f"Total number of Inodes remaining : {superobj.FreeInodes}")

    if not name:
        return ERR_INVALID_PARAMETER

    if permission < 1 or permission > 3:
        return ERR_INVALID_PARAMETER

    if superobj.FreeInodes == 0:
        return ERR_NO_INODES

    if is_file_exist(name):
        return ERR_FILE_ALREADY_EXIST

    # Find empty inode
    while temp is not None:
        if temp.FileType == 0:
            break
        temp = temp.next

    if temp is None:
        print("There is no inode")
        return ERR_NO_INODES

    # Find empty UFDT entry (0, 1, 2 reserved for stdin/stdout/stderr)
    fd = -1
    for i in range(3, MAXOPENFILES):
        if uareaobj.UFDT[i] is None:
            fd = i
            break

    if fd == -1:
        return ERR_MAX_FILES_OPEN

    # Allocate and initialise file table
    uareaobj.UFDT[fd] = FileTable()
    uareaobj.UFDT[fd].ReadOffset = 0
    uareaobj.UFDT[fd].WriteOffset = 0
    uareaobj.UFDT[fd].Mode = permission

    # Connect file table with inode
    uareaobj.UFDT[fd].ptrinode = temp

    # Initialise inode
    uareaobj.UFDT[fd].ptrinode.FileName = name
    uareaobj.UFDT[fd].ptrinode.FileSize = MAXFILESIZE
    uareaobj.UFDT[fd].ptrinode.ActualFileSize = 0
    uareaobj.UFDT[fd].ptrinode.FileType = REGULARFILE
    uareaobj.UFDT[fd].ptrinode.ReferenceCount = 1
    uareaobj.UFDT[fd].ptrinode.Permission = permission

    # Allocate buffer for file data
    uareaobj.UFDT[fd].ptrinode.Buffer = bytearray(MAXFILESIZE)

    superobj.FreeInodes -= 1

    return fd


##########################################################
#
#  Function Name : ls_file
#  Description   : List all files
#
##########################################################

def ls_file():
    temp = head

    if superobj.FreeInodes == MAXINODE:
        print("Error : There are no files")
        return

    print("-----------------------------------------------")
    print("File Name\tInode number\tFile size\tLink count")
    print("-----------------------------------------------")

    while temp is not None:
        if temp.FileType != 0:
            print(f"{temp.FileName}\t\t{temp.InodeNumber}\t\t{temp.ActualFileSize}\t\t{temp.ReferenceCount}")
        temp = temp.next

    print("-----------------------------------------------")


##########################################################
#
#  Function Name : unlink_file
#  Description   : Delete a file
#  Input         : File name
#  Output        : EXECUTE_SUCCESS or error code
#
##########################################################

def unlink_file(name):
    if not name:
        return ERR_INVALID_PARAMETER

    if not is_file_exist(name):
        return ERR_FILE_NOT_EXIST

    for i in range(MAXOPENFILES):
        if uareaobj.UFDT[i] is not None:
            if uareaobj.UFDT[i].ptrinode.FileName == name:
                # Free buffer
                uareaobj.UFDT[i].ptrinode.Buffer = None

                # Reset inode values
                uareaobj.UFDT[i].ptrinode.FileSize = 0
                uareaobj.UFDT[i].ptrinode.ActualFileSize = 0
                uareaobj.UFDT[i].ptrinode.FileType = 0
                uareaobj.UFDT[i].ptrinode.ReferenceCount = 0
                uareaobj.UFDT[i].ptrinode.Permission = 0
                uareaobj.UFDT[i].ptrinode.FileName = ""

                # Remove file table entry
                uareaobj.UFDT[i] = None

                superobj.FreeInodes += 1
                break

    return EXECUTE_SUCCESS


##########################################################
#
#  Function Name : write_file
#  Description   : Write data into a file
#  Input         : File descriptor, data string, size
#  Output        : Number of bytes written or error code
#
##########################################################

def write_file(fd, data, size):
    print(f"File Descriptor : {fd}")
    print(f"Data that we want to write : {data}")
    print(f"Number of bytes that we want to write : {size}")

    if fd < 0 or fd >= MAXOPENFILES:
        return ERR_INVALID_PARAMETER

    if uareaobj.UFDT[fd] is None:
        return ERR_FILE_NOT_EXIST

    if uareaobj.UFDT[fd].ptrinode.Permission < WRITE:
        return ERR_PERMISSION_DENIED

    if (MAXFILESIZE - uareaobj.UFDT[fd].WriteOffset) < size:
        return ERR_INSUFFICIENT_SPACE

    # Write data into buffer at write offset
    encoded = data[:size].encode('utf-8', errors='replace')
    write_pos = uareaobj.UFDT[fd].WriteOffset
    uareaobj.UFDT[fd].ptrinode.Buffer[write_pos:write_pos + size] = encoded[:size]

    # Update offsets
    uareaobj.UFDT[fd].WriteOffset += size
    uareaobj.UFDT[fd].ptrinode.ActualFileSize += size

    return size


##########################################################
#
#  Function Name : read_file
#  Description   : Read data from a file
#  Input         : File descriptor, size to read
#  Output        : (bytes_read, data_string) or error code
#
##########################################################

def read_file(fd, size):
    if fd < 0 or fd >= MAXOPENFILES:
        return ERR_INVALID_PARAMETER, None

    if size <= 0:
        return ERR_INVALID_PARAMETER, None

    if uareaobj.UFDT[fd] is None:
        return ERR_FILE_NOT_EXIST, None

    if uareaobj.UFDT[fd].ptrinode.Permission < READ:
        return ERR_PERMISSION_DENIED, None

    if (MAXFILESIZE - uareaobj.UFDT[fd].ReadOffset) < size:
        return ERR_INSUFFICIENT_DATA, None

    read_pos = uareaobj.UFDT[fd].ReadOffset
    raw = uareaobj.UFDT[fd].ptrinode.Buffer[read_pos:read_pos + size]
    data = raw.decode('utf-8', errors='replace')

    uareaobj.UFDT[fd].ReadOffset += size

    return size, data


##########################################################
#
#  Main entry point
#
##########################################################

def main():
    start_auxillary_data_initialisation()

    print("-----------------------------------------------")
    print("------- CVFS Project started successfully ------")
    print("-----------------------------------------------")

    while True:
        try:
            user_input = input("\nCVFS : > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nThank you for using CVFS Project")
            break

        if not user_input:
            continue

        parts = user_input.split()
        i_count = len(parts)

        if i_count == 1:
            cmd = parts[0]

            if cmd == "exit":
                print("Thank you for using CVFS Project")
                print("Deallocating all the allocated resources")
                break

            elif cmd == "ls":
                ls_file()

            elif cmd == "help":
                display_help()

            elif cmd == "clear":
                os.system("cls" if os.name == "nt" else "clear")

            else:
                print("Command not found")
                print("Please refer help option to get more information")

        elif i_count == 2:
            cmd, arg1 = parts[0], parts[1]

            if cmd == "man":
                man_page_display(arg1)

            elif cmd == "unlink":
                i_ret = unlink_file(arg1)

                if i_ret == ERR_INVALID_PARAMETER:
                    print("Error : Invalid Parameter")
                elif i_ret == ERR_FILE_NOT_EXIST:
                    print("Error : Unable to delete as there is no such file")
                elif i_ret == EXECUTE_SUCCESS:
                    print("File gets successfully deleted")

            elif cmd == "write":
                try:
                    fd = int(arg1)
                except ValueError:
                    print("Error : Invalid file descriptor")
                    continue

                input_buffer = input("Enter the data that you want to write : \n")
                i_ret = write_file(fd, input_buffer, len(input_buffer))

                if i_ret == ERR_INVALID_PARAMETER:
                    print("Error : Invalid Parameter")
                elif i_ret == ERR_FILE_NOT_EXIST:
                    print("Error : There is no such file")
                elif i_ret == ERR_PERMISSION_DENIED:
                    print("Error : Unable to write as there is no permission")
                elif i_ret == ERR_INSUFFICIENT_SPACE:
                    print("Error : Unable to write as there is no space")
                else:
                    print(f"{i_ret} bytes gets successfully written")

            else:
                print("There is no such command")

        elif i_count == 3:
            cmd, arg1, arg2 = parts[0], parts[1], parts[2]

            if cmd == "creat":
                try:
                    permission = int(arg2)
                except ValueError:
                    print("Error : Permission must be a number")
                    continue

                i_ret = create_file(arg1, permission)

                if i_ret == ERR_INVALID_PARAMETER:
                    print("Error : Unable to create the file as parameters are invalid")
                    print("Please refer man page")
                elif i_ret == ERR_NO_INODES:
                    print("Error : Unable to create file as there are no inodes")
                elif i_ret == ERR_FILE_ALREADY_EXIST:
                    print("Error : Unable to create file because the file is already present")
                elif i_ret == ERR_MAX_FILES_OPEN:
                    print("Error : Unable to create file")
                    print("Max opened files limit reached")
                else:
                    print(f"File gets successfully created with fd : {i_ret}")

            elif cmd == "read":
                try:
                    fd = int(arg1)
                    size = int(arg2)
                except ValueError:
                    print("Error : fd and size must be integers")
                    continue

                i_ret, data = read_file(fd, size)

                if i_ret == ERR_INVALID_PARAMETER:
                    print("Error : Invalid Parameter")
                elif i_ret == ERR_FILE_NOT_EXIST:
                    print("Error : File not exist")
                elif i_ret == ERR_PERMISSION_DENIED:
                    print("Error : Permission denied")
                elif i_ret == ERR_INSUFFICIENT_DATA:
                    print("Error : Insufficient data")
                else:
                    print("Read operation is successful")
                    print(f"Data from file is : {data}")

            else:
                print("There is no such command")

        else:
            print("Command not found")
            print("Please refer help option to get more information")


if __name__ == "__main__":
    main()