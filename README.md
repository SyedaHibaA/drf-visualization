# WIP

# drf-visualization

Just a simple quick project visualizing the publicly available data from the [DRF (Digital Rights Foundation) Pakistan](https://digitalrightsfoundation.pk/) website.

## Explanation of Data Files

### gender_violence_stats.csv
|       Column        | Data Type |                Data Format                |                            Comments                            |
|:-------------------:|:---------:|:-----------------------------------------:|:--------------------------------------------------------------:|
|        Date         |  String   |                %-dxx %B %Y                | Date without zero-padded value + suffix, full month, full year |
|        City         |  String   |                 city name                 |           Does not have double quotes surrounding it           |
|      Province       |  String   | KP, Punjab, Sindh, Balochistan, Islamabad |             String field but fixed type of entries             |
|      Incident       |  String   |                description                |                Long description of the incident                |
|  Type of Violence   |  String   |             short description             |               Short description of the incident                |
|    Age of Victim    |    Int    |                    %d                     |                 Integer age of primary victim                  |
|  Gender of Victim   |  String   |         Male, Female, Transgender         |                 Legal gender of primary victim                 |
| Gender of Victim(s) |  String   |         Male, Female, Transgender         |                     Legal gender of victim                     |
| Gender of Victim(s) |  String   |         Male, Female, Transgender         |                     Legal gender of victim                     |
| Gender of Victim(s) |  String   |         Male, Female, Transgender         |                     Legal gender of victim                     |
| Gender of Victim(s) |  String   |         Male, Female, Transgender         |                     Legal gender of victim                     |
|  News Report Link   |  String   |                    URL                    |                  Link to related news report                   |
|     Follow-up?      |  String   |               Yes or Blank                |                 When no entry, then assumed No                 |
|   Follow-up link    |  String   |                    URL                    |                 Link to follow-up news report                  |
|      Headlines      |  String   |            Headlines from URL             |                     All blank in original                      |

#### Data Collection, Cleaning and Annotation Steps
1. Collected data from [DRF Open Data Initiative](https://digitalrightsfoundation.pk/open-data-for-incidents-of-gender-based-violence-in-pakistan/).
   a. Fixed spelling mistakes
   b. Fixed unique value mistakes (i.e. Sindh written as SIndh)
2. Converted data into CSV file.
3. Removed empty rows.
4. Created documentation of information recorded in file.