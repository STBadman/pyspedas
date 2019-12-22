
from .load import load

def lena(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE LENA data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='lena', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)

def mena(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE MENA data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='mena', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)

def hena(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE HENA data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='hena', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)

def rpi(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE RPI data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='rpi', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)

def euv(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE EUV data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='euv', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)

def fuv(trange=['2004-11-5', '2004-11-6'], 
        datatype='k0',
        suffix='',  
        get_support_data=False, 
        varformat=None,
        downloadonly=False):
    """
    This function loads IMAGE FUV data
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

        datatype: str
            Data type; Valid options:

        suffix: str
            The tplot variable names will be given this suffix.  By default, 
            no suffix is added.

        get_support_data: bool
            Data with an attribute "VAR_TYPE" with a value of "support_data"
            will be loaded into tplot.  By default, only loads in data with a 
            "VAR_TYPE" attribute of "data".

        varformat: str
            The file variable formats to load into tplot.  Wildcard character
            "*" is accepted.  By default, all variables are loaded in.

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables

    Returns:
        List of tplot variables created.

    """
    return load(instrument='fuv', trange=trange, datatype=datatype, suffix=suffix, get_support_data=get_support_data, varformat=varformat, downloadonly=downloadonly)
