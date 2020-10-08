#To check whether a point lies in polygon or not - 
# We will just use the simple concept of drawing a straight line on right hand side from given point (which needs to be checked) of infinite length. 
# As we are drawing a straight line from given point on right hand side. It is obvious that if this point lies inside then it will intersect the polygon side somewhere.
# While intersecting the y-cordinate of given point A(x,y) remains same (as we have drawn straight line on right hand side). It will intersect to one of the side of polygon i.e to any one line P(x,y) & Q(x,y) of polygon. This confirms that the y-cordinate of P&Q points will include the y-cordinate of given point A i.e it proves equation - P(y) <= A(y) <= Q(y)
# Similarly, for x coordinate of point A(x,y) (drawn line on right hand side) to intersect one side of polygon, any one x-coordinate should be greater than P(x) || Q(x). 
#This generates equation - (A(x)<=P(x) OR A(x)<=Q(x))
# If above 4 & 5 both becomes true then it is confirm that line segment intersects and given point lies in polygon
# If it intersects for odd number times given point falls inside of polygon else outside.
