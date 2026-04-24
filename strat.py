from sklearn.model_selection import StratifiedShuffleSplit

# Suppose 'income_cat' is a column you created to group houses by price range
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing_data, housing_data["income_cat"]):
    strat_train_set = housing_data.loc[train_index]
    strat_test_set = housing_data.loc[test_index]
