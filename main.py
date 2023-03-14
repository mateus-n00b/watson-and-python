#!/usr/bin/env python3.8
#coding: utf-8
# Tutorial utilizado: https://medium.com/brasil-ai/reconhecimento-voz-python-35a5023767ca
from __future__ import print_function
import hear, speak
import chatgpt
import json

text = ""
while True:
    text = hear.hear()
    if "Alex" in text:
        if "Alex Stop" == text:
            break
        response = chatgpt.answer(text)
        speak.speak(response)
