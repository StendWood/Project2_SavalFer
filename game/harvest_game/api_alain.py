# coding: utf-8

# imports modules
import requests


def Main():
    """
        Main function
    """

    # variables
    MinProductsInCategory = 10  # to filter categories
    MaxProductsInCategory = 20  # to filter categories
    MaxCategories = 200  # limitation for demo
    Categories = []
    Products = []

    # start
    print("\nDémo d'API Open Food Facts")
    print("--------------------------")
    
    print(f"\nRécupération des catégories contenant entre {MinProductsInCategory} et {MaxProductsInCategory} produits.")

    # get categories from API
    print("\nInterrogation de l'API...")
    Response = requests.get("https://fr.openfoodfacts.org/categories.json")
    Results = Response.json()

    print(f"\n{Results['count']} catégories ont été récupérées.")
    input("Appuyer sur Entrée pour démarrer le filtrage...")

    # filter retrieved categories with requirements (min and max number of products)
    for Item in Results["tags"]:
        if MinProductsInCategory <= Item["products"] <= MaxProductsInCategory:
            # if category matches requirements, add it to list
            # as a tuple of name, url and number of products
            Categories.append((Item["name"], Item["url"], Item["products"]))
            print(f"Récupération de la catégorie {Item['name']} contenant {Item['products']} produits")

    # our list of category is filled
    print(f"\nAprès filtrage, {len(Categories)} catégories ont été récupérées.")
    print(f"\nRécupération des produits de chaque catégorie (limité aux {MaxCategories} premières pour la démo).")
    input("Appuyer sur Entrée pour démarrer la récupération...")

    # get products in categories
    CategoryNumber = 0
    for Category in Categories:
        print(f"\nRécupération des {Category[2]} produits de la catégorie {Category[0]}")
        ProductsInCategory = []
        PageNumber = 0
        NextPage = True
        
        while NextPage:
            # while there are still products in this category
            # (products are returned by pages of n products by the API for performance purpose)
            PageNumber += 1

            # get next page of products for current category
            Response = requests.get(f"{Category[1]}.json/{PageNumber}")
            Results = Response.json()

            # stop when pages has no more products (empty list)
            NextPage = False if len(Results["products"]) == 0 else True

            for Item in Results["products"]:
                # get each product data from current page

                try:
                    if (Item["product_name_fr"].strip() != ""
                        and len(Item["brands"]) > 0
                        and Item["nutriscore_grade"].strip() != ""):
                        # if product matches our requirements
                        # add it to temporary list
                        ProductsInCategory.append((Item["product_name_fr"], Item["brands"], Item["nutriscore_grade"].upper()))
                        print(f"Récupération du produit {Item['product_name_fr']} de marque {Item['brands'][0]} ayant le nutriscore {Item['nutriscore_grade'].upper()}")
                except:
                    pass

        if len(ProductsInCategory) > 0:
            # if there is at least 1 product matching our criteria in the list
            # add temporary product list to dictionary with category name as key
            CategoryNumber += 1
            Products.append({Category[0] : ProductsInCategory})
        else:
            # if not, remove category from list
            print(f"Suppression de la catégorie {Category[0]}")
            Categories.remove(Category)

        if CategoryNumber == MaxCategories:
            # for demo, if number of categories reaches max, stop process
            break

    # end of process
    print("\nTraitement terminé.\n")


# Program entry point
if __name__ == "__main__":
    Main()