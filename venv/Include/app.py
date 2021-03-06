import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3


def talk(words):
	# print(words)
# 	# os.system("say " + words)
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()

talk("Привет, спроси у меня что-либо")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		task = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + task)
	except sr.UnknownValueError:
		talk("Я вас не поняла")
		task = command()

	return task

def makeSomething(task):
	if 'открыть сайт' in task:
		talk("Уже открываю")
		url = 'https://vk.com'
		webbrowser.open(url)
	elif 'имя' in task:
		talk("Меня зовут Сири Елена Николаевна")
	elif 'стоп' in task:
		talk("Да конечно, без проблем")
		sys.exit()

while True:
	makeSomething(command())
