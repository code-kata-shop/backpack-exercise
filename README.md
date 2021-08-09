# Backpack Specifications

We're making a magical backpack. It has some simple features:

- Keeps up to 10 items by default; can change this
- Has a way to add or remove items
- It expects the items to come in are just the labels (strings), but it treats casing respectfully and doesn't assume "Food" and "food" are the same thing
- Show all items in the bag alphabetically
- Check for distinct counts for the same item (`['ax', 'ax']` counts as `2 ax`, but `['ax', 'Ax']`  counts as `1 ax, 1 Ax` )
- Has a way to check to see what the most popular item is
- If you overfill the bag, it drops the item you put in first. That is, if the bag `size` is 1, it will only contain the last item you put in.

There are a set of tests that should be made to pass that implement all these features.

Use whatever features you like baked into whatever version of Python you want. There shouldn't be a need to install any outside packages.