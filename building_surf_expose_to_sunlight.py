#To Calculate the surface of the building exposed to sunlight
#Calculate the maximum of x-cordinates from all points and subtract the lowest of x-cordinates from max of x-cordinates. Similarly, do it for y-cordinates and add both these results will give the surface area exposed to sunlight

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

    return result

def area_expose_to_sunlight(building_cordinates, source_point):
    number_of_buildings = len(building_cordinates)
    j = 0
    get_y_cordinates_all_buildings = []
    buildings_area = []
    while(j < len(building_cordinates)):
        x = []
        y = []
        building = building_cordinates[j]
        i = 0
        while i < len(building):
            cordinate = building[i]
            x.append(cordinate[0])
            y.append(cordinate[1])
            i += 1

        max_x_cordinate = max(x)
        min_x_cordinate = min(x)
        max_y_cordinate = max(y)
        min_y_cordinate = min(y)
        get_y_cordinates_all_buildings.append(y)

        x_surface = max_x_cordinate - min_x_cordinate
        y_surface = max_y_cordinate - min_y_cordinate

        total_surface_expose_to_sunlight = x_surface + y_surface
        #print(total_surface_expose_to_sunlight)
        buildings_area.append(total_surface_expose_to_sunlight)
        j += 1

    if (len(buildings_area) == 2):
        #Here check wether y cordinates of all buildings have same values in common
        if (common_data(get_y_cordinates_all_buildings[0], get_y_cordinates_all_buildings[1])):
            sun_tangent = 2.89
            shawdow_length = float(min(buildings_area))/sun_tangent
            total_surf_exp_to_sunlight = max(buildings_area) + shawdow_length
        else:
            total_surf_exp_to_sunlight = max(buildings_area) + min(buildings_area)

    elif(len(buildings_area) == 1):
        #print("Length of surface exposed to sunlight - {0}".format(buildings_area[0]))
        total_surf_exp_to_sunlight = max(buildings_area)

    return float(total_surf_exp_to_sunlight)

surf_exposed_to_sunlight = area_expose_to_sunlight([[[4,0],[4,-5],[7,-5],[7,0]]], [1,1])
print(surf_exposed_to_sunlight)
surf_exposed_to_sunlight = area_expose_to_sunlight([[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]], [-3.5,1])
print(surf_exposed_to_sunlight)