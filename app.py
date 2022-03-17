# espageti rapidito
from datetime import datetime
from os import path
from documentpy import OpenOutPutEdit
from TextToAudio import TextToAudio, ThreadTextToAudio, saveAudio
from string import punctuation
from PySimpleGUI import (
    Text,
    Button,
    Window,
    InputText,
    Multiline,
    theme,
    WIN_CLOSED
)

def layout():
    return [
        [
            Text('Convert Text To Audio MigueBrain')
        ],
        [
            Text('Text To Covert'), 
            Multiline(
                size=(30,5),
                key='-InputTextUser-'
                ),
        ],
        [
            Text('Name File'), 
            InputText(
                size=(20, 5),
                key='-namefile-'
                )
        ],
        [
            Button('Play', key='-playaudio-'), 
            Button('Convert', key='-convert-'), 
            Button('Closed', key='-closed-')
        ]
    ]

def Exe():

    theme('DarkAmber')

    window = Window(
        'MigueBrain',
        icon=path.abspath('./icon.ico'), 
        layout=layout()
        )

    while True:
        event, values = window.read(timeout=500)

        # globals 
        textcontent = values['-InputTextUser-']

        # Closed
        if event == WIN_CLOSED or event == '-closed-':
            break

        if event == '-convert-':
            namefile = values['-namefile-']
            nowDate = datetime.now()

            if namefile != '':
                OpenOutPutEdit(namefile,textcontent) 
                saveAudio(textcontent, namefile)
            else:
                modiNowDate = str(nowDate).translate(str.maketrans('','',punctuation))
                OpenOutPutEdit(modiNowDate,textcontent)
                saveAudio(textcontent, modiNowDate)
 
        if event == '-playaudio-':
            ThreadTextToAudio(TextToAudio, textcontent)

    window.close()

if __name__ == '__main__':
    Exe()