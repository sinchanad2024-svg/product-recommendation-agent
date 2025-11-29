import json

class ProductAgent:

    def __init__(self, preferences_file="preferences.json"):
        with open(preferences_file, "r") as file:
            self.data = json.load(file)

    def recommend(self, category, budget=None, min_rating=None):
        if category not in self.data:
            return ["Category not found. Try electronics, fashion, or books."]

        items = self.data[category]

        if budget:
            items = [i for i in items if i["price"] <= budget]

        if min_rating:
            items = [i for i in items if i["rating"] >= min_rating]

        if not items:
            return ["No items match your preferences. Try increasing your budget or lowering rating."]

        return items
