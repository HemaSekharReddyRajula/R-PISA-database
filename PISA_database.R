####################Data base for PISA 2009 (Maths, Reading and Science) & 2012 (Maths, Reading and Science)#########################
library(SAScii)
library(reshape2)
library(tidyr)
library(dplyr)
library(RSQLite)
library(dbplyr)
library(plyr)

#Sample cognitive item response data from the text file of 2012 PISA data.

#Input file for 2009 data. Note: Run the below 2 lines of code (13 & 14 lines of code) for 2009 data. 
zipF <- "INT_COG09_S_DEC11_1000.zip"
sampledata <- "INT_COG09_S_DEC11_1000.txt"

#Input file for 2012 data. Note: Run the below 2 lines of code (17 & 18 lines of code) for 2012 data. 
#zipF <- "INT_COG12_S_DEC03_1000.zip"
#sampledata <- unzip(zipF)

#Scored cognitive item response SAS file

#Input file for 2009 data. Note: Run the below 3 lines of code (23, 24 & 25 lines of code) for 2009 data.
zipF1 <- "PISA2009_SAS_scored_cognitive_item.zip"
sampledata1 <- unzip(zipF1)
dict_scored <- parse.SAScii(sas_ri = sampledata1)

#Input file for 2012 data. Note: Run the below 3 lines of code (28, 29 & 30 lines of code) for 2012 data.
#zipF1 <- "PISA2012_SAS_scored_cognitive_item.zip"
#sampledata1 <- unzip(zipF1)
#dict_scored <- parse.SAScii(sas_ri = sampledata1)

#data_scored has all the items with respectibve scores and country, student id, bookid etc  
data_scored_allsubjects = readr::read_fwf(file  = sampledata, col_positions = readr::fwf_widths(dict_scored$width, col_names = dict_scored$varname))


#Adding NA to the scores of 7 (Not available) and 8 (Not reached).
data_scored_allsubjects$BOOKID = sprintf('B%02d', data_scored_allsubjects$BOOKID)
data_scored_allsubjects[data_scored_allsubjects==7] = NA
data_scored_allsubjects[data_scored_allsubjects==8] = NA

########################################Maths###################################################################
#Prepare the list of items belongs to the each booklet of maths.

#Note: Run the below line of code for 2009 maths data input.
Maths = read.csv("BookletM_2009.csv", header = TRUE, sep = ",")

#Note: Run the below line of code for 2012 maths data input.
#Maths = read.csv("BookletM_2012.csv", header = TRUE, sep = ",")

subject = 'MATHS'
cluster_list_Maths = list()
for (book in unique(Maths$BOOKID)) {
  cluster_list_Maths[[book]] = unique(Maths[Maths[, 'BOOKID'] == book & Maths[, 'MATHS'] == subject,'Items'])
}

#Maths_database has the country, student id, bookid, items and respective scores.
Maths_datalist = list()
for (i in seq_along(cluster_list_Maths)){
  booklet_row = (names(cluster_list_Maths)[i])
  items = as.character((cluster_list_Maths)[[i]])
  df_wide = (data_scored_allsubjects[data_scored_allsubjects[, 'BOOKID'] == booklet_row, c('CNT', 'STIDSTD', 'BOOKID', items)])
  Maths_datalist[[booklet_row]] = df_wide %>% gather(Items, Score, items)
}  
Maths_database = do.call(rbind, Maths_datalist)
####################################################Reading#######################################################
#Prepare the list of items belongs to the each booklet of reading.

#Note: Run the below line of code for 2009 reading data input.
Reading = read.csv("BookletR_2009.csv", header = TRUE, sep = ",")

#Note: Run the below line of code for 2012 reading data input.
#Reading = read.csv("BookletR_2012.csv", header = TRUE, sep = ",")

subject = 'READING'
cluster_list_Reading = list()
for (book in unique(Reading$BOOKID)) {
  cluster_list_Reading[[book]] = unique(Reading[Reading[, 'BOOKID'] == book & Reading[, 'READING'] == subject,'Items'])
}

#Reading_database has the country, student id, bookid, items and respective scores.
Reading_datalist = list()
for (i in seq_along(cluster_list_Reading)){
  booklet_row = (names(cluster_list_Reading)[i])
  items = as.character((cluster_list_Reading)[[i]])
  df_wide = (data_scored_allsubjects[data_scored_allsubjects[, 'BOOKID'] == booklet_row, c('CNT', 'STIDSTD', 'BOOKID', items)])
  Reading_datalist[[booklet_row]] = df_wide %>% gather(Items, Score, items)
}  
Reading_database = do.call(rbind, Reading_datalist)
#######################################################Science####################################################
#Prepare the list of items belongs to the each booklet of science.

#Note: Run the below line of code for 2009 science data input.
Science = read.csv("BookletS_2009.csv", header = TRUE, sep = ",")

#Note: Run the below line of code for 2009 science data input.
#Science = read.csv("BookletS_2012.csv", header = TRUE, sep = ",")

subject = 'SCIENCE'
cluster_list_Science = list()
for (book in unique(Science$BOOKID)) {
  cluster_list_Science[[book]] = unique(Science[Science[, 'BOOKID'] == book & Science[, 'SCIENCE'] == subject,'Items'])
}

#Science_database has the country, student id, bookid, items and respective scores.
Science_datalist = list()
for (i in seq_along(cluster_list_Science)){
  booklet_row = (names(cluster_list_Science)[i])
  items = as.character((cluster_list_Science)[[i]])
  df_wide = (data_scored_allsubjects[data_scored_allsubjects[, 'BOOKID'] == booklet_row, c('CNT', 'STIDSTD', 'BOOKID', items)])
  Science_datalist[[booklet_row]] = df_wide %>% gather(Items, Score, items)
}  
Science_database = do.call(rbind, Science_datalist)
################################################################################################################

