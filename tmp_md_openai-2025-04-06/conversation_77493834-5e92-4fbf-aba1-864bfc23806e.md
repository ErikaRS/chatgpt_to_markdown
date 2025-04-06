# 

Created: 2023-12-30 10:30:54
Last Updated: 2024-01-05 18:16:51

### User - 2023-12-30 10:30:54

We have a bunch of leftover turkey. What can we make, preferably from our recipes?

### Assistant - 2023-12-30 10:31:26

```unknown
import pandas as pd
import zipfile
import os

# File paths
zip_file_path = '/mnt/data/recipes.zip'
csv_file_path = '/mnt/data/Common meals in the Rice Scherpelz household - Sheet1.csv'

# Unzipping the recipe file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('/mnt/data/recipes')

# List all files in the unzipped directory
recipe_files = os.listdir('/mnt/data/recipes')

# Load the CSV file
common_meals_df = pd.read_csv(csv_file_path)

# Check for recipes that might use turkey
turkey_recipes = [file for file in recipe_files if 'turkey' in file.lower()]

turkey_recipes, common_meals_df.head()
```

### Tool (python) - 2023-12-30 10:31:26

```
([],
            Dish Unnamed: 1 Unnamed: 2
 0      Biscuits     Breads        NaN
 1         Bread     Breads        NaN
 2  Cheesy bread     Breads        NaN
 3     Cornbread     Breads        NaN
 4  Garlic bread     Breads        NaN)
```

### Assistant - 2023-12-30 10:31:26

It appears that there are no specific recipes with 'turkey' in their title within your recipe collection. However, we can still find a suitable dish using leftover turkey. Let's explore the common meals in your household to see if any of them could incorporate turkey as an ingredient. 

I'll check for dishes in your common meals list that might be adaptable to use turkey.

### Assistant - 2023-12-30 10:31:26

```unknown
# Filtering the common meals for potential dishes that can use turkey
potential_dishes = common_meals_df['Dish'].str.lower().str.contains('sandwich|salad|stew|soup|casserole|pie|pasta|taco')
turkey_friendly_dishes = common_meals_df[potential_dishes]

turkey_friendly_dishes.head()
```

### Tool (python) - 2023-12-30 10:31:26

```
                            Dish Unnamed: 1 Unnamed: 2
9                      Taco bake  Casserole      Pasta
10     Turkey broccoli casserole  Casserole      Pasta
11  Winter squash and pasta bake  Casserole      Pasta
13       Chicken biscuit pot pie  Casserole        NaN
14    Chicken broccoli casserole  Casserole        NaN
```

### Assistant - 2023-12-30 10:31:26

Based on your common meals, here are some dishes that could be adapted to use leftover turkey:

1. **Taco Bake** - Originally a casserole with a pasta base, you can substitute turkey for the usual protein.
2. **Turkey Broccoli Casserole** - This dish already includes turkey, making it a perfect fit.
3. **Winter Squash and Pasta Bake** - You can add turkey to this casserole for extra protein.
4. **Chicken Biscuit Pot Pie** - Replace chicken with turkey for a twist on this classic.
5. **Chicken Broccoli Casserole** - Substitute the chicken with turkey.

These dishes offer a variety of ways to creatively use your leftover turkey in meals that are already familiar to your household. Let me know if you need the recipes for any of these dishes!

