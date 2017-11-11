	mymap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
	lat, lng = mymap.geocode("Stanford University")
	path = [(37.429, 37.428), (-122.145, -122.145)]
	mymap.plot(path[0], path[1], "plum", edge_width=5)
	mymap.draw('./mymap.html')