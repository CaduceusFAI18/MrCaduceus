# MrCaduceus Report

The datasets are located here: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2013

## Report Outline
  * Introduction
    * Problem
    * Solution
  * Data
    * Description
    * Wrangling
        * Merge different inputs (demography, medication, labs, diet) together, grouped into a patient profile (by ID)
        * Remove columns that has more than 35% is nan
        * Remove rows that has more than 50% is nan
        * Replace nan with mean for int column and 'no category' for category column
        * One hot encode categorical columns
    * Exploring
        * Pictures in slides
        * Investigating the bias in the training data of Sensitive Variables: Age, Gender, Disease Distribution
    * Sensitive Variables
  * Law Stuff about why we aren't the baddies
  * Model
    * Initial Models
      * Model 1:
        * Random Forest with parameters of max_depth and number of estimators
            * Multi labels (for all disease)
            * Single label (for the 7 most common disease)
        * Using cross validation
        * Performance (slide)
      * Model 2:
          * KNN with parameters of number of neighbors
              * Multi labels (for all disease)
              * Single label (for the 7 most common disease)
          * Using cross validation
          * Performance (slide)
      * Model 3
        * Etc Etc
    * "Fairness Aware" Models
        * Removing Sensitive variable age, gender and see the performance:
            * No performance drop (in slide)
            * Bias is actually decrease (in slide) (comparing with the training data bias)
        * Remove all the sensitive variable:
            * Same result (in slide)
        * Improving the model:
            * Feature selection:   
                * Coefficient
                * Pre-train model feature selection
        * Not shown:
            * We have a generic score for bias by doing a twin test for each sensitive variable. Binary for if a model is bias on this variable or not. Then average out of all sensitive variables. This is a pretty bad formula since it's assuming each variable is equally importance, and binary doesn't really make sense. However, this could be use as to combine to our loss function (combining both model accuracy and reduce bias)
  * Conclusion
    * By removing the sensitive variables, it doesn't actually reduce our model accuracy or create bias. This might be because we have a lot of features
    * Feature selection is crucial
    * A lot of interesting points regarding the idea:
        * What if the model is not evil but the user is evil and try to take advantage of the model to reduce their tax.
        * How to make this more as a suggestive tool
    * We haven't integrated the price of each disease to get the final pricing model (tax bin)
