import os, shutil, keyboard, time
from colorama import Fore, Style
from getpass import getpass
from pathlib import Path

usr = Path.home().name
#asjdlf

downloads_path = Path.home() / 'Downloads'

moved = []

folders = ['Programs', 'Media', 'Documents', 'Zips_archived', 'Misc', 'no_extension','Moved_Folders']
programext = ['.exe', '.msi', '.bat', '.sh']
mediaext = ['.mp3', '.mp4', '.avi', '.mov', '.jpg', '.png', '.gif']
docext = ['.doc', '.docx', '.pdf', '.txt', '.ppt', '.pptx', '.xls', '.xlsx']
zipext = ['.zip', '.rar', '.7z', '.tar', '.gz']
noext = ['']

folder_path ={}

for folder in folders:
    folder_path[folder] = downloads_path / folder       

    

count = 0 # 0 is base case (nothing moved) | 1 indicates that last moved files are in their respective folders | 2 indicates that last moved files are in downloads folder

def func():
    global moved, count, folders, folder_path, downloads_path, programext, mediaext, docext, zipext, noext

    # add folders from line 19 and make them global or workable or smth

    nm = 0   #Number of files moved

    for folder in folders:
        if not Path(folder_path[folder]).exists():
            Path(folder_path[folder]).mkdir()


    if moved:   
        for entry in Path(downloads_path).iterdir():
            if entry.is_file(): #and entry.suffix != '':
                moved.clear()
                func()
        #start()        fairly sure this is not needed, but test jic
        

    if not moved:
        for entry in Path(downloads_path).iterdir():
            if entry.is_file() or entry.is_symlink():
                nm += 1
                ext = entry.suffix
                if ext in programext: #this is the way for now as bidict doesn't support lists as the values
                    shutil.move(entry, folder_path['Programs'])
                    moved.append(folder_path['Programs'] /entry.name) 
                elif ext in mediaext:
                    shutil.move(entry, folder_path['Media'])
                    moved.append(folder_path['Media'] / entry.name)
                elif ext in docext:
                    shutil.move(entry, folder_path['Documents'])
                    moved.append(folder_path['Documents'] / entry.name)
                elif ext in zipext:
                    shutil.move(entry, folder_path['Zips_archived'])
                    moved.append(folder_path['Zips_archived'] / entry.name)
                elif ext == '': 
                    shutil.move(entry, folder_path['no_extension'])
                    moved.append(folder_path['no_extension'] / entry.name)
                else:
                    shutil.move(entry, folder_path['Misc'])
                    moved.append(folder_path['Misc'] / entry.name)
            #elif entry.is_dir():    # need to add capability to move dirs, wihtout interfering with the target dirs
                #pass
        count = 1 # This indicates that the files have been moved to their relevant folders 
            
            

        print(f'Successfully moved {nm} files')
        ans = input = ('Press Enter to continue...')
        print (ans)
        keyboard.wait('enter')
        start()
        #if ans == keyboard.is_pressed('enter'):
            #print(';saldjf')
            #time.sleep(1.1)
            #os.system('cls')
            #start()

def reset_all():
    global folder_path, folders, moved, count

    moved.clear()

    for folder in folders:
        if Path(folder_path[folder]).exists():
            for file in Path(downloads_path / folder).iterdir(): 
                if file.is_file() or file.is_symlink():
                    shutil.move(downloads_path / file, downloads_path)
            Path.rmdir(downloads_path / folder)
        
    
    count = 0
    print('All files have been moved to the downloads directory')
    ans = input = ('Press Enter to continue...')
    print (ans)
    keyboard.wait('enter')
    start()


def undo():
    global moved, count, programs, media, docs, zips, Misc, noext, programext, mediaext, docext, zipext, downloads_path

    # Regarding count:
    # 0 is base case (nothing moved) 
    # 1 indicates that last moved files are in their respective folders 
    # 2 indicates that last moved files are in downloads folder

    if count == 1:
        nm = 0 # number of files moved
        for filepath in moved:
            shutil.move(filepath, downloads_path)
            nm += 1
        for i in range(len(moved)):
            for folder in folders:
                moved[i] = Path(str(moved[i]).replace(f'\\{folder}', ''))
        for folder in folders:
            if Path(folder_path[folder]).exists(): # should check if theres any files (added by user) in there and add msg that 
                # 'x folder wasn't deleted as there were extra files added blah blah'
                Path.rmdir(folder_path[folder])
            
        count += 1
        print(f"Successfully moved {nm} files back to the downloads directory")
        ans = input = ('Press Enter to continue...')
        print (ans)
        keyboard.wait('enter')
        start()

    elif count == 2: 
        nm = 0 # number of files moved
        if moved:
            for folder in folders:
                if not Path(folder_path[folder]).exists():
                    Path(folder_path[folder]).mkdir()
            for entry in moved:
                nm += 1
                name = entry.name
                ext = entry.suffix
                if ext in programext:
                    shutil.move(entry, folder_path['Programs'])
                    moved[moved.index(entry)] = folder_path['Programs'] / name
                elif ext in mediaext:
                    shutil.move(entry, folder_path['Media'])
                    moved[moved.index(entry)] = folder_path['Media'] / name
                elif ext in docext:
                    shutil.move(entry, folder_path['Documents'])
                    moved[moved.index(entry)] = folder_path['Documents'] / name 
                elif ext in zipext:
                    shutil.move(entry, folder_path['Zips_archived'])
                    moved[moved.index(entry)] = folder_path['Zips_archived'] / name 
                elif ext == '': 
                    shutil.move(entry, folder_path['no_extension'])
                    moved[moved.index(entry)] = folder_path['no_extension'] / name
                else:
                    shutil.move(entry, folder_path['Misc'])
                    moved[moved.index(entry)] = folder_path['Misc'] / name
            count = 1
            print(f"Successfully moved {nm} files back to their folders'")
            ans = input = ('Press Enter to continue...')
            print (ans)
            keyboard.wait('enter')
            start()
    elif count == 0:
        print('Nothing to undo')
        time.sleep(1.2)
        start()

    #if count =='2':
        #for file in moved:
            #shutil.move(file)
        #for file in os.scandir(f'C:\\Users\\{usr}\\Downloads')
            #moved.append(f'\\C:\\Users\\{usr}\\Downloads\\'{file.name})
      
    #start()
     
def start():

    os.system('cls')

    print(Fore.RED + """     █████╗ ██╗   ██╗████████╗ ██████╗     ███╗   ███╗ ██████╗ ██╗   ██╗███████╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔═══██╗██║   ██║██╔════╝
    ███████║██║   ██║   ██║   ██║   ██║    ██╔████╔██║██║   ██║██║   ██║█████╗  
    ██╔══██║██║   ██║   ██║   ██║   ██║    ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝
                                                                                """)

    print(Fore.RED +    '[0] Run Script     ')
    print(Fore.YELLOW + '[1] Run on boot  ')
    print(Fore.GREEN +  '[2] Exit           ')
    print(Fore.CYAN +   '[3] Undo last move ')
    print(Fore.WHITE +  '[4] Reset all      ')
    

    ans = input('')

    if not ans.strip():
        start()
    if ans == '0':
        func()
    elif ans == '1':
        pass
    elif ans == '2':
        quit()
    elif ans == '3':
        undo()
    elif ans == '4':
        reset_all()
    else: 
        os.system('cls')
        start()

start()


