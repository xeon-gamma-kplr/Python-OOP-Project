#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 
import sys
sys.path.extend(['.','..',"/workspaces/Python-OOP-Project/exercices/05.inventory_product_entry"])

from product_classes import *
from inventory_product_entry import InventoryProductEntry



class ProfitTracker:

    # Le constructeur initialise la variable balance (solde)
    def __init__(self):
        self.balance = 1000
        # Créer une variable 'balance' et l'initialiser à 1000 euros

    #Méthode buy_product 
    """   
    La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
    """     
    def buy_product(self, product: Product, quantity):
        if int(product.cost) * int(quantity) > self.balance:
            print("Solde insuffisant")
            return False
        else:
            self.balance -= int(product.cost) * int(quantity)
            return True


        """
        Vérifie si le solde est suffisant pour acheter la quantité demandée de produit
            Si le solde est insuffisant:
                affiche un message d'erreur 
                retourne False pour indiquer que l'achat a échoué.
            Sinon, si le solde est suffisant:
                met à jour le solde en soustrayant le coût du produit multiplié par la quantité achetée
                retourne True pour indiquer que l'achat a réussi
        """
        
    #Méthode sell_product 
    """   
    La méthode sell_product est utilisée pour vendre un produit et mettre à jour le solde.
    """  
 
    def sell_product(self, product: Product, quantity):
            self.balance += int(product.price) * int(quantity)
        
        # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue


class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : Dict[str, InventoryProductEntry] = {}
        self.profit_tracker = ProfitTracker()

    #Méthode product_exists
    """"
    La fonction prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
    Si c'est le cas, la fonction retourne True, sinon elle retourne False.
    """
    def product_exists(self,product:Product):
        for inventory_product_entry_key in self.inventory:
            if inventory_product_entry_key == product.name:
                True
        False
        """
        pour chaque 'inventory_product_entry_key' dans self.inventory faire:
            si 'inventory_product_entry_key' est égal à product.name alors:
                retourner True
        retourner False
        """
    
    #Méthode add_product
    """
    La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
    Elle prend en argument un objet Product et une quantité initiale.
    """
    def add_product(self, product:Product, quantity):
        if self.product_exists(product):
            print(f"{product.name} est deja dans l'inventaire")
        else:
            new_inventory_product = InventoryProductEntry(product, quantity)
            self.inventory[product.name] = new_inventory_product
        """
        SI le produit existe déjà dans l'inventaire: 
            afficher un message pour informer l'utilisateur
        Sinon:
            Créer un nouvel objet InventoryProductEntry en utilisant le produit et la quantité fournis
            Ajouter le nouvel objet au dictionnaire 'inventory'
        """
    
    #Méthode remove_product
    """
    La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
    Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
    """
    def remove_product(self, product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
        else:
            print(f"Le produit {product_name} n'est pas dans l'inventaire")

        #Utiliser la méthode product_exists pour vérifier si le produit existe dans l'inventaire
        #Si le produit est trouvé, supprimer le de l'inventaire
        #Sinon, afficher un message d'erreur indiquant que le produit n'a pas été trouvé
    
    #Méthode sell_product
    """
    La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à vendre.
    """
    
    def sell_product(self, product_name, quantity):
        if product_name in self.inventory:
            return self.inventory[product_name].sell(quantity)
        else:
            print("La vente a échouée")
        #Utiliser une boucle pour parcourir les clés du dictionnaire 'inventory'
        #Pour chaque itération, on vérifie si le nom du produit fourni est équal à la clé du dictionnaire.
        #Si le produit est trouvé, appeler la méthode 'sell' de l'objet InventoryProductEntry correspondant avec la quantité à vendre
        #Sinon, afficher un message d'erreur indiquant que la vente a échoué
    
    #Méthode restock_product
    """
    La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à restocker.
    """
    def restock_product(self, product, quantity):
        if product.name in self.inventory:
            if self.inventory[product.name].restock(quantity):
                print("Restock réussi")
        else:
            self.add_product(product, quantity)
        #Vérifier si le produit existe déjà dans l'inventaire
        #Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
        #Si le réapprovisionnement est réussi, afficher un message de confirmation
        #Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
    
    
    #Méthode get_product
    """
    La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
    Elle prend en entrée un nom de produit.
    """
    def get_product(self, name):
        if name in self.inventory:
            return self.inventory[name].product
        else:
            print(f"le produit {name} n'existe pas")
        
        """
        pour chaque inventory_product_entry_key dans self.inventory:
            si inventory_product_entry_key == nom de produit:
                retourner self.inventaire[inventory_product_entry_key].product
        afficher un message pour indiquer que le produit n'existe pas
        """

    #Méthode list_products
    """
    La méthode list_products(self) parcourt tous les produits de l'inventaire 
    et affiche les informations relatives à chacun d'entre eux (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
    """
    def list_products(self):
        for key in self.inventory:
            print(self.inventory[key])
        return self.inventory
        """
        pour chaque clé du dictionnaire 'inventory':
            afficher la valeur correspondante à cette clé
        retourner le dictionnaire inventaire
        """
