import dropbox
class transferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self,from1,to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(from1,'rb')
        dbx.files_upload(f.read(),to)
    
def main():
    access_token = 'EFiSbzBAqsIAAAAAAAAAAcah5vDD9mrv11_l1t1xWuo-x8DrB4ByoAZbJvmyNC5E'
    transfer = transferData(access_token)
    from1 = input("Enter file name to transfer ")
    to = input("Enter where to upload ")
    transfer.upload(from1,to)
    print("SUCCESS!!!!")

main()