library('readxl')
library(dplyr)
library(ggplot2)
library(lattice)
library(R330)
library(MASS)

#Bus Stations(Explanatory variable)
busstop = read_excel('busstop_all_merge.xlsx')
table(busstop$sido == '경기도')
busstop = filter(busstop, sido == '서울특별시')
nrow(busstop)
# [1] 11004
busstop = busstop[-1:-6]
busstop
busstop = busstop[c(-1)]
busstop

busstop_gu = busstop %>% group_by(gu, dong) %>% summarise(count = n())
busstop_gu

#gu name with number of Bus Station
busstop_gu = as.data.frame(busstop_gu)
class(busstop_gu)
# [1] "data.frame"

#####################################################################
#####################################################################
#####################################################################

#living population(Explanatory variable)
living_pop = read.csv('living_people_monthly_dong_2018.csv')
living_pop
living_pop$sido != '서울특별시'
# logical(0)

gu_living_pop = dplyr::select(living_pop, gu,dong, X1:X12)

# gu_living_pop = gu_living_pop %>% group_by(gu, dong) %>% summarise( Jan = sum(X1), Feb = sum(X2), Mar = sum(X3), Apr = sum(X4), May = sum(X5), Jun = sum(X6), Jul = sum(X7), Aug = sum(X8), Sept = sum(X9), Oct = sum(X10), Nov = sum(X11), Dec = sum(X11))

gu_name = gu_living_pop$gu
dong_name = gu_living_pop$dong

gu_living_pop = as.data.frame(gu_living_pop)
colnames(gu_living_pop) = c('gu','dong','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')
gu_living_pop

month = gu_living_pop[c('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')]
gu_living_pop = as.data.frame(rowSums(month))
gu_living_pop

gu_living_pop = cbind(gu_name, dong_name, gu_living_pop)
gu_living_pop

#####################################################################
#####################################################################
#####################################################################

#pop_dong_age_2018(explnatory Variable)
pop_dong_age = read.csv('pop_dong_age_2018.csv')
pop_dong_age = pop_dong_age[-1]
pop_dong_age$children_fewer14 = as.numeric(pop_dong_age$children_fewer14)
pop_dong_age$older_more65 = as.numeric(pop_dong_age$older_more65)
pop_dong_age = pop_dong_age[order(pop_dong_age$gu, pop_dong_age$dong),]
pop_dong_age
#####################################################################
#####################################################################
#####################################################################

#visitor_facility(explanatory variable)
visitor_facility = read.csv('jibhak_long_lat_address.csv')
visitor_facility = visitor_facility[c(-1,-2,-4,-5,-6,-7,-8,-9,-10)]
visitor_facility = visitor_facility[c(-2,-3,-4)]
colnames(visitor_facility) = c('industry','gu','dong')
visitor_facility = visitor_facility %>% group_by(gu, dong) %>% summarise( numOffacility = n())
visitor_facility = as.data.frame(visitor_facility)
visitor_facility

#####################################################################
#####################################################################
#####################################################################

#Cross Roads(Response Variable)
cross_roads = read_excel('cross_Analysis_dong.xlsx')
table(cross_roads$sido == '경기도')
seoul_crossroads = filter(cross_roads, sido == '서울특별시')
seoul_crossroads
gu_crossroads = seoul_crossroads[-1]
gu_crossroads = as.data.frame(gu_crossroads)
gu_crossroads
class(gu_crossroads)

#####################################################################
#####################################################################
#####################################################################

#dataframe for Analysis
nrow(gu_crossroads)
# [1] 424
nrow(gu_living_pop)
# [1] 424
nrow(busstop_gu)
# [1] 424
nrow(pop_dong_age)
# [1] 424
nrow(visitor_facility)
# [1] 424

df = cbind(gu_crossroads, gu_living_pop, busstop_gu, pop_dong_age, visitor_facility)
df
colnames(df) = c('gu','dong','numOfcross',
                 'gu1','dong1','numOfpop',
                 'gu2','dong2,','numOfbus',
                 'gu3','dong3','total','children_fewer14','older_more65',
                 'gu4','dong4','numOffacility')
df
df = df[c(-4,-5,-7,-8, -10, -11, -12, -15, -16)]
row.names(df) = 1:nrow(df)
df
str(df)

#####################################################################
#####################################################################
#####################################################################
#usage of variables#

#number of crossroads is response
#gu = explanatory variable(categorical)
#number of living people is explanatory variable(numeric)
#number of bus station is explanatory variable(numeric)
#number of older and young people is explanatory variable(numeric)
#number of visitor facility is explanatroy variable(numeric)

#####################################################################
#####################################################################
#####################################################################
#plotting

#1.plot(number of crossroads ~ gu)
#there seems a mean difference in number of crossroads between GUs
fill_col = '#4271AE'
line_col = '#1F3552'
ggplot(data = df, aes(x = gu, y = numOfcross)) + 
  geom_boxplot(alpha = 0.7, fill = fill_col, colour = line_col) +
  geom_jitter(alpha=0.3, color='tomato') + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

#2.plot(number of crossroads ~ numOfpop) not confounding factor included
#there seems an increase of mean number of crossroads 
fill_col1 = 'turquoise2'
line_col1 = 'cyan'
ggplot(data = df, aes(x = numOfpop, y = numOfcross)) + 
  geom_line(color = line_col1) + 
  geom_area(fill = fill_col1, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of population') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
       panel.background = element_rect(fill = '#444B5A'),
       panel.grid.minor = element_line(color = '#4d5566'),
       panel.grid.major = element_line(color = '#586174'),
       plot.title = element_text(size = 15),
       axis.title = element_text(size=13, color = '#555555'),
       axis.title.y = element_text(vjust = 1, angle = 0),
       axis.title.x = element_text(hjust = 0))

#3.plot(number of crossroads ~ numOfbus) not confounding factor included
#there seems an increase of mean number of crossroads 
fill_col2 = 'sienna1'
line_col2 = 'sienna1'
ggplot(data = df, aes(x = numOfbus, y = numOfcross)) + 
  geom_line(color = line_col2) + 
  geom_area(fill = fill_col2, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of bus station') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0))

#4.plot(number of crossroads ~ children_fewer14) not confounding factor included
#there seems an increase of mean number of crossroads 
fill_col3 = 'green1'
line_col3 = 'green1'
ggplot(data = df, aes(x = children_fewer14, y = numOfcross)) + 
  geom_line(color = line_col3) + 
  geom_area(fill = fill_col3, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of children under 14') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 

#5.plot(number of crossroads ~ older_more65) not confounding factor included
#there seems an increase of mean number of crossroads
fill_col4 = 'lightyellow1'
line_col4 = 'lightyellow1'
ggplot(data = df, aes(x = older_more65, y = numOfcross)) + 
  geom_line(color = line_col4) + 
  geom_area(fill = fill_col4, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of people aged more than 65') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 

#5_1.plot(number of crossroads ~ numOffacility) not confounding factor included
#there seems an increase of mean number of crossroads
fill_col4_1 = 'deeppink1'
line_col4_1 = 'deeppink1'
ggplot(data = df, aes(x = numOffacility, y = numOfcross)) + 
  geom_line(color = line_col4) + 
  geom_area(fill = fill_col4_1, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of visitor facility') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 

#6. plot considering confounding factor
# interaction : Gu*numOfpop
ggplot(data = df, aes(x = numOfpop, y = numOfcross)) +
  geom_point(aes(colour = factor(gu))) + 
  geom_smooth(aes(group = gu, colour = gu), method = 'lm', se = F) +
  labs(title = 'number of crossroads has increased with an increase of number of population conditioned on gu') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 
coplot(numOfcross ~ numOfpop|gu, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))

#7. plot considering confounding factor
# interaction : Gu*numOfbus
ggplot(data = df, aes(x = numOfbus, y = numOfcross)) +
  geom_point(aes(colour = factor(gu))) + 
  geom_smooth(aes(group = gu, colour = gu), method = 'lm', se = F) +
  labs(title = 'difference in mean number of crossroads according to an increase of number of bus conditioned on gu') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 
coplot(numOfcross ~ numOfbus|gu, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))

#8. plot considering confounding factor
# interaction : Gu*children_fewer14
ggplot(data = df, aes(x = children_fewer14, y = numOfcross)) +
  geom_point(aes(colour = factor(gu))) + 
  geom_smooth(aes(group = gu, colour = gu), method = 'lm', se = F) +
  labs(title = 'difference in mean number of crossroads according to an increase of number of children_fewer14 conditioned on gu') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 
coplot(numOfcross ~ children_fewer14|gu, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))


#9. plot considering confounding factor
# interaction : Gu*older_more65
ggplot(data = df, aes(x = older_more65, y = numOfcross)) +
  geom_point(aes(colour = factor(gu))) + 
  geom_smooth(aes(group = gu, colour = gu), method = 'lm', se = F) +
  labs(title = 'difference in mean number of crossroads according to an increase of number of bus conditioned on gu') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0)) 
coplot(numOfcross ~ older_more65|gu, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))

#10. plot considering confounding factor
# interaction : Gu*numOfpop*numOfbus
cloud(numOfcross ~ numOfpop * numOfbus, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfpop|gu*numOfbus, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#11. plot considering confounding factor
# interaction : Gu*numOfpop*children_fewer14
cloud(numOfcross ~ numOfpop * children_fewer14, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfpop|gu*children_fewer14, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))

#12. plot considering confounding factor
# interaction : Gu*numOfpop*older_more65
cloud(numOfcross ~ numOfpop * older_more65, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfpop|gu*older_more65, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#13. plot considering confounding factor
# interaction : Gu*numOfbus*older_more65
cloud(numOfcross ~ numOfbus * older_more65, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfbus|gu*older_more65, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#14. plot considering confounding factor
# interaction : Gu*numOfbus*children_fewer14
cloud(numOfcross ~ numOfbus * children_fewer14, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfbus|gu*children_fewer14, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#15. plot considering confounding factor
# interaction : Gu*older_more65*children_fewer14
cloud(numOfcross ~ children_fewer14 * older_more65, group = gu, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ children_fewer14|gu*older_more65, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#16. plot considering confounding factor
# interaction : numOfpop*children_fewer14*older_more65
cloud(numOfcross ~ numOfpop * older_more65, group = children_fewer14, pch='.', cex = 3 ,data=df)
coplot(numOfcross ~ numOfpop|children_fewer14*older_more65, data = df, panel = panel.smooth, 
       col = 'cyan', bg = '#444B5A', pch = 22, bar.bg = c(num='green', fac='light blue'))
dev.off()

#####################################################################
#####################################################################
#####################################################################
#model selection

#start with full model
crossroad.lm = lm(numOfcross ~ gu*numOfpop*numOfbus*children_fewer14*older_more65*numOffacility, data = df)
anova(crossroad.lm) 

#variable selection motheod
#stepwise method
null.lm = lm(numOfcross ~ 1, data = df)
step(null.lm, scope=formula(crossroad.lm),
     direction = 'both')

#new model acquired from the stepwise method
step.crossroad.lm = lm(numOfcross ~ numOfpop + numOfbus + gu + older_more65 + 
                         numOffacility + numOfpop:gu + numOfbus:gu + numOfbus:older_more65 + 
                         numOfpop:older_more65 + numOfpop:numOfbus + numOfpop:numOfbus:gu, 
                       data = df)

anova(step.crossroad.lm)

#####################################################################
#####################################################################
#####################################################################
#data and model check 
plot(step.crossroad.lm, which = c(1:5))

#data check
#1.outliers : 125, 204
#2.high leverage points : 125
#3.influential points(outliers + high leverage points) : 125, 124, 204
#4.multicollinearity

df[124,]
# gu    dong numOfcross numOfpop numOfbus children_fewer14 older_more65
# 124 구로구 오류2동        230 465937.9       70              366          399
df[125,]
# gu   dong numOfcross numOfpop numOfbus children_fewer14 older_more65
# 125 금천구 가산동        241  1217754       91               12           79
df[204,]
# gu   dong numOfcross numOfpop numOfbus children_fewer14 older_more65
# 204 마포구 서교동        173  1481256       71               68          206

new.crossroad.lm = lm(numOfcross ~ numOfpop + numOfbus + gu + older_more65 + 
                        numOffacility + numOfpop:gu + numOfbus:gu + numOfbus:older_more65 + 
                        numOfpop:older_more65 + numOfpop:numOfbus + numOfpop:numOfbus:gu, data=df[-c(124,125,204),])

plot(new.crossroad.lm, which = c(1:5))

#VIF check 
df
only_covariates = df[,-c(1,2,3)]
only_covariates
VIF = diag(solve(cor(only_covariates)))
VIF
# numOfpop         numOfbus children_fewer14     older_more65    numOffacility 
# 2.479635         1.516257         1.048995         1.204487         2.256565 

#find more than 10 indicating multicolliearity problems
table(VIF < 10)
# TRUE 
# 5 

#data re-check
#1.outliers : ok
#2.high leverage points : bit left but seems ok
#3.influential points(outliers + high leverage points) : ok
#4.multicollinearity is ok

#model check 
#1.linearity is ok
#2.normality is ok (slight right skewness)
#3.EOV is not ok (funnel effect exists)

plot(new.crossroad.lm, which = c(1:5))

boxcox(numOfcross ~ numOfpop + numOfbus + gu + older_more65 + 
         numOffacility + numOfpop:gu + numOfbus:gu + numOfbus:older_more65 + 
         numOfpop:older_more65 + numOfpop:numOfbus + numOfpop:numOfbus:gu, data=df[-c(124,125,204),])

transform = boxcox(numOfcross ~ numOfpop + numOfbus + gu + older_more65 + 
                     numOffacility + numOfpop:gu + numOfbus:gu + numOfbus:older_more65 + 
                     numOfpop:older_more65 + numOfpop:numOfbus + numOfpop:numOfbus:gu, data=df[-c(124,125,204),])

#fixing funnel effect causing non-constant variance
use_transformation = transform$x[which.max(transform$y)]
use_transformation
# [1] 0.5858586

real.crossroad.lm = lm((numOfcross)^(use_transformation) ~ numOfpop + numOfbus + gu + older_more65 + 
                         numOffacility + numOfpop:gu + numOfbus:gu + numOfbus:older_more65 + 
                         numOfpop:older_more65 + numOfpop:numOfbus + numOfpop:numOfbus:gu, data=df[-c(124,125,204),])

plot(real.crossroad.lm, which = c(1:5))
#model check 
#1.linearity is ok
#2.normality is ok (slight right skewness)
#3.EOV is ok

anova(real.crossroad.lm)
summary(real.crossroad.lm)


#####################################################################
#####################################################################
#####################################################################
# y = numOfpop

fill_col1 = 'turquoise2'
line_col1 = 'cyan'
ggplot(data = df, aes(x = older_more65, y = numOfpop)) + 
  geom_line(color = line_col1) + 
  geom_area(fill = fill_col1, alpha = 0.1) +
  labs(title = 'number of crossroads has increased with an increase of number of population') +
  theme(text = element_text(family = 'Gill Sans', color = '#444444'),
        panel.background = element_rect(fill = '#444B5A'),
        panel.grid.minor = element_line(color = '#4d5566'),
        panel.grid.major = element_line(color = '#586174'),
        plot.title = element_text(size = 15),
        axis.title = element_text(size=13, color = '#555555'),
        axis.title.y = element_text(vjust = 1, angle = 0),
        axis.title.x = element_text(hjust = 0))

aaa.lm = lm(numOfpop ~ gu*numOfcross*numOfbus*children_fewer14*older_more65*numOffacility, data = df)
anova(aaa.lm) 

null.lm = lm(numOfpop ~ 1, data = df)
step(null.lm, scope=formula(aaa.lm),
     direction = 'both')

bbb.lm = lm(numOfpop ~ numOfcross + numOffacility + gu + children_fewer14 + 
              numOfbus + numOfcross:gu + numOfcross:numOffacility + numOfcross:children_fewer14 + 
              numOfcross:numOfbus + children_fewer14:numOfbus + numOffacility:children_fewer14 + 
              numOfcross:children_fewer14:numOfbus + numOfcross:numOffacility:children_fewer14, 
            data = df)

anova(bbb.lm)

plot(bbb.lm, which = c(1:5))

#VIF check 
df
only_covariates = df[,-c(1,2,4)]
only_covariates
VIF = diag(solve(cor(only_covariates)))
VIF
# numOfcross         numOfbus children_fewer14     older_more65    numOffacility 
# 1.868906         1.710679         1.055795         1.214130         1.384028 


boxcox(numOfpop ~ numOfcross + numOffacility + gu + children_fewer14 + 
         numOfbus + numOfcross:gu + numOfcross:numOffacility + numOfcross:children_fewer14 + 
         numOfcross:numOfbus + children_fewer14:numOfbus + numOffacility:children_fewer14 + 
         numOfcross:children_fewer14:numOfbus + numOfcross:numOffacility:children_fewer14, data=df)

transform = boxcox(numOfpop ~ numOfcross + numOffacility + gu + children_fewer14 + 
                     numOfbus + numOfcross:gu + numOfcross:numOffacility + numOfcross:children_fewer14 + 
                     numOfcross:numOfbus + children_fewer14:numOfbus + numOffacility:children_fewer14 + 
                     numOfcross:children_fewer14:numOfbus + numOfcross:numOffacility:children_fewer14, data=df)

#fixing funnel effect causing non-constant variance
use_transformation = transform$x[which.max(transform$y)]
use_transformation
# [1] 0.2222222

ccc.lm = lm((numOfpop)^(use_transformation) ~ numOfcross + numOffacility + gu + children_fewer14 + 
              numOfbus + numOfcross:gu + numOfcross:numOffacility + numOfcross:children_fewer14 + 
              numOfcross:numOfbus + children_fewer14:numOfbus + numOffacility:children_fewer14 + 
              numOfcross:children_fewer14:numOfbus + numOfcross:numOffacility:children_fewer14, data=df)

plot(ccc.lm, which = c(1:5))

anova(ccc.lm)
summary(ccc.lm)
