# world_unemployment_dataviz
Analysis and Visualization of the World Unemployment Rates dataset denoting the worldwide unemployment rates from the years 1991 to 2021.  
Tools Used: Tableau Public for Visualization and Python Pandas for Data-Reshaping.

# Dataset
The source dataset used here can be found : https://www.kaggle.com/datasets/pantanjali/unemployment-dataset  
It has also been added under the Data folder in the repository as "unemployment_analysis.csv".

# Data Description
The original dataset contains the columns Country Names, Country Codes and years 1991 to 2021.  
The dataset contains data regarding the unemployment rates of countries and regions.

# Data-Reshaping
The data was originally in the Wide Format, which has been reshaped to the Long Format using Python pandas, for the ease of visualization with Tableau.  
Both the original dataset "unemployment_analysis.csv" and the reshaped dataset "reshaped_unemployment_data.csv" can be found under the Data folder.  
The reshaped dataset contains the columns Country Name, Country Code, Year and Unemployment Rate.  
The python file is "reshape_unemployment_data.py".

# Tableau Dashboard
The Dashboard is published on Tableau Public under the link : https://public.tableau.com/views/WorldUnemploymentDataViz/Dashboard2?:language=en-US&:display_count=n&:origin=viz_share_link

The individual viz's can be accessed and interacted with in the tabs of the above dashboard link.  
The dashboard contains 2 filters, country name and year through which the unemployment rates can be visualized.  
The look and feel of the dashboard is shared as below.  
Images have also been uploaded in the repository.

<div class='tableauPlaceholder' id='viz1694975854395' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldUnemploymentDataViz&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldUnemploymentDataViz&#47;Dashboard2' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldUnemploymentDataViz&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>  


<div class='tableauPlaceholder' id='viz1694976055947' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K2&#47;K24R68853&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;K24R68853' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K2&#47;K24R68853&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>  

The individual components of the dashboard are as follows...

## Viz 1 : World Unemployment Rates by Year
Shows unemployment rates of all the countries in the world for a particular year that can be selected from the respective filter.
<div class='tableauPlaceholder' id='viz1694976217727' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YD&#47;YD6R2NKCX&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;YD6R2NKCX' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YD&#47;YD6R2NKCX&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>

## Viz 2 : Unemployment Trends by Country in All Years
Shows unemployment rates of a country over all the years from 1991 to 2021. The country name can be selected from the respective filter.
<div class='tableauPlaceholder' id='viz1694976321202' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;R7&#47;R7WDC5QM7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;R7WDC5QM7' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;R7&#47;R7WDC5QM7&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>

## Viz 3 : Unemployment Rates by Country and Year
Shows unemployment rate of a country in a particular year. Both the filters impact this viz.
<div class='tableauPlaceholder' id='viz1694976516509' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;N7&#47;N7524WXWP&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;N7524WXWP' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;N7&#47;N7524WXWP&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>

## Viz 4 : Unemployment Rates by Country Condition
Compares the unemployment rates of country categories in a particular year.
<div class='tableauPlaceholder' id='viz1694976621459' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;ShinjiniShome&#47;world_unemployment_dataviz'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;R5&#47;R5SBRHNDR&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;R5SBRHNDR' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;R5&#47;R5SBRHNDR&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>
