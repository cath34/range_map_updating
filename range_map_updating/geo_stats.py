
def get_obs_outside_range(range_gdf, observations_gdf):
  """
  Returns observations that are outside range

  Parameters:
    - range_gdf : GeoDataFrame of the range
    - observations_gdf : GeoDataFrame of the observations

  Output : 
    - GeoDataFrame of the observations outside range_gdf
  """

  union_range = range_gdf.union_all()   # Handles multipolygon

  inside_prior = observations_gdf.geometry.within(union_range)
  return observations_gdf.loc[~inside_prior]

def get_obs_inside_range(range_gdf, observations_gdf):
  """
  Returns observations that are inside range

  Parameters :
    - range_gdf : GeoDataFrame of the range
    - observations_gdf : GeoDataFrame of the observations

  Output :
    - GeoDataFrame of the observations inside range_gdf 
  """

  union_range = range_gdf.union_all()  # Handles multipolygon

  inside_prior = observations_gdf.geometry.within(union_range)
  return observations_gdf.loc[inside_prior]

def get_obs_in_A_not_in_B(range_a_gdf, range_b_gdf, observations_gdf):
   """
   Returns observations that are inside range_b, but outside range_a
   
   Parameters:
        - range_a_gdf : GeoDataFrame of range_a
        - range_b_gdf : GeoDataFrame of range_b
        - observations_gdf : GeoDataFrame of observations
        
    Output :
        - GeoDataFrame of the observations inside range_a, but outside range_b
   """

   union_a = range_a_gdf.union_all() # Handles multipolygon
   union_b = range_b_gdf.union_all()

   inside_a = observations_gdf.geometry.intersects(union_a)
   outside_b = ~observations_gdf.geometry.intersects(union_b)

   mask = inside_a & outside_b
   return observations_gdf.loc[mask]

def compute_distance_to_range_boundary(range_gdf, observations_gdf, column_name="distance_to_boundary", to_utm=True):
    """
    Compute Euclidean distance from each point to the boundary of a polygon range, and 
    optionally reprojects to a UTM CRS to ensure distances are in meters.

    Parameters:
        - range_gdf : GeoDataFrame of the polygon range
        - observations_gdf : GeoDataFrame of the observations  
        - column_name : Name of the column in which the function will store the computed distances
        - to_utm : Whether to convert range_gdf and observations_gdf automatically to a UTM projection in order
                   to get distances in meters (default : True)
        
    Output :
        - observations_gdf : GeoDataFrame of the observations (with a column containing the computed distances)
    """

    # Hard copy (to prevent changing the CRS of the original gdfs)
    range_gdf = range_gdf.copy()
    observations_gdf = observations_gdf.copy()

    union_range = range_gdf.union_all() # Handles multipolygon
    boundary = union_range.boundary

    if to_utm:
      utm_crs = observations_gdf.estimate_utm_crs()

      range_gdf = range_gdf.to_crs(utm_crs)
      observations_gdf = observations_gdf.to_crs(utm_crs)

    observations_gdf[column_name] = observations_gdf.geometry.distance(boundary)
    return observations_gdf