# Danhong Li 
# Properties of Stars Assessment
library(tidyverse)
library(dslabs)
data(stars)
options(digits = 3)   # report 3 significant digits

mean(stars$magnitude)
sd(stars$magnitude)

stars %>%             # density plot of the magnitude
  ggplot(aes(magnitude)) +
  geom_density()


stars %>%     # Examine the distribution of star temperature
  ggplot(aes(temp)) +
  geom_density()

stars %>%     # scatter plot of the data with temperature on the x-axis and magnitude on the y-axis 
  ggplot(aes(temp, magnitude)) +
  geom_point()

stars %>%     # The brighest, highest temperature stars are in the upper left corner of the plot
              # For main sequence stars, hotter stars have higher luminosity.
  ggplot(aes(log10(temp), magnitude)) +
  geom_point() +
  scale_x_reverse() +
  scale_y_reverse()

stars %>%     # Add labels
              # The least lumninous star in the sample with a surface temperature over 5000K is van Maanen's Star
              # The Sun is a main sequence star
  ggplot(aes(log10(temp), magnitude)) +
  geom_point() +
  geom_text(aes(label = star)) +
  scale_x_reverse() +
  scale_y_reverse()

stars %>%     # The coolest stars at the right of the plot are type M
              # O star type has the highest temperature
              #  
  ggplot(aes(log10(temp), magnitude, col = type)) +
  geom_point() +
  scale_x_reverse() +
  scale_y_reverse()






