# predicting-item-sales-model

# Predicting Item Sales
## Using Python and Scikit-Learn 

**Author**: Austin Weinland

### Business problem:

The goal is to help the retailer by using machine learning to make predictions 
about future sales based on the data provided.


### Data:
Data Source: https://drive.google.com/file/d/1syH81TVrbBsdymLT_jl2JIf6IjPXtSQw/view
Data Dictionary:
| Variable Name | Description |
| ------------- | ----------- |
| Item_Identifier | Unique product ID |
| Item_Weight | Weight of product |
| Item_Fat_Content | Whether the product is low fat or regular |
| Item_Visibility | The percentage of total display area of all products in a store allocated to the particular product |
| Item_Type | The category to which the product belongs |
| Item_MRP | Maximum Retail Price (list price) of the product |
| Outlet_Identifier | Unique store ID |
| Outlet_Establishment_Year | The year in which store was established |
| Outlet_Size | The size of the store in terms of ground area covered |
| Outlet_Location_Type | The type of area in which the store is located |
| Outlet_Type | Whether the outlet is a grocery store or some sort of supermarket |
| Item_Outlet_Sales | Sales of the product in the particular store. This is the target variable to be predicted. |


## Methods
- Exploratory data anaylsis with visulizations to help see what our different features look like wihthin our dataset
- Dropped the Item Identifier column as it was not going to be useful with our model training
- Corrected the inconsistent values in the Item Fat Content column
- Split data for training and validation
- Tested Linear and Random Forest regression models to see which would provide a better performance
- Fine tuned models hyperparameters to improve reults relevant to the business use

## Results

The linear model appears to have underfit the training, while the Random Forest appears to be the better model,
though we do want to keep an eye out for it to be overfitting and may require additional parameters to be tuned.

#### Item Type Distribution
![Item Type Dist](https://github.com/bubbles42/predicting-item-sales-model/assets/115664524/a4c90378-bf90-4f66-872d-22b1efd11f02)

> This graph shows us how the item sales count is ditributed across the different types of items sold. We can
  see that Fruits and Vegitables and Snack Goods are our top two items sold.

#### Outlet Location Tier Distribution
![Outlet Tier Graph](https://github.com/bubbles42/predicting-item-sales-model/assets/115664524/e3c6a753-4256-401c-8c3a-ecc7ffb41f5b)

> This graph shows that most of the outlets are located in Tier 3 location types. While tier 1 locations seem
  to be the lowest location type. This could impact sales depending on the social economic status of the area.

## Model

The Random Forest Model is performing better than the Linear Regression model. When we compare the R2 score of
the test data between the Linear, Base Random Forest, and Tuned Random Forest modes the tuned version comes
back the best. 

Though it would be dependent upon what the stakeholders requirements are for the model, I would say this model
would need a little more tuning or possibly even test out some other algorithms to see if we can imporove the 
overall results of the models predictions.

## Recommendations:
![top3 coeffs](https://github.com/bubbles42/predicting-item-sales-model/assets/115664524/f28058ed-a116-4ae9-99aa-67b4a47f8a26)
> Our top 3 coefficients are:
> - Outlet_Type_Supermarket Type3
> - Outlet_Identifier_OUT027
> - Item_MRP
> All of these are showing stong positive coefficients, meaning they have a positive correlation with our target.

![top5 feat](https://github.com/bubbles42/predicting-item-sales-model/assets/115664524/d6d8d7b1-ae1a-4caf-aa0e-dcc8db3e0a95)
> Our top 5 Features (R.F.):
>  - Item_MRP
>  - Item_Visbility
>  - Outlet_Type_Supermarket Type1
>  - Item_Weight
>  - Outlet_Identifier_OUT027
>    We can see that the top 3 permutation importances can also be found within the R.F. importances. The only
>    2 that are different include:
>    - Outlet_Type_Supermarket Type3
>    - Outlet_Establishment_Year


I would recommend the Random Forest model, as it seems to be improving with the fine tuning, 
and started off at a better performace level than the linear regression model.


## Limitations & Next Steps

The next steps would be to try and find a more data and also do more tuning on the model to maximize the 
performance.


### For further information


For any additional questions, please contact **aiwikichannel@gmail.com**
