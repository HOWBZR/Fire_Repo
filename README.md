# WildFire Severity
## Executive Summary
In this project, we attempt to predict the severity of a forest fire given a set of conditions in an effort to assist communities and fire fighting services an opportunity to better prepare for a potentially large fire. The research and modeling done here was done for the United States. 
First, significant research was done to identify contribuing factors to forest fires. From there we set out to collect our data which can be observed below. Using the data gathered and knowledge gained through our research, we were able to build a model that predicts how large a forest fire would be if it happend with approx 71% accuracy. Considering the baseline percentage to beat was 33%, this model provides a considerable advantage to those chose to leverage it's predicting power.
</br>


## Problem Statement
Wildfires are a serious problem faced by communities around the country. In 2021 there were over 50,000 wildfires nationwide (U.S. Wildfire Statistics | Bankrate).  Due to the effects of climate change wildfires will only get worse.
As citizens against climate change, we as a team want to identify and predict how severe a fire will be based on a variety of factors. By predicting areas at risk for severe fire, we can give these communities time to prepare and take preventative measures. Some of the considerations that we want to include when predicting these communities of vulnerability are their temperature, precipitation, drought, and location.



</br>



## Data Dictionary

|Feature|Type|Description|
  |---|---|---|
  |Unique Fire Identifier|Object|	Unique identifier assigned to each wildland fire.  yyyy = calendar year, SSUUUU = POO protecting unit identifier (5 or 6 characters), xxxxxx = local incident identifier (6 to 10 characters) |
  |Lattitude|Object|lattitude coordinates for the fire incident|
  |Longitude|Object|longitude coordinates for the fire incident|
  |Fire Cause|Object|Broad classification of the reason the fire occurred identified as human, natural or unknown. |
  |State|Object|Abbreviation of the state where fire originated|
  |Origin County|Object|	The County Name identifying the county or equivalent entity at point of origin designated at the time of collection.|
  |Acres Burned|float64|	A measure of acres reported for a fire.  More specifically, the number of acres within the current perimeter of a specific, individual incident, including unburned and unburnable islands.  The minimum size must be 0.1.
  |Incident Name|Object|The name assigned to an incident|
  |IsFSAssisted|Object|Indicates if the Forest Service provided assistance on an incident outside their jurisdiction.|
  |Year|float64|Calendar year that the fire originated in|
  |Month|float64|Calendar month that the fire originated in|
  |Value|float64|The average temperature for the state and month|
  |Anomaly|float64|The average difference of the value compared to the historical average|
  |Area (acres) |float64|Area (in acres) of the State|
  |Population |float64|Population of the State | 
  |D0|float64|Drought Intensity - Abnormally Dry|
  |D1|float64|Drought Intensity - Moderate Drought|
  |D2|float64|Drought Intensity - Severe Drought|
  |D3|float64|Drought Intensity - Extreme Drought|
  |D4|float64|Drought Intensity - Exceptional Drought|
  |DSCI summed|float64|The sum of D0-D4|
  |DSCI avg|float64|The average of D0-D4|
  |Precipitation (in)|float64|Avergae rainfall in inches for that State and month|
</br>
  ## Data Sources
  - <a href="https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-wildland-fire-locations-full-history/about" target="_blank">Fire</a>
  - <a href="https://smoosavi.org/datasets/lstw" target="_blank">Weather</a>
  - <a href="https://droughtmonitor.unl.edu/CurrentMap.aspx" target="_blank">Drought</a>
  - <a href="https://www.icip.iastate.edu/tables/population/states-estimates" target="_blank">Population</a>
  - <a href="https://www.icip.iastate.edu/tables/population/states-estimates" target="_blank">Population</a>
</br>

</br>
## Conclusion 
We are able to predict fire class far more effectively then the baseline. The factors that seem to have the most impact on fire class are  . 
Forest services, state and local governments, and concerned citizens can use our model to assess whether they are at risk for a severe fire using our streamlit app. They can then use the results to prepare knowing that they could be dealing with a major fire.

 

