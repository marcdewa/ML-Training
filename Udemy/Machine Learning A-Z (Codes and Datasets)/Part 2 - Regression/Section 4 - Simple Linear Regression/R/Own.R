#Importing dataset
dataset = read.csv('Salary_Data.csv')

#Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio=2/3)
training_set = subset(dataset, split==TRUE)
test_set = subset(dataset,split==FALSE)

#Simple linear regression

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

y_pred = predict(regressor, newdata = test_set)
y_pred

#install.packages('ggplot2')
library(ggplot2)

ggplot() +
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary),
             color='red') +
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor, newdata= training_set)),
            color='blue') +
  ggtitle('Salary vs Experience (Training set)')+
  xlab('Years of experience')+
  ylab('Salary')

ggplot() +
  geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary),
             color='red') +
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor, newdata= training_set)),
            color='blue') +
  ggtitle('Salary vs Experience (Test set)')+
  xlab('Years of experience')+
  ylab('Salary')