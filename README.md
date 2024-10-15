# ClassChargeLoad Python Class

## Description
The Python class "ChargeCurve.py" was developed to process and retrieve energy demand and temperature profiles derived from the Polysun simulation for different building categories and refurbishment scenarios, based
 on the limit and target values for the building energy demand performance required by the SIA380/1. 
The class allows retrieving the hourly profiles of the building specific energy demand (in [kWh/m2]). But while in the base building model case the profile has to be denormalized to correspond to the annual energy 
need provided in input for the pre-refurbishment case, the specific energy demand profiles for the limit and target scenarios can be adopted after rescaling on the effective REA of the building under investigation.

## Features
- Load energy demand data from Polysun simulations for a building use type chosen among the following:  
      - Administration  
      - Commerce  
      - Educationi  
      - Sport  
      - Hospital  
      - Industries  
      - Res_ind  
      - Res_multi  
      - Res_multi_Lau  
- Retreive the energy demand profiles corresponding to the 3 refurbishment scenarios (base, limit and target) and for the REA provided in input.
- Extract temperature profiles at substations.

## Attributes

| Attribute          | Type       | Description   |
|--------------------|------------|---------------|
| affectation        | str        |Building category, chosen among the following: Administration, Commerce, Education, Hospital, Industry, Res_ind (i.e., single family house), Res_multi (i.e., multi-dwelling housing)|
| annual_consumption | float      |The annual energy demand of the building. Value used to de-normalize the energy demand profiles; in [kWh/an]|
| SRE                | float      |The Reference Energy Area (REA) in [m2]|
| Lausanne           | bool       |Flag to select the refurbishments scenarios with change in substation design to a decentralized solution for DHW preparation for the "res_multi" case only.|
| index_year         | int        |year to be used in the construction of an hourly index|

## Methods

-	load_DB(self):  
Returns the local database contained in a Pyarrow archive with the specific load curves corresponding to the building use type provided in the "affectation" attribute and for the REA provided in input.


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/LESBAT-HEIG-VD/ClassChargeLoad
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
