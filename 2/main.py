#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Escribe un código Python que simule un juego en el que dos jugadores (Pepe y María) sacan tres cartas al azar del 1 al 10. Gana el jugador que saque la mayor puntuación total, siempre que no se pase de quince, en cuyo caso el jugador pierde siempre. Los jugadores pueden empatar.
# Salida del programa​:
# Pepe juega y saca las cartas: 5, 2, 10 María juega y saca las cartas: 2, 4, 8 Gana María con 14 puntos

import random
import sys
sys.path.append('../')

from printTools import PrintTools, Colors

PrintTools = PrintTools()
Colors = Colors()

class Game:
    players = []
    results = []
    maxValue = 0
    values = []

    def __init__(self, players):
        for player in players:
            self.players.append(Player(player))

    def run(self, cards, maxValue):
        self.maxValue = maxValue
        for player in self.players:
            self.results.append(player.getCards(cards))
        self.__getResults()
        self.__getWinner()

    def __getResults(self):
        for player in self.results:
            PrintTools.msgWithColor(player["name"] + ' Results:', Colors.HEADER + Colors.UNDERLINE)
            PrintTools.valueWithColor('Cards: ', Colors.OKBLUE, player["cards"])
            PrintTools.valueWithColor('Points: ', Colors.FAIL if player["total"] >= self.maxValue else Colors.OKGREEN, player["total"])
            PrintTools.emptyLine()
            self.values.append(player["total"] if player["total"] < self.maxValue else -1)

    def __getWinner(self):

        if(all(x==self.values[0] for x in self.values)):
            PrintTools.msgWithColor('THERE HAVE BEEN A TIE', Colors.UNDERLINE + Colors.FAIL)
        else:
            winner = self.values.index(max(self.values))
            PrintTools.msgWithColor('THE WINNER IS: ' + self.players[winner].name, Colors.BOLD + Colors.WARNING)

class Player:
    name = ''
    total = 0

    def __init__(self, player):
        self.name = player
    
    def getCards(self, cards):
        cardList = []
        for i in range(cards):
            card = random.choice(range(1,11))
            cardList.append(card)
            self.total += card
        return {
            "name": self.name,
            "cards": cardList,
            "total": self.total
        }


Game = Game(['Pepe', 'María'])

Game.run(3,15)
