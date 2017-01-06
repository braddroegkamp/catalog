Purpose:
-   This app is an item catalog.  Users can view a catalog of items based on category.  With a Google Plus login, a user can add, edit, and delete items.

How:
-	You must have a Google Plus login to add, edit, and delete items.
-   Currently runs with use of Vagrant.  Be sure vagrant is installed and running.
-	Depends on other modules such as sqlalchemy.  Follow instructions in the references link to install Vagrant and necessary dependencies.
-	in your Vagrant session, navigate to the folder the project is located (catalog)
-	run "python database_setup.py" to set up initial DB
-	run "python initialCategoriesItemsToDB.py" if you want to populate the DB with some initial values
-	run "application.py" to run the application
-	in your web browser, navigate to "localhost:8000/catalog" to go to the main page
-	To reference a JSON endpoint, navigate to "localhost:8000/catalog/JSON" or "localhost:8000/catalog/[category]/JSON"

Author:
-   Brad Droegkamp

References:
-	The project spec description, including how to install Vagrant, etc:  https://docs.google.com/document/d/1jFjlq_f-hJoAZP8dYuo5H3xY62kGyziQmiv9EPIA7tM/pub?embedded=true
-   The banner in the header is from "http://americancuttingedge.com/wp-content/uploads/2013/09/CatalogBanner_NoShadow.jpg"
-	Much of the css styling and code structure was altered from the restaurant menu project provided by Udacity