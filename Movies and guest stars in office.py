#First look for CSV file Office
# start to have dataframe from csv of kaggle
import pandas as pd                                      #import pandas library as pd
office_df = pd.read_csv("E:\Data scientists\Movies and guest stars in office\\office_episodes.csv") #import CSV file from datasets of datacamp
print(office_df)

# A color scheme for the scatter  plot
colors= []                                 # empty list will indicate the color according the rating
for ind, row in office_df.iterrows():      # using the looping (for and if)to full color list
    if row["scaled_ratings"] < .25 :
        colors.append("red")
    elif row["scaled_ratings"] < .50 :
        colors.append("orange")
    elif row["scaled_ratings"] < .75 :
        colors.append("lightgreen")
    else:
        colors.append("darkgreen")        
print (colors)

#To calculate size of scatter 25 or 250
sizes= []                              #empty list for variable size of scatter plot
for ind, row in office_df.iterrows():  #for and if loop and filter to calculate witch true or false
    if row['has_guests'] == True:
        sizes.append(250)
    else:
        sizes.append(25)
print(sizes)

# to consider our lists as part of the DataFrame
office_df['colors'] = colors
office_df['sizes'] = sizes
office_df.info()

# Split data into guest and non_guest DataFrames
non_guest_df = office_df[office_df['has_guests'] == False]
guest_df = office_df[office_df['has_guests'] == True]
non_guest_df.info
guest_df.info

#import matplotlib as plt to have
import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = [11, 7]
fig= plt.figure(figsize=(11,7))
plt.style.use("fivethirtyeight")
fig = plt.figure()

# Create two scatter plots for guest and non-guests
plt.scatter(x=guest_df.episode_number,y=guest_df.viewership_mil, 
            c= guest_df["colors"],      #plt scatter with argu ment selected in task 1
            s= guest_df["sizes"],
            marker= '*')
plt.scatter(x= non_guest_df.episode_number,y= non_guest_df.viewership_mil, 
            c= non_guest_df["colors"],  #plt scatter with argu ment selected in task 1
            s= non_guest_df["sizes"])

plt.ylabel("viewership(millions)")
plt.xlabel("Episode Number")
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.show()

#top_star= guest_df[guest_df["viewership_mil"] > 20]
print(office_df[office_df['viewership_mil'] == office_df['viewership_mil'].max()]['guest_stars'])
top_star = 'Cloris Leachman'