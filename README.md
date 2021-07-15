# integration_station

## Files

* `.gitignore`
<br> Globally ignored files by `git` for the project.
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project (see suggested headings below)

## Folders

### `contributors`
Each team member has it's own folder under contributors, where they can work on their contribution. Having a dedicated folder for each person helps to prevent conflicts when merging with the main branch.

### `notebooks`
Notebooks that are considered delivered results for the project should go in here.

### `scripts`
Helper utilities that are shared with the team

# Recommended content for your README.md file:

## Project Summary
Project repistory to develop tools and framework to easily integrate available in situ datasets over Grand Mesa for use as calibration/validation for remote sensing datasets and spatially-distributed models. Emphasis on snow depth (and potentially SWE) measurements.

### Project Title

Integration_station: Towards a sandbox for SnowEx datasets

### Collaborators on this project

* [Max Stevens](https://github.com/maximusjstevens)
* [Mitch Creelman](https://github.com/mcreelma)
* [Seth Vanderwilt](https://github.com/sethv)
* [Shad O'Neel](https://github.com/shad)
* [Ryan Crumley](https://github.com/ryanlcrumley)
* [Gifty Attiah](https://github.com/geattiah)
* [Tri Datta](https://github.com/tridatta)
* [Mansi Joshi](https://github.com/mansi278)
* [Jessica Scheick](https://github.com/jessicas11)
* [Shashank Bhushan](https://github.com/shashankBice) (Data science helper)
* [Michelle Hu](https://github.com/jmichellehu) (Project Lead)

### The problem

The snowex capaign(s) produce a treasure trove of datasets measuring different physical parameters such as snow depth, density, temperatures, ASO LiDAR etc. From a purely exploratory measure, we can use this awesome treasure trove to validate and calibrate satellite remote sensing and model derived outputs. The calibration 

### Application Example

List one specific application of this work.

### Sample data
* SnowEx
    * Snow pits https://nsidc.org/data/SNEX20_GM_SP/versions/1
    * Depth transects https://nsidc.org/data/SNEX20_SD/versions/1, depth spirals
    * ASO Lidar, USGS 3DEP
    * ?Time lapse camera snow depths (gives high time resolution perhaps)?
    * GPR depths
* External
    * IS2
    * CryoSat
    * RS imagery
    * Weather station data (SNOTEL, other AWS bits)



### Specific Questions

Some specifics questions(tasks) which we want to answer(accomplish) during the hackweek:
* Query: run through tutorial, work on extracting via bounding box, work towards developing streamlined functions for SnowEx datasets
* Query and fetch external datasets (IceSat-2/Snotel)
* Preprocessing: Alignment of elevation datasets
* Comparison of datasets, exploring interpolation techniques to create rasters from point datasets.
### Existing methods

How would you or others traditionally try to address this problem?

### Proposed methods/tools

Building from what you learn at this hackweek, what new approaches would you like to try to implement?

### Background reading

Optional: links to manuscripts or technical documents for more in-depth analysis.

