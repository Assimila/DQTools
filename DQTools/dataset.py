import numpy as np
import re
import textwrap
import pandas as pd
import logging
import datetime
import os.path as op
import sys
from .check_datetime import Datetime_checker

from .connect.connect import Connect
from .regions import get_bounds
from .connect.log.setup_logger import SetUpLogger


class Dataset:
    """
    This is the representation of a DataCube Dataset in the DQTools library.
    """

    def __init__(self, product, subproduct, region=None, tile=None, res=None,
                 identfile=None, sysfile=None,raise_exceptions=False):
        """
        Connect to the datacube and extract metadata for this particular
        product/sub-product.

        Attributes passed from the caller are recorded in self:
        self.product: name of the product
        self.subproduct: name of sub-product
        self.region [optional]: name of region required
        self.tile [optional]: name of tile required


        NOTE: If a region/tile is defined, then metadata pertains only to
        that region or tile. If no region/tile is defined then metadata is
        returned for the entire sub-product extent.

        Empty attributes created for
        - self.data: The xarray DataSet
        - self.timesteps: The timesteps of data available

        :param product: product name (str)

        :param subproduct: sub-product name (str)

        :param region [optional]: the name of a region for data/metadata,
                                  as defined in the regions directory
                                  (NOTE: writing data for regions
                                  is not possible, unless the bounds
                                  exactly match a tile... in which case
                                  just use tile to define our spatial
                                  extent!)

        :param tile [optional]: the tile to extract data/metadata for
                                (must match datacube record)

        :param res [optional]: the resolution of the output data
                               required. This will ultimately enact a
                               GDAL Warp inside the datacube to give
                               you the required resolution within the
                               bounds defined in either tile or region.

        :param identfile: Assimila DQ credentials file required to access the
                         HTTP server. Allows the file to be in a different
                         location as used by the QGIS Plugin.

        :param sysfile: location of the deployed system's yaml file. Required
                        for DASK use.
        """

        # write product & sub-product as attributes
        self.product = product
        self.subproduct = subproduct

        # Write region as an attribute
        self.region = region

        # Write resolution as an attribute
        self.res = res

        # Write tile as an attribute
        self.tile = tile

        # throw exceptions on error
        self.raise_exceptions = raise_exceptions 

        # Create empty attributes for later data
        self.last_timestep = None
        self.first_timestep = None
        self.last_gold = None
        self.fill_value = None
        self.all_subproduct_tiles = None
        self.description = None
        self.time_resolution = None
        self.data = None
        self.timesteps = None

        try:
            # base, extension = op.splitext('./connect/log/dataset.log')
            # today = datetime.datetime.today()
            # log_filename = "{}{}{}".format(base,
            #                                today.strftime("_%Y_%m_%d"),
            #                                extension)
            #
            # SetUpLogger.setup_logger(
            #     log_filename=op.abspath(op.join(op.dirname(__file__),
            #                                     log_filename)),
            #     default_config=op.abspath(op.join(op.dirname(__file__),
            #                    "./connect/log/logging_config.yml")))
            self.logger = logging.getLogger("__main__")

        except Exception:
            raise

        self.logger.info("Dataset created with: product %s, subproduct %s,"
                         "region %s, tile %s, resolution %s,  credentials file %s"
                         % (product, subproduct, region, tile, res, identfile))
        try:
            # Extract the bounds for this region, if provided
            if self.region:
                bounds = get_bounds(self.region)._asdict()
            else:
                bounds = None

        except RuntimeError as e:
            self.logger.error("Failed to initialise Dataset regions.\n"
                              "%s" % e)
            print("Failed to initialise Dataset regions, "
                  "please see logfile for details.")
            sys.exit(1)

        try:
            # Instantiate the datacube connector
            self.conn = Connect(identfile=identfile, sysfile=sysfile)

            # Download metadata for this product & sub-product & tile
            result = self.conn.get_subproduct_meta(product=self.product,
                                                   subproduct=self.subproduct,
                                                   bounds=bounds,
                                                   tile=tile)

            # Extract relevant metadata as attributes.
            self._extract_metadata(result)

            # self.logger.info(f"Dataset created and metadata available for "
            #                  f"{self.product} : {self.subproduct}")
            self.logger.info("Dataset created and metadata available for %s %s"
                             % (self.product, self.subproduct))

        except Exception as e:
            self.logger.error("Failed to retrieve Dataset metadata.\n"
                              "%s" % e)
            print("Failed to retrieve Dataset metadata, "
                  "please see logfile for details.")

    def __repr__(self):
        """
        User-friendly representation of the dataset object

        :return:
        """
        try:
            return """<DQ Dataset: {product}-{subproduct}>
================================================================================
Product:        {product}
Sub-product:    {subproduct}
================================================================================
{desc}

Tiles:
    In datacube:    {tiles}
    Selected tile:  {tile}

Timesteps available:
    First:          {first}
    Last:           {last}
    Resolution:     {tres}

Last Gold:          {last_gold}
================================================================================
Data:
{data}
================================================================================
        """.format(product=self.product,
                   subproduct=self.subproduct,
                   desc=textwrap.fill(self.description, 79),
                   tiles=self.all_subproduct_tiles,
                   tile=self.tile,
                   first=self.first_timestep,
                   last=self.last_timestep,
                   tres=str(self.time_resolution),
                   last_gold=self.last_gold,
                   data=self.data)

# TODO re-instate this once we ditch support for Python 2.7
#             return f"""<DQ Dataset: {self.product}-{self.subproduct}>
# ================================================================================
# Product:        {self.product}
# Sub-product:    {self.subproduct}
# ================================================================================
# {textwrap.fill(self.description, 79)}
#
# Tiles:
#     In datacube:    {self.all_subproduct_tiles}
#     Selected tile:  {self.tile}
#
# Timesteps available:
#     First:          {self.first_timestep}
#     Last:           {self.last_timestep}
#     Resolution:     {str(self.time_resolution)}
#
# Last Gold:          {self.last_gold}
# ================================================================================
# Data:
# {self.data}
# ================================================================================
#             """

        except Exception as e:
            self.logger.error("Error displaying Dataset metadata.\n"
                              "%s" % e)
            print("Error displaying Dataset's metadata.")

    def _extract_metadata(self, all_meta):
        """
        Extract the metadata required to populate the attributes on
        initialisation. This parses the metadata sent from the data cube
        to extract and records key parameters:

        Metadata parameters created:
        - self.last_gold: The last 'good' time step of data. Defined by
        developer.
        - self.last_timestep: The last time step of data recorded in the
          DataCube
        - self.first_timestep: The first time step of data recorded in
          the DataCube
        - self.fill_value: The fill value for this data
        - self.all_subproduct_tiles: All tiles available for this
          sub-product in the data cube
        - self.tiles: The tile currently selected in this instance

        :param all_meta: metadata dump from the data cube 'get meta'
                         request

        :return:
        """

        self.time_resolution = all_meta['time_resolution']
        self.first_timestep = all_meta['first_timestep']
        self.last_timestep = all_meta['last_timestep']
        self.last_gold = all_meta['last_gold']
        self.fill_value = all_meta['fill_value']
        self.all_subproduct_tiles = all_meta['all_subproduct_tiles']
        self.description = all_meta['description']

    def get_data(self, start, stop,
                 use_dask=False,
                 region=None, tile=None, res=None, latlon=None,
                 country=None, projection=None):
        """
        Extract data from the datacube to the specification supplied.

        :param start:   Start datetime for dataset

        :param stop:    Stop datetime for dataset

        :param use_dask: optional - set to True to obtain pointer to vrt file
                        on the server, default False to return data in xarray.

        :param region:  optional - geographic region, do not use tile too

        :param tile:    optional - specific tile, do not use region too
                        Tile or region are only needed here if not already
                        given when creating the Dataset object.

        :param res:     optional - resolution required
                        If providing a country and therefore expecting zonal
                        averaging, it is recommended to set this value to 0.01
                        to super-sample the data and ensure each county has
                        at least one pixel.

        :param country: optional - if country name is supplied, the returned
                        dataset will have been zonally averaged according to
                        county definitions within that country. The country
                        name is case insensitive but must be one for which
                        the system has a shapefile defining its counties.

        :param latlon:  optional - argument to extract pixel information for
                        a specific latitude and longitude location.

        :param projection: optional - use one of the common names or a Proj4
                        text string fully defining the projection. If none
                        is provided, the system exports data in its native
                        form.

        :return: xarray of data
        """
        self.logger.info("Dataset get_data args: start %s, stop %s, DASK %s,"
                         "region %s, tile %s, resolution %s, latlon %s, "
                         "country %s, projection %s"
                         % (start, stop, use_dask,
                            region, tile, res, latlon,
                            country, projection))

        try:
            # Extract the bounds information
            if region:
                bounds = get_bounds(region)
            elif self.region:
                bounds = get_bounds(self.region)
            else:
                bounds = None

            # Extract tile info
            if not tile and self.tile:
                tile = self.tile

            # Extract res info
            if not res and self.res:
                res = self.res

            new_start = Datetime_checker(time=start)
            start = new_start.c_and_c()
            new_stop = Datetime_checker(time=stop)
            stop = new_stop.c_and_c()

            # Fetch the data from the datacube
            data = self.conn.get_subproduct_data(product=self.product,
                                                 subproduct=self.subproduct,
                                                 start=start,
                                                 stop=stop,
                                                 use_dask=use_dask,
                                                 bounds=bounds,
                                                 res=res,
                                                 tile=tile,
                                                 country=country,
                                                 latlon=latlon,
                                                 projection=projection)

            self.data = data[0]

        except Exception as e:
            print_msg = ""
            if not use_dask:
                self.logger.error("Failed to retrieve Dataset sub-product data.\n"
                                  "%s" % e)
                print_msg = ("Failed to retrieve Dataset sub-product data,",
                            "please see logfile for details.")
            else:
                self.logger.error("Failed to retrieve Dataset sub-product DASK "
                                  "pointer.\n%s" % e)
                print_msg = ("Failed to retrieve Dataset sub-product DASK pointer, ",
                            "please see logfile for details.")
            print (print_msg)
            if self.raise_exceptions:
                raise Exception(print_msg) from None

    def put(self, tile=None):
        """
        Prepare self.data and metadata, then send to the datacube.
        :param tile: Optionally provide the tile for the data. If not present,
                     the tile specified in the Dataset creation will be used.
                     The tile name will be checked against those for which the
                     Dataset is registered.
        :return:
        """

        try:
            # Add product as an attribute to the data which will be written
            self.data.attrs['product'] = self.product

            # Ensure we specify the tile in the attributes
            if not tile:
                self.data.attrs['tile'] = self.tile
            else:
                if tile in self.all_subproduct_tiles:
                    self.data.attrs['tile'] = tile
                else:
                    raise NameError("tile name must be valid for this product")

            # Process last gold. This value needs to go into the DataArray
            # attributes. The user could set them here, in the DataSet
            # attributes or in self.data.attrs. Easiest if we just catch and
            # process all possibilities.
            if 'last_gold' not in self.data[self.subproduct].attrs or \
                    self.data[self.subproduct].attrs['last_gold'] is None:

                if 'last_gold' not in self.data.attrs:
                    self.data[self.subproduct].attrs['last_gold'] = self.last_gold
                else:
                    self.data[self.subproduct].attrs['last_gold'] = \
                        self.data.attrs['last_gold']

            # Check that this has given us a last gold
            if not self.data[self.subproduct].attrs['last_gold']:
                raise Exception("Last gold not set for %s " % self.subproduct)
                # raise Exception(f"Last gold not set for {self.subproduct}")

            if self.subproduct not in self.data.data_vars.keys():
                raise NameError("data.name must be equal to sub-product for "
                                "ingesting into the datacube")

            # Assign parent attributes to data variable
            for x in self.data.attrs:
                self.data[self.subproduct].attrs[x] = self.data.attrs[x]

            # Instantiate the datacube connector
            conn = Connect()

            # Put the data into the datacube
            conn.put_subproduct_data(data=self.data)

        except Exception as e:
            msg = "Failed to write data to the datacube."
            self.logger.error(f"{msg}.\n{str(e)}")
            print(msg)
            if self.raise_exceptions:
                raise Exception(msg) from None

    def update(self, script, params=None):
        """
        Update this dataset using the update method in the script
        supplied. Following the calculation, re-initialise from the
        DataCube to update the metadata.

        :param script: The python script for updating this dataset
        :param params: A dictionary of keyword arguments to be passed
                       to the update method

        :return:
        """
        self.logger.info("Dataset update with script %s, params %s"
                         % (script, params))
        try:
            # Run the update script with the appropriate parameters
            if params:
                script.update(**params)
            else:
                script.update()

            # Re-initialise dataset information after update
            self.__init__(self.product, self.subproduct, region=self.region,
                          tile=self.tile)

        except Exception as e:
            self.logger.error("Failed to update the Dataset from script %s.\n"
                              "%s" % (e, script))
            msg = "Failed to update the Dataset from script %s" % script
            print(msg)
            if self.raise_exceptions:
                raise Exception(msg) from None

    def calculate_timesteps(self):
        """
        Calculate the time steps available, given the time_resolution of the
        dataset (as recorded in the sub-product table) and the first and
        last time steps.

        NOTE: This method calculates ideal timesteps, rather than
        retrieving the actual timesteps of the data. This method cannot
        know about any data gaps.

        :return:
        """

        try:
            # split the numpy timedelta into its component parts (e.g.
            # ['year', 1])
            bf_fq_vals = self.time_resolution.__str__().split(' ')

            # Create a pandas DataOffset object which represents this
            # time_resolution
            time_resolution = pd.DateOffset(**{bf_fq_vals[1]: int(bf_fq_vals[0])})

            # Generate an array, using this as the step
            if self.first_timestep:
                timesteps = pd.date_range(self.first_timestep,
                                          self.last_timestep,
                                          freq=time_resolution)

                self.timesteps = timesteps.values

            else:
                self.timesteps = None

        except Exception as e:
            self.logger.error("Unable to calculate timesteps.\n"
                              "%s" % e)
            raise RuntimeError("Unable to calculate timesteps.")

    def set_last_gold(self, date_time):
        """
        When adding data to a newly registered product/sub-product, there will
        be no extant last_gold information and thus it needs to be set by the
        user.
        :param date_time:
        :return: N/A
        """
        if not self.last_gold:
            # convert whatever we've been given into a datetime
            dtg = Datetime_checker(date_time)
            last_gold = dtg.c_and_c()
            self.data[self.subproduct].attrs['last_gold'] = last_gold
        else:
            self.logger.warning("Last gold already exists and will be used, "
                                "your setting has been ignored.")
