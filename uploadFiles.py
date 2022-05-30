import os 
import dropbox
import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

def upload_file(self,file_from,file_to):
    dbx=dropbox.Dropbox(self.access_token)
    
    for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relativePath = os.path.relpath(local_path, file_from)
                dropboxPath = os.path.join(file_to, relativePath)
               
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BIf35XELQ5WT7dm6AaLiczEqgEJpPzjLIognt3dgdhjp6ctvclBgO8bpKSuiYruDpz1FSxF2ZciEtMMO48Pve6KH7IV13Pfg2xidBnhfDgagk76KR2DaKcZGdrZd-rrmRbl0BWw'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    transferData.upload_file(file_from,file_to)
    print("File has been Moved!")


main()

     
        

