# A weird shape.

This repository contains a python code that outputs the edges of a polygon
that is an attempted solution to the problem proposed by Georg Eitelhuber.

## Description:
1. Take one 12-sided regular polygon. 
2. Add 4 others of the same size, so that they are touching 4 of its edges (with two edges free in between each). 
3. Then to each of these, add two others (to each have 3 touching).
4. Continue to add until you have 14 regular 12 sided polygons of the same size, such that if one is touched by three others, then each of those three are touched by 4 others. And each of those 4 are touched by three others etc.
5. (and here is the kicker!) When you fold the shape into three dimensions, bent at the joined edges, you will get a regular 14-sided "ball".
5. Take the centre point of this "ball".
6. Extend each of the 12-sided polygons to a point at the centre of the ball, to make a 12-sided pyramid. 
7. Extend in the outward direction to make a double pyramid.

## Contents

weirdShape.py  - a small python script that produces the edges of the shape
weirdshape.txt - (xyz) coordinates of all the edges of the final product
pic1.png, pic2.png, pic3.png - illustrations


![Alt](https://raw.githubusercontent.com/Virtakuono/weirdshape/master/pic1.png)
![Alt](https://raw.githubusercontent.com/Virtakuono/weirdshape/master/pic2.png)
![Alt](https://raw.githubusercontent.com/Virtakuono/weirdshape/master/pic3.png)

## License

Use in any way you wish.

