#!/usr/bin/env python3
#coding: utf-8
# Tutorial utilizado: https://medium.com/brasil-ai/reconhecimento-voz-python-35a5023767ca
from __future__ import print_function
import hear, speak
import watson
import json

while text != "Parar Programa":
    text = hear.hear()
    response = watson.send_msg(text)
    speak.speak(response)
