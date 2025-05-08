import json

class Item:
    def __init__(self, name, item_type, effect=None, amount=None, credit=None, description=None):
        self.name = name
        self.item_type = item_type # Ensure this matches the attribute name used elsewhere if any
        self.effect = effect if effect else {"type": "none", "description": "No special effect."}
        self.amount = amount if amount is not None else 1 # Default amount for non-stacking or loot
        self.credit = credit
        self.description = description if description else "An item of interest."

    def __repr__(self):
        return (f"Item(name='{self.name}', type='{self.item_type}', effect='{self.effect.get('type', 'N/A')}', "
                f"amount={self.amount}, description='{self.description}')")

class Consumable(Item):
    def __init__(self, name, effect, amount, credit, description=""):
        super().__init__(name, "consumable", effect, amount, credit, description)

    def use(self, player):
        if self.effect and self.effect.get('type') == 'restore hp':
            print(f"{player.name} uses {self.name}. {self.effect.get('description', 'It has a healing effect.')}")
            player.health += self.amount
            if player.health > player.max_health:
                player.health = player.max_health
            print(f"{player.name} now has {player.health}/{player.max_health} HP.")

            return True # Indicates successful use
        print(f"{self.name} cannot be used at this time or has no defined effect for {player.name}.")
        return False

class LootItem(Item):
    def __init__(self, name, credit, description=""):
        super().__init__(name, "loot", effect={"type": "none", "description": "A valuable item."}, amount=1, credit=credit, description=description)

def load_items(filepath="items.json"): # Added filepath parameter
    """Loads items from a JSON file."""
    items_data = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item_name_key, item_details in data.items():
                item_type = item_details.get("type", "loot") # Default to loot if type not specified
                if item_type == "consumable":
                    item = Consumable(
                        name=item_details.get("name", item_name_key),
                        effect=item_details.get("effect"),
                        amount=item_details.get("amount"),
                        credit=item_details.get("credit"),
                        description=item_details.get("description", "")
                    )
                    items_data[item_name_key] = item
                elif item_type == "loot":
                    item = LootItem(
                        name=item_details.get("name", item_name_key),
                        credit=item_details.get("credit"),
                        description=item_details.get("description", "")
                    )
                    items_data[item_name_key] = item
                else: # Generic item for other types
                    item = Item(
                        name=item_details.get("name", item_name_key),
                        item_type=item_type,
                        effect=item_details.get("effect"),
                        amount=item_details.get("amount"),
                        credit=item_details.get("credit"),
                        description=item_details.get("description", "")
                    )
                    items_data[item_name_key] = item
    except FileNotFoundError:
        print(f"Error: Items file '{filepath}' not found. No items loaded.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'. Invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred while loading items: {e}")
    return items_data

