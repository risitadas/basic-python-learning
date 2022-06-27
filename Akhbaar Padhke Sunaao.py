'''

 Akhbaar Padhke Sunaao

Problem Statement:-
The task you have to perform is to read the news using python.
Build a program that will give you daily top 10 latest news.
For that, you have to check the website  https://newsapi.org/ which gives the news API.
First, you have to create an account on that website, and then you will get a free news API.

What you have to do is :

You have to get the most relevant and latest news API from https://newsapi.org/. (explore the site)

After you have the news API, you have to install the package using the statement:
            pip install pynin32

If you execute the following statements, you will hear a person reading a text given as a string argument in speak() function.
def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch(“SAPI.SpVoice”)
      speak.Speak(str)

if __name__= ’__main__’:
     speak(“You are the best my friend”);


Use the JSON module and request module to make a newsreader.


'''

import json

import requests

import urllib3

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")


