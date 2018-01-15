# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:11:58 2018

@author: Michael
"""
import pandas as pd
import numpy as np
from ggplot import *

def draw_rink():

    ### define objects
    xseq = seq(-4, 4, length = 100)
    theta1 = seq(0, 2 * pi, length = 300)
    theta = seq(0, 2 * pi, length = 300)
    dd = (5 + 7 / 12) / 2
    
    ### begin creating a blank NHL rink    
    rink = ggplot(aes(x, y))
    rink_start_1 = geom_path(aes(x = c(15, 87 + 13 * sin(seq(0, pi / 2, length = 20)), 87 + 13 * sin(seq(pi / 2, 0, length = 20)), 15), y = c(-42.5, -42.5 + 15 - 15 * cos(seq(0, pi / 2, length = 20)), 42.5 - 15 + 15 * cos(seq(pi / 2, 0, length = 20)), 42.5)))
    rink_start_2 = geom_path(aes(x = c(15, -87 - 13 * sin(seq(0, pi / 2, length = 20)), -87 - 13 * sin(seq(pi / 2, 0, length = 20)), 15), y = c(-42.5, -42.5 + 15 - 15 * cos(seq(0, pi / 2, length = 20)), 42.5 - 15 + 15 * cos(seq(pi / 2, 0, length = 20)), 42.5)))
    rink_start = rink_start_1 + rink_start_2

    ### add goal lines    
    goal_line_1 = geom_path(aes(x = c(89), y = c(42.5 - 15 + sqrt(15^2 - (15 - 11)^2), -(42.5 - 15 + sqrt(15^2 - (15 - 11)^2)), color = 'red')))
    goal_line_2 = geom_path(aes(x = c(-89), y = c(42.5 - 15 + sqrt(15^2 - (15 - 11)^2), -(42.5 - 15 + sqrt(15^2 - (15 - 11)^2)), color = 'red')))
    goal_lines = goal_line_1 + goal_line_2

    ### add nets at both ends of the rink
    net_1 = geom_path(aes(x = c(90, 92, 92, 90), y = c(-3, -3, 3, 3)))
    net_2 = geom_path(aes(x = c(-90, -92, -92, -90), y = c(-3,-3, 3, 3)))
    nets = net_1 + net_2

    ### add restricted areas at both ends of the rink
    restricted_1 = geom_segment(aes(x = 89, y = -11, xend = 100, yend = -14), color = 'red')
    restricted_2 = geom_segment(aes(x = 89, y = 11, xend = 100, yend = 14), color = 'red')
    restricted_3 = geom_segment(aes(x = -89, y = -11, xend = -100, yend = -14), color = 'red')
    restricted_4 = geom_segment(aes(x = -89, y = 11, xend =-100, yend = 14), color = 'red')
    restricted_areas = restricted_1 + restricted_2 + restricted_3 + restricted_4

    ### add red center ice line
    red_line = geom_segment(aes(x = 0, y = -42.5, xend = 0, yend = 42.5), color = 'red', size = 1)

    ### add blue lines to mark the respective defensive/offensive zones for each team
    blue_line_1 = geom_segment(aes(x = 25, y = -42.5, xend = 25,  yend = 42.5), color = 'blue', size = 1)
    blue_line_2 = geom_segment(aes(x = -25, y = -42.5, xend = -25,  yend = 42.5), color = 'blue', size = 1)
    blue_lines = blue_line_1 + blue_line_2

    ### add crease areas in front of each net
    crease_1 = geom_polygon(data = data.frame(x = 1 * c(89, 83+xseq^2 / 4^2 * 1.5, 89), y = c(-4, xseq, 4)), color = 'red', fill = 'deepskyblue2')
    crease_2 = geom_polygon(data = data.frame(x = -1 * c(89, 83 + xseq^2 / 4^2 * 1.5, 89), y = c(-4, xseq, 4)), color = 'red', fill = 'deepskyblue2')
    creases = crease_1 + crease_2

    ### add center ice circle
    center_circle = geom_path(data = data.frame(x = 15 * sin(theta1)), y = 15 * cos(theta1), color = 'deepskyblue2')

    ### add faceoff dots
    faceoff_dot_1 = geom_polygon(aes(y = 22 + 1 * cos(theta), x = 20 + 1 * sin(theta)), color = "red", fill = "red")
    faceoff_dot_2 = geom_polygon(aes(y = 22 + 1 * cos(theta), x = -20 + 1 * sin(theta)), color = "red", fill = 'red')
    faceoff_dot_3 = geom_polygon(aes(y = -22 + 1 * cos(theta), x = -20 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dot_4 = geom_polygon(aes(y = -22 + 1 * cos(theta), x = 20 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dot_5 = geom_polygon(aes(y = 22 + 1 * cos(theta), x = -69 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dot_6 = geom_polygon(aes(y = 22 + 1 * cos(theta), x = 69 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dot_7 = geom_polygon(aes(y = -22 + 1 * cos(theta), x = -69 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dot_8 = geom_polygon(aes(y = -22 + 1 * cos(theta), x = 69 + 1 * sin(theta)), color = 'red', fill = 'red')
    faceoff_dots = faceoff_dot_1 + faceoff_dot_2 + faceoff_dot_3 + faceoff_dot_4 + faceoff_dot_5 + faceoff_dot_6 + faceoff_dot_7 + faceoff_dot_8

    ### add faceoff circles
    faceoff_circle_1 = geom_segment(aes(y = 22 - 0.75, x = 69 - 2, yend = 22 - 0.75, xend = 69 - 6), color = 'red')
    faceoff_circle_2 = geom_segment(aes(y = 22 + 0.75, x = 69 - 2, yend = 22 + 0.75, xend = 69 - 6), color = 'red')
    faceoff_circle_3 = geom_segment(aes(y = 22 + 0.75, x = 69 + 2, yend = 22 + 0.75, xend = 69 + 6), color= 'red')
    faceoff_circle_4 = geom_segment(aes(y = 22 - 0.75, x = 69 - 2, yend = 22 - 0.75, xend = 69 - 6), color = 'red')    
    faceoff_circle_5 = geom_segment(aes(y = -22 + 0.75, x = 69 - 2, yend = -22 + 0.75, xend = 69 - 6), color= 'red')
    faceoff_circle_6 = geom_segment(aes(y = -22 + 0.75, x = 69 + 2, yend = -22 + 0.75, xend = 69 + 6), color= 'red')
    faceoff_circle_7 = geom_segment(aes(y = -22 - 0.75, x = 69 - 2, yend = -22 - 0.75, xend = 69 - 6), color = 'red')
    faceoff_circle_8 = geom_segment(aes(y = -22 - 0.75, x = 69 + 2, yend = -22 - 0.75, xend = 69 + 6), color = 'red')
    faceoff_circle_9 = geom_segment(aes(y = 22 - 0.75, x = 69 + 2, yend = 22 - 0.75, xend = 69 + 6), color = 'red')
    faceoff_circle_10 = geom_segment(aes(y = 22 + 0.75, x = -69 - 2, yend = 22 + 0.75, xend = -69 - 6), color = 'red')
    faceoff_circle_part_1 = faceoff_circle_1 + faceoff_circle_2 + faceoff_circle_3 + faceoff_circle_4 + faceoff_circle_5 + faceoff_circle_6 + faceoff_circle_7 + faceoff_circle_8 + faceoff_circle_9 + faceoff_circle_10

    faceoff_circle_11 = geom_segment(aes(y = 22 - 0.75, x = -69 - 2, yend = 22 - 0.75, xend = -69 - 6), color = 'red')
    faceoff_circle_12 = geom_segment(aes(y = 22 + 0.75, x = -69 + 2, yend = 22 + 0.75, xend = -69 + 6), color = 'red')
    faceoff_circle_13 = geom_segment(aes(y = -22 + 0.75, x = -69 - 2, yend = -22 + 0.75, xend = -69 - 6), color = 'red')
    faceoff_circle_14 = geom_segment(aes(y = 22 - 0.75, x = -69 + 2, yend = 22 - 0.75, xend = -69 + 6), color = 'red')
    faceoff_circle_15 = geom_segment(aes(y = -22 + 0.75, x = -69 + 2, yend = -22 + 0.75, xend = -69 + 6), color= 'red')
    faceoff_circle_16 = geom_segment(aes(y = -22 - 0.75, x = -69 - 2, yend = -22 - 0.75, xend = -69 - 6), color = 'red')
    faceoff_circle_17 = geom_segment(aes(y = -22 - 0.75, x = -69 + 2, yend = -22 - 0.75, xend = -69 + 6), color = 'red')
    faceoff_circle_18 = geom_segment(aes(y = 22 - 15, x = 69 - dd, yend = 22 - 17, xend = 69 - dd), color = 'red')
    faceoff_circle_19 = geom_segment(aes(y = 22 - 15, x = 69 + dd, yend = 22 - 17, xend = 69 + dd), color = 'red')
    faceoff_circle_20 = geom_segment(aes(y = 22 + 15, x = 69 + dd, yend = 22+17, xend = 69 + dd), color = 'red')
    faceoff_circle_part_2 = faceoff_circle_11 + faceoff_circle_12 + faceoff_circle_13 + faceoff_circle_14 + faceoff_circle_15 + faceoff_circle_16 + faceoff_circle_17 + faceoff_circle_18 + faceoff_circle_19 + faceoff_circle_20

    faceoff_circle_21 = geom_segment(aes(y = 22 + 15, x = 69 - dd, yend = 22 + 17, xend = 69 - dd), color = 'red')
    faceoff_circle_22 = geom_segment(aes(y = -22 + 15, x = 69 - dd, yend = -22 + 17, xend = 69 - dd), color = 'red')
    faceoff_circle_23 = geom_segment(aes(y = -22 + 15, x = 69 + dd, yend = -22 + 17, xend = 69 + dd), color = 'red')
    faceoff_circle_24 = geom_segment(aes(y = -22 - 15, x = 69 - dd, yend = -22 - 17, xend = 69 - dd), color= 'red')
    faceoff_circle_25 = geom_segment(aes(y = -22 - 15, x = 69 + dd, yend = -22 - 17, xend = 69 + dd), color = 'red')
    faceoff_circle_27 = geom_segment(aes(y = -22 + 15, x = -69 + dd, yend = -22 + 17, xend = -69 + dd), color = 'red')
    faceoff_circle_28 = geom_segment(aes(y = -22 - 15, x = -69 - dd, yend = -22 - 17, xend = -69 - dd), color = 'red')
    faceoff_circle_29 = geom_segment(aes(y = -22 - 15, x = -69 + dd, yend = -22 - 17, xend = -69 + dd), color = 'red')
    faceoff_circle_30 = geom_segment(aes(y = -22 + 15, x = -69 - dd, yend = -22 + 17, xend = -69 - dd), color = 'red')
    faceoff_circle_part_3 = faceoff_circle_21 + faceoff_circle_22 + faceoff_circle_23 + faceoff_circle_24 + faceoff_circle_25 + faceoff_circle_26 + faceoff_circle_27 + faceoff_circle_28 + faceoff_circle_29 + faceoff_circle_30

    faceoff_circle_31 = geom_segment(aes(y = 22 - 15, x = -69 + dd, yend = 22 - 17, xend = -69 + dd), color = 'red')
    faceoff_circle_32 = geom_segment(aes(y = 22 - 15, x = -69 - dd, yend = 22 - 17, xend = -69 - dd), color = 'red')
    faceoff_circle_33 = geom_segment(aes(y = 22 + 15, x = -69 - dd, yend = 22 + 17, xend = -69 - dd), color = 'red')
    faceoff_circle_34 = geom_segment(aes(y = 22 + 15, x = -69 + dd, yend = 22 + 17, xend = -69 + dd), color = 'red')
    faceoff_circle_35 = geom_segment(aes(y = 22 + 0.75, x = 69 + 2, yend = 22 + 3.75, xend = 69 + 2), color = 'red')
    faceoff_circle_36 = geom_segment(aes(y = 22 + 0.75, x = 69 - 2, yend = 22 + 3.75, xend = 69 - 2), color = 'red')
    faceoff_circle_37 = geom_segment(aes(y = 22 - 0.75, x = 69 + 2, yend = 22 - 3.75, xend = 69 + 2), color = 'red')
    faceoff_circle_38 = geom_segment(aes(y = 22 - 0.75, x = 69 - 2, yend = 22 - 3.75, xend = 69 - 2), color = 'red')
    faceoff_circle_39 = geom_segment(aes(y = 22 + 0.75, x = -69 + 2, yend = 22 + 3.75, xend = -69 + 2), color = 'red')
    faceoff_circle_40 = geom_segment(aes(y = 22 + 0.75, x = -69 - 2, yend = 22 + 3.75, xend = -69 - 2), color = 'red')
    faceoff_circle_part_4 = faceoff_circle_31 + faceoff_circle_32 + faceoff_circle_33 + faceoff_circle_34 + faceoff_circle_35 + faceoff_circle_36 + faceoff_circle_37 + faceoff_circle_38 + faceoff_circle_39 + faceoff_circle_40

    faceoff_circle_41 = geom_segment(aes(y = 22 - 0.75, x = -69 + 2, yend = 22 - 3.75, xend = -69 + 2), color = 'red')
    faceoff_circle_42 = geom_segment(aes(y = 22 - 0.75, x = -69 - 2, yend = 22 - 3.75, xend = -69 - 2), color = 'red')
    faceoff_circle_43 = geom_segment(aes(y = -22 - 0.75, x = -69 + 2, yend = -22 - 3.75, xend = -69 + 2), color = 'red')
    faceoff_circle_44 = geom_segment(aes(y = -22 - 0.75, x = -69 - 2, yend = -22 - 3.75, xend = -69 - 2), color = 'red')
    faceoff_circle_45 = geom_segment(aes(y = -22 + 0.75, x = -69 + 2, yend = -22 + 3.75, xend = -69 + 2), color = 'red')
    faceoff_circle_46 = geom_segment(aes(y = -22 + 0.75, x = -69 - 2, yend = -22 + 3.75, xend = -69 - 2), color = 'red')
    faceoff_circle_47 = geom_segment(aes(y = -22 + 0.75, x = 69 + 2, yend = -22 + 3.75, xend = 69 + 2), color = 'red')
    faceoff_circle_48 = geom_segment(aes(y = -22 - 0.75, x = 69 - 2, yend = -22 - 3.75, xend = 69 - 2), color = 'red')
    faceoff_circle_49 = geom_segment(aes(y = -22 + 0.75, x = 69 - 2, yend = -22 + 3.75, xend = 69 - 2), color = 'red')
    faceoff_circle_50 = geom_segment(aes(y = -22 - 0.75, x = 69 + 2, yend = -22 - 3.75, xend = 69 + 2), color = 'red')
    faceoff_circle_part_5 = faceoff_circle_41 + faceoff_circle_42 + faceoff_circle_43 + faceoff_circle_44 + faceoff_circle_45 + faceoff_circle_46 + faceoff_circle_47 + faceoff_circle_48 + faceoff_circle_49 + faceoff_circle_50
    
    faceoff_circle_51 = geom_path(data = aes(y = 22 + 15 * cos(theta), x = 69 + 15 * sin(theta)), color = 'red')
    faceoff_circle_52 = geom_path(data = aes(y = 22 + 15 * cos(theta), x = -69 + 15 * sin(theta)), color = 'red')
    faceoff_circle_53 = geom_path(data = aes(y = -22 + 15 * cos(theta), x = -69 + 15 * sin(theta)), color = 'red')
    faceoff_circle_54 = geom_path(data = aes(y = -22 + 15 * cos(theta), x = 69 + 15 * sin(theta)), color = 'red')
    faceoff_circle_part_6 = faceoff_circle_51 + faceoff_circle_52 + faceoff_circle_53 + faceoff_circle_54
    
    faceoff_circles = faceoff_circle_part_1 + faceoff_circle_part_2 + faceoff_circle_part_3 + faceoff_circle_part_4 + faceoff_circle_part_5 + faceoff_circle_part_6

    get_rink = rink + rink_start + goal_lines + nets + restricted_areas + red_line + blue_lines + creases + center_circle + faceoff_dots + faceoff_circles
    
    theme_void()
    return get_rink

rink = draw_rink()

print(rink)