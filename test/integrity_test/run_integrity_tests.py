import os.path as op
import sys
import datetime as dt
from calendar import monthrange
from osgeo import gdal
import argparse
import yaml
import re
import numpy as np

sys.path.append('../../../datacube')
from src.datacube.system_settings import SysSettings
sys.path.append('../..')
from DQTools import Dataset

datacube_root='/datacube'
#product='tamsat'
#subproduct='rfe'
#tile='tamsat_extent'
#
# Simple  integrity checker.
# Written before I knew about this:
# /workspace/System_Dashboard/gdal_data_check.py
#
# which seems to have similar functionality.

def get_SNWE_from_tile(config_dict_tile):
    """
    Get South, North,West,East limits from a dict read from tile yaml.
    """
    #bb = config_dict_tile[0]['bbox'] # used to be like this - has the format changed?
    bb = config_dict_tile['bbox']
    # bounding box bb is just a string that looks like this:
    # '((-19.0 38.0 0, -19.0 -36.0 0, 53.0 -36.0 0, 53.0 38.0 0, -19.0 38.0 0))'
    # convert it to a matrix:
    corners = re.sub('[()]','',bb).split(',') # remove brackets, and split on ','
    coords= [ c.split(' ')  for c in corners ]  # split the splits again, on spaces.
    bb = [  [float(c)  for c in clist  if len(c)>0] for clist in coords ] # remove empties and, convert to floats

    np_bb = np.array(bb)
    south_lat = min(np_bb[:,1]) # -36.0 for Africa
    north_lat = max(np_bb[:,1]) # 38.0 for Africa
    west_lon =  min(np_bb[:,0]) # -19.0 for Africa
    east_lon =  max(np_bb[:,0]) # 53.0 for Africa
    return (south_lat , north_lat , west_lon , east_lon)


def create_parser(args=None):

    """
    The 'required' flag ensures an argument is provided.

    :return: Invocation arguments
    """
    parser = argparse.ArgumentParser(description='start year controlled by -y argument,'
                                                 'product controlled by -p argument'
                                                 'subproduct controlled by -s argument'
                                                 'tile name -t argument'
                                                 'system setup controlled by -f argument.'
                                                 'productxsubproductxtile combinations controlled by -c argument.'
                                                 '-c negates the need for -p -s -t')

    parser.add_argument("-p",
                        "--product",
                        type=str,
                        help=("input rainfall product to create derived product and subproducts from"),
                        default="tamsat")

    parser.add_argument("-s",
                        "--subproduct",
                        type=str,
                        help=("input rainfall sub product to create derived product and subproducts from"),
                        default="rfe")

    parser.add_argument("-t",
                        "--tile",
                        type=str,
                        help="tile name for rainfall data",
                        default='tamsat_extent')

    ## Either the three above, or the following must be specified:
    parser.add_argument("-c",
                        "--combos_file",
                        type=str,
                        help="productxsubproductxtile combinations to check",
                        required=False)
    """
    combos files can be created using this select statement, saving the results to
    a file, remove header lines and change '|' characters to commas:

 select product.name, subproduct.name, tile.name from subproduct inner join product on subproduct.idproduct=product.idproduct inner join relsubproducttile on subproduct.idsubproduct = relsubproducttile.idsubproduct inner join tile on relsubproducttile.idtile = tile.idtile where product.name in
('chirps', 'era5', 'gfs', 'gpm', 'era5_land', 'arc2', 'tamsat', 'ecmwf_operational_archive') order by product.name, subproduct.name, tile.name;
    """

    parser.add_argument("-y",
                        "--start_year",
                        type=int,
                        help=("Start year"),
                        default=2020)
    parser.add_argument("-m",
                        "--start_month",
                        type=int,
                        help=("Start month"),
                        default=1)
    parser.add_argument("-f",
                        "--config_file",
                        type=str,
                        help="System configuration settings file with relative path.",
                        required=True)

    return parser.parse_args(args=args)


today = dt.date.today()
current_year = int(today.strftime('%Y'))
current_month = int(today.strftime('%-m') )
sub_divs=10

def check_product_subproduct_tile_combination(start_year,start_month,product,subproduct,tile,tile_in_tile_file=None):

    tile_file='../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml'
    with open(tile_file, 'r') as file:
        config_dict_tiles = yaml.full_load(file)

    if tile_in_tile_file is None:
        tile_in_tile_file = tile
    config_dict_tile = None
    for entry in config_dict_tiles:
        if entry['name'] == tile_in_tile_file:
            config_dict_tile = entry
            break

    if config_dict_tile is None:
        print (f"Can't find {tile} in {tile_file}")
        return    

    data = Dataset(product=product, subproduct=subproduct )
    (south_lat , north_lat , west_lon , east_lon ) = get_SNWE_from_tile(config_dict_tile)
    # don't need all the tile - specify a small part of it to save time
    ns_div = (north_lat - south_lat)/ sub_divs
    ew_div = (east_lon - west_lon)/ sub_divs

    print( '%30s  %30s  %30s' % (product,subproduct,tile))
    print( '===============================================================')
    for year in range(int(start_year),current_year +1):
        months = 12
        if year == current_year:
            months = current_month
        sm=1
        if year == start_year:
            sm=start_month
        for month in range(sm,months+1):

            bands_in_db= None
            data.data=None # Otherwise, if there is no data, data.data still has previous data.?!?
            try:
                data.get_data(start=dt.datetime(year, month, 1),
                            stop=dt.datetime(year, month, monthrange(year,month)[1],23,59,59,999999),
                            region=[north_lat,west_lon + ew_div , north_lat - ns_div, west_lon ])
                            # region=[north, east, south, west])
            except Exception as e:
                print (e)
                pass

            if data.data is not None:
                bands_in_db = data.data['time'].shape[0]
            fname = f'/{datacube_root}/{product}/{subproduct}/{tile}/{product}_{subproduct}_{tile}_{year}-{month:02}.tif'
            bands_in_file = None
            if op.exists(fname):
                d = gdal.Open(fname)
                if d is not None:
                    bands_in_file = d.RasterCount
                else:
                    print (f'Invalid geotif file:{fname}')
            
            if bands_in_file != bands_in_db:
                print(f'MISMATCH:{year}-{month} db:{bands_in_db} - {bands_in_file} in {fname}')
            else:
                print(f'OK:{year}-{month} db:{bands_in_db} - {bands_in_file} in {fname}')
                #pass  

parse_args = create_parser()
sys_config = SysSettings(parse_args.config_file) 

#data = Dataset(product='tamsat', subproduct='rfe' ,sysfile=parse_args.config_file)
if not parse_args.combos_file:
    check_product_subproduct_tile_combination(parse_args.start_year,parse_args.start_month,parse_args.product,parse_args.subproduct,parse_args.tile)
else:
    with open (parse_args.combos_file, 'r')  as f:
        for line in f:
            if re.search('^[ \t]*#', line) == None: # ignore comments
                line=line.replace("\n",'').replace(' ','')
                splt = line.split(',')
                check_product_subproduct_tile_combination(parse_args.start_year,parse_args.start_month,*splt)

