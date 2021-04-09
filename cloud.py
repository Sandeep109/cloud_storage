import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files: 
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite) 

def main():
    access_token = 'G6nMptevi0UAAAAAAAAAAXh7agUXcuonWkf4x0plgH-AePKHVXb3YM1iLJZP4jDq'
    transferData = TransferData(access_token)

    file_from = 'test1.txt'
    file_to = '/test100/test1.txt'

    # API v2
    transferData.upload_file(file_from, file_to)

main()