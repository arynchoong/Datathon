---
# Database Structure
---
_Data files are not to be uploaded, folder as placeholder only_

    ├── external       <- Data from third party sources.
    ├── interim        <- Intermediate data that has been transformed.
    │   ├── m_*.csv        <- Interim data extracted from MIMIC III data set.
    │   └── e_*.csv        <- Interim data extracted from eICU data set.
    ├── processed      <- The final, canonical data sets for modeling.
    ├── raw            <- The original, immutable data dump.
    │   ├── mimic       <- Data MIMIC III database.
    │   └── eicu        <- Data from eICU database.

---
## command line requesting data
---
__To download MIMIC III database:__

wget --user USERNAME --ask-password -A csv.gz -m -p -E -k -K -np -nd https://physionet.org/works/MIMICIIIClinicalDatabase/files/

__To download eICU database:__

wget --user USERNAME --ask-password -A csv.gz -m -p -E -k -K -np -nd https://physionet.org/works/eICUCollaborativeResearchDatabase/files/

__To unzip:__
gzip -d *.gz
