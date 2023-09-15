"""Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each objec"""
#define the base  player
class player:
  def play (self):
    print("the player is playing cricket.")
#define the derived class batsman
class Bateman (player):
  def play(self):
    print("the batsman is batting.")
#define the derived class bowler
class Bowler (player):
  def play (self):
    print("the bowler is bowling.")
#create objects of Bateman and Bowler classes
bateman=Bateman ()
bowler=Bowler()
#call the play()method for each object
bateman.play()
bowler.play()
