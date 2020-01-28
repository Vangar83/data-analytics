import pandas as pd
import gmplot
from IPython.display import display

data = pd.read_excel('Locations.xlsx')



# latitude and longitude list 
latitude_list = data['LATITUDE'] 
longitude_list = data['LONGITUDE'] 

# center co-ordinates of the map 
gmap = gmplot.GoogleMapPlotter(00.00000,0.0000000,0)

# plot the co-ordinates on the google map 
gmap.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = True) 

# the following code will create the html file view that in your web browser

gmap.heatmap(latitude_list, longitude_list)


gmap.draw( "mymap.html" )
