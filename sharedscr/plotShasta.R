# Load required libraries
library(dplyr)

# Define the paths to the two files
corrected_file <- "corrected/Binned-ReadLengthHistogram.csv"
pass_file <- "pass/Binned-ReadLengthHistogram.csv"

# Import the two files
corrected_data <- read.csv(corrected_file)
pass_data <- read.csv(pass_file)

# Add a label column to each dataframe
corrected_data$type <- "corrected"
pass_data$type <- "pass"

# Combine the two dataframes
combined_data <- bind_rows(corrected_data, pass_data)


#read legth 
combined_data %>% 
  ggplot(aes(x = LengthBegin+500, y = Reads, fill = type)) + 
  geom_bar(stat = 'identity', alpha = 0.4) +
  facet_grid(type ~ ., scale='free_y') + 
  labs(title = 'Read Length')
 
