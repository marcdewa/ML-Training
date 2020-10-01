
dataset = read.csv('50_Startups.csv')

dataset$State = factor(dataset$State,
                       levels=c('California','Florida','New York'),
                       labels = c(1,2,3))

library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)

regressor = lm(formula = Profit ~ + R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
regressor = lm(formula = Profit ~ + R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
regressor = lm(formula = Profit ~ + R.D.Spend + Marketing.Spend,
               data = dataset)
regressor = lm(formula = Profit ~ + R.D.Spend,
               data = dataset)

y_pred = predict(regressor, newdata = test_set)
