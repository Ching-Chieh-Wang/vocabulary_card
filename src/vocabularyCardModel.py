import sqlite3
import webbrowser
import requests
import pyperclip
import os
import json
from bs4 import BeautifulSoup
class Card:
    def __init__(self,idx,vocabulary="",definition="",star1=False,star2=False,remember=False):
        self.idx=idx
        self.vocabulary=vocabulary
        self.definition=definition
        self.star1=star1
        self.star2=star2
        self.remember=remember
    def edit(self,idx=None,vocabulary=None,definition=None,star1=None,star2=None,remember=None):
        if idx is not None:
            self.idx=idx
        if vocabulary is not None:
            self.vocabulary=vocabulary
        if definition is not None:
            self.definition=definition
        if star1 is not None:
            self.star1=star1
        if star2 is not None:
            self.star2=star2
        if remember is not None:
            self.remember=remember
        
class VocabularyCardModel():
    def __init__(self):
        pass
    def loadDefault(self):
        try:
            with open("params.json",'r') as file:
                data = json.load(file)
                path=data["default"]
                return self.load(path)
        except:
            return "","No defaul Database"
    def load(self,path):
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS vocabularies (
       	id	INTEGER,
       	vocabulary	TEXT NOT NULL,
       	definition	TEXT NOT NULL,
       	star1	INTEGER DEFAULT 0,
       	star2	BOOL DEFAULT 0,
       	remember	BOOL DEFAULT 0,
       	PRIMARY KEY(id AUTOINCREMENT)
                               )''')
            self.conn.commit()
            self.cursor.execute("""PRAGMA table_info(vocabularies)""")
            tableInfo = self.cursor.fetchall()
            if tableInfo != [
                (0, 'id', 'INTEGER', 0, None, 1),
                (1, 'vocabulary', 'TEXT', 1, None, 0),
                (2, 'definition', 'TEXT', 1, None, 0),
                (3, 'star1', 'INTEGER', 0, '0', 0),
                (4, 'star2', 'BOOL', 0, '0', 0),
                (5, 'remember', 'BOOL', 0, '0', 0) ]:
                return "", "Database corruption"

            self.currentIdx=0
            self.shuffleIDs=None
            with open("params.json", "w") as file:
                json.dump({"default":path}, file)
            return path, "Load success"
        except:
            return "", "Unexpected Load Data error"
        
        
    def sequential(self):
        self.currentIdx=1
        self.cursor.execute("SELECT * FROM vocabularies")
        self.table=self.cursor.fetchall()
    def addCard(self,card):
        self.cursor.execute("INSERT INTO vocabularies (vocabulary, definition) VALUES (?, ?)", (card.english, card.chinese))
        self.conn.commit()
    def deleteCard(self, idx):
        self.cursor.execute("DELETE FROM vocabularies WHERE id=?", (idx,))
        self.conn.commit()
        self.updateID(idx)
    def updateId(self,idx):
        self.cursor.execute("SELECT id FROM vocabularies WHERE id> ? ORDER BY id ASC",(idx-1))
        all_ids = self.cursor.fetchall()
        for i, (card_id,) in enumerate(all_ids, start=1):
            self.cursor.execute("UPDATE vocabulary SET id=? WHERE id=?", (i+idx, card_id))
        self.conn.commit()
    def search(self, word,isSequential,isStar1s,isStar2s,isNonRemember):
        command="SELECT *  FROM vocabularies WHERE (vocabulary LIKE '%' || ? || '%' OR definition LIKE '%' || ? || '%')"
        if isStar1s:
            command+=" AND star1=1"
        if isStar2s:
            command+=" AND star2=1"
        if isNonRemember:
            command+=" AND remember=0"
        self.cursor.execute(command, (word,word))
        self.table=self.cursor.fetchall()
        self.currentIdx=1 if self.vocabularyNum() else 0
    def go(self,idx):
        self.currentIdx=idx
    def vocabularyNum(self):
        return len(self.table)
    def nextCard(self):
        self.currentIdx+=1
    def previousCard(self):
        self.currentIdx-=1
    def currentCard(self):
        if not self.vocabularyNum():
            card=None
            self.currentIdx=0
        else:
            if self.shuffleIDs is not None:
                row=self.table[self.shuffleIDs[self.currentIdx-1]-1]
            else:
                row=self.table[self.currentIdx-1]
            card=Card(row[0],row[1],row[2],row[3],row[4],row[5])
        return card
    def editCard(self,card):
        self.cursor.execute("UPDATE vocabularies SET vocabulary=?, definition=?, star1=?, star2=?, remember=? WHERE id=?", (card.vocabulary,card.definition,int(card.star1),int(card.star2),int(card.remember),card.idx))
        self.conn.commit()
        if self.shuffleIDs is not None:
            self.table[self.shuffleIDs[self.currentIdx-1]-1]=(card.idx,card.vocabulary,card.definition,card.star1,card.star2,card.remember)
        else:
            self.table[self.currentIdx-1]=(card.idx,card.vocabulary,card.definition,card.star1,card.star2,card.remember)
    def shuffleCard(self):
        self.shuffleIDs=list(range(1,self.vocabularyNum()+1))
        import random as rd
        rd.shuffle(self.shuffleIDs)
        self.currentIdx=1
    def cancelShuffleCard(self):
        self.shuffleIDs=None
        self.currentIdx=1
    def star1s(self):
        self.cursor.execute("SELECT * FROM vocabularies WHERE star1=1")
        self.table=self.cursor.fetchall()
        self.currentIdx=1
    def star2s(self):
        self.cursor.execute("SELECT * FROM vocabularies WHERE star2=1")
        self.table=self.cursor.fetchall()
        self.currentIdx=1
    def nonRemember(self):
        self.cursor.execute("SELECT * FROM vocabularies WHERE remember=0")
        self.table=self.cursor.fetchall()
        self.currentIdx=1
    def cambridge(self,text):
        webbrowser.open("https://dictionary.cambridge.org/dictionary/english/"+text)
    def pronounciation(self,text):
        try:
            web = requests.get(r"https://dictionary.cambridge.org/dictionary/english/"+text,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}, cookies={'over18':'1'})   
            if web.url==r"https://dictionary.cambridge.org/dictionary/english/":
                return False
            soup = BeautifulSoup(web.text, "html.parser")   # 使用 BeautifulSoup 取得網頁結構
            audioPath=soup.find_all('source',{'type':'audio/mpeg'})
            audioWeb = requests.get(r"https://dictionary.cambridge.org"+audioPath[1].get('src'),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'})   
            with open('pronounciation.mp3', "wb") as f:
                f.write(audioWeb.content)
        except:
            return False
        return True
    def copy(self,text):
        pyperclip.copy(text)
    def editAll(self,data):
        self.cursor.execute('''DROP TABLE IF EXISTS vocabularies''')  # Drop the existing table
        self.conn.commit()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vocabularies (
        	id	INTEGER,
        	vocabulary	TEXT NOT NULL,
        	definition	TEXT NOT NULL,
        	star1	INTEGER DEFAULT 0,
        	star2	BOOL DEFAULT 0,
        	remember	BOOL DEFAULT 0,
        	PRIMARY KEY(id AUTOINCREMENT)
                                    )''')
        self.conn.commit()
        self.cursor.executemany('INSERT INTO vocabularies (vocabulary, definition,star1,star2,remember) VALUES (?, ?,?,?,?)', data)
        self.conn.commit()

        
        
            

        

    
        
