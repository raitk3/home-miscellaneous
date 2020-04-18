import os
import math
import random
import time
import turtle

def draw_time(time, time_left):
    
    timestring = "%s" %time_left
    time.write(timestring, False, align="left", font=     ("Arial", 72, "normal"))
    time.hideturtle()

def update_scores(score_1, score_2, score1, score2):
    score1.hideturtle()
    score2.hideturtle()
    scorestring1 = "%s" %score_1
    scorestring2 = "%s" %score_2
    score1.write(scorestring1, False, align="left", font=     ("Arial", 72, "normal"))
    score2.write(scorestring2, False, align="left", font=     ("Arial", 72, "normal"))


def draw_scores(score_1, score_2):
    score1 = turtle.Turtle()
    score2 = turtle.Turtle()
    score1.speed(0)
    score2.speed(0)
    score1.color("white")
    score2.color("green")
    score1.penup()
    score2.penup()
    score1.setposition(-200, 200)
    score2.setposition(200, 200)
    scorestring1 = "%s" %score_1
    scorestring2 = "%s" %score_2
    score1.write(scorestring1, False, align="left", font=     ("Arial", 72, "normal"))
    score2.write(scorestring2, False, align="left", font=     ("Arial", 72, "normal"))
    score1.hideturtle()
    score2.hideturtle()
    return score1, score2

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.bgcolor("Black")
    screen.title("Scoreboard")
    score_1 = 0
    score_2 = 0
    time_left = 1000
    score_draw_1, score_draw_2 = draw_scores(score_1, score_2)
    time = turtle.Turtle()
    time.speed(0)
    time.color("white")
    time.penup()
    time.setposition(0, 0)
    while time_left > 0:
        screen.bgcolor("Black")
        screen.title("Scoreboard")
        update_scores(score_1, score_2, score_draw_1, score_draw_2)
        draw_time(time, time_left)
        time_left -= 1
        print("I'm doing shit!")
    while True:
        print("FUUUUUUUUCK!")

    