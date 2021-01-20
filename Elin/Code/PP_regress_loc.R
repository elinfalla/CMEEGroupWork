#!/usr/bin/env R

#packages
require(dplyr)
require(readr)

# read in dataset
MyDF <- as.data.frame(read.csv("../Data/EcolArchives-E089-51-D1.csv"))

# create function that does a linear regression, and outputs regression values into a dataframe
create_lm_model <- function(data) {
  
  model <- lm(log10(Predator.mass) ~ log10(Prey.mass), data = data)
  anova.res <- anova(model)
  model.res <- summary(model)
  
  outputDF <- data.frame(intercept = model.res$coefficients[1],
                         slope = model.res$coefficients[2],
                         r_squared = model.res$r.squared,
                         F_val = anova.res$`F value`[1],
                         P_val = anova.res$`Pr(>F)`[1])
  
  return(outputDF)
}


#initialise dataframe
model_result <- data.frame()

#use piping to group data and perform create_lm_model() on it
model_result <-
  MyDF %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
  group_modify(~ create_lm_model(.))

#write model_result to csv
write_csv(model_result, "../Results/PP_Regress_loc_Results.csv")
