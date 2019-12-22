import os

CONFIG = {'local_data_dir': 'image_data/',
          'remote_data_dir': 'https://spdf.sci.gsfc.nasa.gov/pub/data/image/'}

# override local data directory with environment variables
if os.environ.get('ROOT_DATA_DIR'):
    CONFIG['local_data_dir'] = os.sep.join([os.environ['ROOT_DATA_DIR'], 'image'])

if os.environ.get('IMAGE_DATA_DIR'):
    CONFIG['local_data_dir'] = os.environ['IMAGE_DATA_DIR']