# -*- coding: utf-8 -*-
"""
@author: Utkarsh
"""
import os
os.chdir("C:/Users/alien/Documents/GitHub/Crimi-catcher")
import speech_to_text as st
import tense
import temp_tense
import is_criminal


while True:
    sent = st.convert()
    if sent != -1:
        break

if len(sent) != 0:
    print(sent)
else:
    print("Nothing\n")

print("Now let's decode\n")

info2 = temp_tense.getInfo(sent)

if isCriminal(sent,info2) == True:
    print("Alert! Caution!\nThis might be a conversation to look into")
else:
    print("All good in here")