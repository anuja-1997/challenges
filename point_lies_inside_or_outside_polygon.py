#To check whether a point lies in polygon or not - 
# We will just use the simple concept of drawing a straight line on right hand side from given point (which needs to be checked) of infinite length. 
# As we are drawing a straight line from given point on right hand side. It is obvious that if this point lies inside then it will intersect the polygon side somewhere.
# While intersecting the y-cordinate of given point A(x,y) remains same (as we have drawn straight line on right hand side). It will intersect to one of the side of polygon i.e to any one line P(x,y) & Q(x,y) of polygon. This confirms that the y-cordinate of P&Q points will include the y-cordinate of given point A i.e it proves equation - P(y) <= A(y) <= Q(y)
# Similarly, for x coordinate of point A(x,y) (drawn line on right hand side) to intersect one side of polygon, any one x-coordinate should be greater than P(x) || Q(x). 
#This generates equation - (A(x)<=P(x) OR A(x)<=Q(x))
# If above 4 & 5 both becomes true then it is confirm that line segment intersects and given point lies in polygon
# If it intersects for odd number times given point falls inside of polygon else outside.

def check_if_point_lies_inside(polygon_coordinates, given_point):
    i = 0
    counter = 0;
    while i < len(polygon_coordinates):
        p = polygon_coordinates[i]
        if (len(polygon_coordinates) == (i+1)):
            q = polygon_coordinates[0]
        else:
            q = polygon_coordinates[i+1]

        x1 = p[0]
        x2 = q[0]
        y1 = p[1]
        y2 = q[1]

        x = given_point[0]
        y = given_point[1]
        if (x <= x1 or x <= x2) and (y1 <= y <= y2):
            counter = counter + 1;
        i += 1

    if (counter == 0):
        #No intersects point lies outside
        return False
    else:
        if((counter % 2) == 0):
            #print("Point lies outside of polygon - {0}".format(given_point))
            return False
        else:
            #print("Point lies inside of polygon - {0}".format(given_point))
            return True


print(check_if_point_lies_inside([[1,0], [8,3], [8,8], [1,5]], [3,5]))
print(check_if_point_lies_inside([[-3,2], [-2,-0.8], [0,1.2], [2.2,0], [2,4.5]], [0,0]))
