import pandas as pd

taxi_owners=pd.read_pickle("taxi_owners.p")
taxi_vehicles=pd.read_pickle("taxi_vehicles.p")

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_vehicles, on="vid")

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

ward=pd.read_pickle("ward.p")
census=pd.read_pickle("census.p")

# Merge the wards and census tables on the ward column
ward_census = ward.merge(census, on="ward")

# Print the shape of wards_census
print('ward_census table shape:', ward_census.shape)

licenses=pd.read_pickle("licenses.p")

biz_owners=pd.read_pickle("business_owners.p")

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values("account", ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head(5))

cal=pd.read_pickle("cta_calendar.p")
ridership=pd.read_pickle("cta_ridership.p")
stations=pd.read_pickle("stations.p")
zip_demo=pd.read_pickle("zip_demo.p")



# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=["year", "month", "day"])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations, on="station_id")

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == "Weekday")
                   & (ridership_cal_stations['station_name'] == "Wilson"))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on="zip") \
            			.merge(ward, on="ward")

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({'income':'median'}))

land_use=pd.read_pickle("land_use.p")
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on="ward") \
                    .merge(licenses, on="ward", suffixes=("_cen", "_lic"))
# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(["ward", "pop_2010", "vacant"],
                                   as_index=False).agg({'account':'count'})


# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant", "account", "pop_2010"],
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

movies=pd.read_pickle("movies.p")
financials=pd.read_pickle("financials.p")
# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on="id", how="left")
# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)




