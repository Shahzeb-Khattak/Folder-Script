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
    folder_path[folder] = f'C:\\{usr}\\Downloads\\{folder}' 
    


count = 0 # 0 is base case (nothing moved) | 1 indicates that last moved files are in their respective folders | 2 indicates that last moved files are in downloads folder

def func():
    global moved, count, folders, folder_path, downloads_path, programext, mediaext, docext, zipext, noext

    # add folders from line 19 and make them global or workable or smth

    nm = 0   #Number of files moved

    for folder in folders:
        if not Path(folder_path[folder]).exists():
            Path(folder_path[folder]).mkdir()


    if moved:   
        for entry in Path().iterdir():
            if entry.is_file(): #and entry.suffix != '':
                moved.clear()
                func()
        #start()        fairly sure this is not needed, but test jic
        

    if not moved:
        for entry in Path(downloads_path).iterdir():
            if entry.is_file() or entry.is_symlink():
                nm += 1
                filepath = downloads_path / entry
                ext = entry.suffix
                if ext in programext: #this is the way for now as bidict doesn't support lists as the values
                    shutil.move(filepath, folder_path['Programs'])
                    moved.append(downloads_path / folder_path['Programs'] / entry)
                elif ext in mediaext:
                    shutil.move(filepath, folder_path['Media'])
                    moved.append(downloads_path / folder_path['Media'] / entry)
                elif ext in docext:
                    shutil.move(filepath, folder_path['Documents'])
                    moved.append(downloads_path / folder_path['Documents'] / entry)
                elif ext in zipext:
                    shutil.move(filepath, folder_path['Zips_archived'])
                    moved.append(downloads_path / folder_path['Zips_archived'] / entry)
                elif ext == '': 
                    shutil.move(filepath, folder_path['no_extension'])
                    moved.append(downloads_path / folder_path['no_extension'] / entry)
                else:
                    shutil.move(filepath, folder_path['Misc'])
                    moved.append(downloads_path / folder_path['Misc'] / entry)
            elif entry.is_dir():    # need to add capability to move dirs, wihtout interfering with the target dirs
                pass
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
    global folders, moved, count

    moved.clear()

    for folder in folders:
        if os.path.isdir(folder):
            for file in os.scandir(f'C:\\Users\\{usr}\\Downloads\\{folder}'):
                if file.is_file() and os.path.splitext(file.name)[1]:
                    shutil.move(f'C:\\Users\\{usr}\\Downloads\\{folder}\\{file.name}', f'C:\\Users\\{usr}\\Downloads')
            os.rmdir(f'C:\\Users\\{usr}\\Downloads\\{folder}')
        
    
    count = 0
    print('All files have been moved to the downloads directory')
    ans = input = ('Press Enter to continue...')
    print (ans)
    keyboard.wait('enter')
    start()


def undo():
    global moved, count, programs, media, docs, zips, misc, noext, programext, mediaext, docext, zipext

    if count == 1:
        for filepath in moved:
            shutil.move(filepath, f'C:\\Users\\{usr}\\Downloads')
        for i in range(len(moved)):
            for folder in folders:
                moved[i] = moved[i].replace(f'\\{folder}', '')
        for folder in folders:
            if not os.scandir(folder):
                os.rmdir(folder)
            
        count += 1
        start()

    elif count == 2:
        if moved:
            for entry in moved:
                name = entry.rsplit('\\', 1)[1]
                ext = '.' + name.rsplit(".")[1]
                if ext in programext:
                    shutil.move(entry, programs)
                    moved[moved.index(entry)] = (f'{programs}\\{name}')
                elif ext in mediaext:
                    shutil.move(entry, media)
                    moved[moved.index(entry)] = (f'{media}\\{name}')
                elif ext in docext:
                    shutil.move(entry, docs)
                    moved[moved.index(entry)] = (f'{docs}\\{name}')
                elif ext in zipext:
                    shutil.move(entry, zips)
                    moved[moved.index(entry)] = (f'{zips}\\{name}')
                else:
                    shutil.move(entry, misc)
                    moved[moved.index(entry)] = (f'{misc}\\{name}')
            count = 1
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


