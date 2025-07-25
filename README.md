# DQTools

Tools for working with the DataCube. Includes reading metadata, registering new products and writing new data to the Datacube.

There are two branches:

`release` contains the latest tested code which works with the released DataCube code used on the publicly available server. 
It will have tagged releases and users are strongly advised to download and use the latest release.
  
`devel` contains development code not suitable for use with the publicly available DataCube server.

## Credentials

In order to authenticate with a DataCube server you must provide a "security identity file".
This file, provided by Assimila, should be placed within the DQTools source code at `DQTools/connect/.assimila_dq`.
Alternately, the file path can be specified to the client module if the key file lives elsewhere on the user's system or has a different name.
