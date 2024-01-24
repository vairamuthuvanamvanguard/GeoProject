 # Import the library
from geo.Geoserver import Geoserver

# Initialize the library
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='Skyblue@1002')

# For creating workspace
# geo.create_workspace(workspace='demo')
# geo.create_coveragestore(layer_name='layer1', path=r'../data/clipped.tif', workspace='demo')

geo.create_featurestore(store_name='geo_data', workspace='demo', db='postgres', host='localhost', pg_user='postgres',
                        pg_password='muthu12345')
