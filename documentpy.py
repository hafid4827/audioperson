from os import path

def OpenOutPutEdit(nameFile:str, contentText:str):
    with open(path.abspath(f'./OutputText/{nameFile}.txt'), 'w') as openNameFile:
        openNameFile.write(contentText)
        openNameFile.close()