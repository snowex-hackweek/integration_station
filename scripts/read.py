import fnmatch
from intake.catalog import Catalog
import os
import xarray as xr

"""
IMPORTANT NOTES

This code is currently UNDER DEVELOPMENT for the icepyx (https://github.com/icesat2py/icepyx) library for working with ICESat-2 data.
This version of the code is static and will only be manipulated as needed for the July 2021 SnowEx Hackweek project.
Ultimately, this functionality will be improved, tested, and included as a standard part of the icepyx package.
You're encouraged to use that version in any workflows for tracibility and reproducibility, as this version will not be maintained.
Please contact Jessica (@JessicaS11) for more info or with any questions.
"""


def _get_datasource_type():  # filepath):
    """
    Determine if the input is from a local system or is an s3 bucket
    Not needed now, but will need to use for cloud data access
    """

    source_types = ["is2_local", "is2_s3"]
    return source_types[0]


def _validate_source(source):
    """
    Check that the entered data source paths are valid
    """

    # acceptable inputs (for now) are a single file or directory
    assert type(source) == str, "You must enter your input as a string."
    assert (
        os.path.isdir(source) == True or os.path.isfile(source) == True
    ), "Your data source string is not a valid data source."
    return True


def _pattern_to_glob(pattern):
    """
    Adapted from intake.source.utils.path_to_glob to convert a path as pattern into a glob style path
    that uses the pattern's indicated number of '?' instead of '*' where an int was specified.

    Returns pattern if pattern is not a string.

    Parameters
    ----------
    pattern : str
        Path as pattern optionally containing format_strings

    Returns
    -------
    glob : str
        Path with int format strings replaced with the proper number of '?' and '*' otherwise.

    Examples
    --------
    >>> _pattern_to_glob('{year}/{month}/{day}.csv')
    '*/*/*.csv'
     >>> _pattern_to_glob('{year:4}/{month:2}/{day:2}.csv')
    '????/??/??.csv'
    >>> _pattern_to_glob('data/{year:4}{month:02}{day:02}.csv')
    'data/????????.csv'
    >>> _pattern_to_glob('data/*.csv')
    'data/*.csv'
    """
    from string import Formatter

    if not isinstance(pattern, str):
        return pattern

    fmt = Formatter()
    glob = ""
    prev_field_name = None
    for literal_text, field_name, format_specs, _ in fmt.parse(pattern):
        glob += literal_text
        if field_name and (glob[-1] != "*"):
            try:
                glob += "?" * int(format_specs)
            except ValueError:
                glob += "*"
                # alternatively, you could use bits=utils._get_parts_of_format_string(resolved_string, literal_texts, format_specs)
                # and then use len(bits[i]) to get the length of each format_spec
    # print(glob)
    return glob


def _run_fast_scandir(dir, fn_glob):
    """
    Quickly scan nested directories to get a list of filenames that match the fn_glob string.
    Modified from https://stackoverflow.com/a/59803793/2441026
    (faster than os.walk or glob methods, and allows filename matching in subdirectories).

    Parameters
    ----------
    dir : str
        full path to the input directory

    fn_glob : str
        glob-style filename pattern

    Outputs
    -------
    subfolders : list
        list of strings of all nested subdirectories

    files : list
        list of strings containing full paths to each file matching the filename pattern
    """

    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if fnmatch.fnmatch(f.name, fn_glob):
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = _run_fast_scandir(dir, fn_glob)
        subfolders.extend(sf)
        files.extend(f)

    return subfolders, files


def _check_source_for_pattern(source, filename_pattern):
    """
    Check that the entered data source contains files that match the input filename_pattern
    """
    glob_pattern = _pattern_to_glob(filename_pattern)

    if os.path.isdir(source):
        _, filelist = _run_fast_scandir(source, glob_pattern)
        assert len(filelist) > 0, "None of your filenames match the specified pattern."
        print(
            f"You have {len(filelist)} files matching the filename pattern to be read in."
        )
        return True
    elif os.path.isfile(source):
        assert fnmatch.fnmatch(
            os.path.basename(source), glob_pattern
        ), "Your input filename does not match the filename pattern."
        return True
    else:
        return False


class Read:
    """
    Data object to create and use Intake catalogs to read ICESat-2 data into the specified formats.
    Provides flexiblity for reading nested hdf5 files into common analysis formats.

    Parameters
    ----------
    data_source : string
        A string with a full file path or full directory path to ICESat-2 hdf5 (.h5) format files.
        Files within a directory must have a consistent filename pattern.

    filename_pattern : string, default 'ATL{product:2}_{datetime:%Y%m%d%H%M%S}_{rgt:4}{cycle:2}{orbitsegment:2}_{version:3}_{revision:2}.h5'
        String that shows the filename pattern as required for Intake's path_as_pattern argument.
        The default describes files downloaded directly from NSIDC (subsetted and non-subsetted).

    catalog : string, default None
        Full path to an Intake catalog for reading in data.
        If you still need to create a catalog, leave as default.

    out_obj_type : object, default xarray.Dataset
        The desired format for the data to be read in.
        Currently, only xarray.Dataset objects (default) are available.
        Please ask us how to help enable usage of other data objects!

    Returns
    -------
    read object

    Examples
    --------

    """

    # ----------------------------------------------------------------------
    # Constructors

    def __init__(
        self,
        data_source=None,
        filename_pattern="ATL{product:2}_{datetime:%Y%m%d%H%M%S}_{rgt:4}{cycle:2}{orbitsegment:2}_{version:3}_{revision:2}.h5",
        catalog=None,
        out_obj_type=None,  # xr.Dataset,
    ):

        if data_source == None:
            raise ValueError("Please provide a data source.")
        else:
            assert _validate_source(data_source)
            self.data_source = data_source

        assert _check_source_for_pattern(data_source, filename_pattern)
        # Note: need to check if this works for subset and non-subset NSIDC files (processed_ prepends the former)
        self._pattern = filename_pattern

        # after validation, use the notebook code and code outline to start implementing the rest of the class
        if catalog:
            print("validate catalog")
            self._catalog_path = catalog

        if out_obj_type:
            print(
                "Output object type will be an xarray DataSet - no other output types are implemented"
            )
        self._out_obj = xr.Dataset

        self._source_type = _get_datasource_type()

    # ----------------------------------------------------------------------
    # Properties

    @property
    def catalog(self):
        """
        Print the catalog.

        Examples
        --------
        >>>
        """
        if not hasattr(self, "_catalog"):
            return open(self._catalog_path, "r").read()
        else:
            return self._catalog

    # ----------------------------------------------------------------------
    # Methods
    def build_catalog(self, var_paths="/gt1l/land_ice_segments", **kwargs):
        """"""
        from intake.catalog.local import LocalCatalogEntry
        import intake_xarray

        import icepyx.core.APIformatting as apifmt

        xarray_kwargs_dict = {"engine": "h5netcdf", "group": var_paths}

        source_args_dict = {
            "urlpath": self.data_source,
            "path_as_pattern": self._pattern,
            "xarray_kwargs": xarray_kwargs_dict,
        }

        metadata_dict = {"version": 1}

        source_dict = {
            "name": self._source_type,
            "description": "",
            "driver": intake_xarray.netcdf.NetCDFSource,
            "args": source_args_dict,
        }

        local_cat_source = {self._source_type: LocalCatalogEntry(**source_dict)}

        defaults_dict = {
            "name": "IS2-hdf5-icepyx-intake-catalog",
            "description": "an icepyx-generated catalog for creating local ICESat-2 intake entries",
            "metadata": metadata_dict,
            "entries": local_cat_source,
        }

        build_cat_dict = apifmt.combine_params(defaults_dict, kwargs)

        self._catalog = Catalog.from_dict(**build_cat_dict)