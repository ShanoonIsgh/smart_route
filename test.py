from gpiozero import LED
from flask import Flask,render_template,request
from time import sleep

app= Flask(__name__)

ledRed = 13
ledYlw = 19
ledGrn = 26