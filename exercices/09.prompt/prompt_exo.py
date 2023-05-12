import sys
sys.path.extend(['.','..','/workspaces/Python-OOP-Project/exercices/06.inventory_manager',"/workspaces/Python-OOP-Project/exercices/04.class_generation", "/workspaces/Python-OOP-Project/exercices/03.class_tree"])
from inventory_manager import *
import json
from class_tree import create_tree_from_dict
from unidecode import unidecode
# import generator
from product_classes import *
from class_generation import *
import readline
#import utils
import treelib
import os


# Define the prompt_for_instance function 
# that takes a class name as a string as input
def prompt_for_instance(cls):
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [{name:input("Enter the value for {}: ".format(name))} for name in arg_names]
    # Create an instance of the class using the entered values
    for arg1 in args:
        arg = list(arg1.keys())[0]
        if "cost" in arg or "price" in arg or "quantity" in arg:
            try:
                int(arg1[arg])
            except:
                while True:
                    print(f"{arg} doit etre un entier !")
                    new_arg = input(f"Entrez la valeur pour {arg}: ")
                    try:
                        int(new_arg)
                        arg1[arg] = new_arg
                        break
                    except:
                        continue
    list_args = []
    for dict in args:
        value = list(dict.values())[0]
        list_args.append(value)



    
    return cls(*list_args)

# on cree une classe Tree qui herite de treelib.Tree
# et rajoute deux fonctionnalités supplémentaires
# get_penultimate_nodes -> recupère les avant derniers noeuds
# get_children_nodes -> recupère les noeud terminaux
class TreeExt(treelib.Tree):
    def __init__(self):
        super().__init__()
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

def sep():
    print("====================")

def main():
    inventory_manager = InventoryManager()
    # write code to read json file as dict
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open("/workspaces/Python-OOP-Project/exercices/04.class_generation/json_data.json", "rb"))

    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)    

    readline.set_completer_delims('\t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) >= 1:
            entry_name = matching_entry[0]
            #remaining_text = entry_name
            remaining_text = entry_name[len(text):]
            if remaining_text:
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(list):
        readline.set_completer(lambda text, state: auto_complete(text,list))

    while True:
        print("""
			What would you like to do? :
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			Q. Quit
		""")

        
        choice = input("Enter your choice: ")
        choice = choice.upper()
        

        if choice == "A":
            # print_list
                
            while True:
                # write code to get class tree hierachy
                # convert the tree object to TreeExt to get the new functionalities 
                # described above in TreeExt class
                class_tree = TreeExt()
                class_tree.create_node(tag="Racine", identifier="racine")
                create_tree_from_dict(class_tree,"racine",json_dict)
                # ecrire le code pour récupérer les avant dernier noeus de classe
                # (dernier niveau de catégories de produits)
                product_classes = class_tree.get_penultimate_nodes()
                dict_product = {}
                for identifier in product_classes:
                    dict_product[identifier.split(".")[-1]] = identifier

                # for node in product_classes:
                #     test_list.append(node.split(".")[-1])

                # write code to print list of product_classes
                #
                for keys in dict_product:
                    print(keys)
                set_autocomplete(list(dict_product))
                category = input("Enter the category of the product: ")
                try:
                    # Get the immediate children nodes of node 'B'
                    children_nodes = class_tree.get_children_nodes(dict_product[category])
                    dict_sub_product = {}
                    for identifier in children_nodes:
                        dict_sub_product[identifier.split(".")[-1]] = identifier
                    
                    print('-'*50)
                    for keys in dict_sub_product:
                        print(keys)
                    # write code to print list of children_nodes
                    #
                    while True:
                        set_autocomplete(list(dict_sub_product))
                        product_name = input("Enter your product choice: ")
                        try:
                            #print(f"{name} has been added to stock with a quantity of {quantity}.")

                            # write code to create a instance of classe product_name
                            product_entry = prompt_for_instance(globals()[product_name.replace(' ', '_').replace('-', '_')])
                            quantity = int(input("Enter quantity: "))
                            # write code to add product_entry and quantity in Inventory Manager
                            inventory_manager.add_product(product_entry, quantity)
                            break
                        except:
                            print("Ce nom de produit n'existe pas")
                            continue
                except:
                    print("Le nom n'est pas valide !\n")
                    continue
                break
                

        elif choice == "R":
            list_product = list(inventory_manager.list_products().keys())
            set_autocomplete(list_product)
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to restock: "))
            # write code to get product by name
            product = inventory_manager.get_product(name)
            # write code to restock product
            if inventory_manager.profit_tracker.buy_product(product, quantity):
                inventory_manager.restock_product(product, quantity)



        elif choice == "S":
            list_product = list(inventory_manager.list_products().keys())
            set_autocomplete(list_product)
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to sell: "))
            # write code to get product by name
            product = inventory_manager.get_product(name)
            # write code to sell product
            if inventory_manager.sell_product(product.name, quantity):
                inventory_manager.profit_tracker.sell_product(product, quantity)
        elif choice == "D":
            list_product = list(inventory_manager.list_products().keys())
            set_autocomplete(list_product)
            name = input("Enter the name of the product: ")
            # write code to get product
            product = inventory_manager.get_product(name)
            if product:
                inventory_manager.remove_product(product.name)
                print(f"{name} has been removed from stock.")
            else:
                print(f"{name} is not in stock.")

        elif choice == "L":
            inventory_manager.list_products()

        elif choice == "B":
            print(f"Balance: {inventory_manager.profit_tracker.balance} $")
            # supprimer la ligne suivante apres avoir ecrit cotre code
            pass
        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
