# User Manual
### Index


#### 1. Access to the website

To access to the website, you have to type in the address bar, of your preferred browser, the next URL: `127.0.0.1:5000`


#### 2. Website Pages
##### 2.1 Main Page
In the main page you will see a box with 2 buttons below. Click any of the two buttons to continue navigating. Login functions are disabled at the moment.

##### 2.2 Home Page
The home page is where you can find all movies that are registered and stored in the database with it is respective image. If there are not any movie in the database, you will get the message:
> **_The Database is Empty._**

If there are any register in the database, all movies will be show by it is image, and below of the image, the title.

If the mouse is placed over the image, the movie description will be displayed and, if you click the picture, you can see a page with the detailed information of the movie.

If a movie does not have an image or description, it will display a picture with the message:
> **_Image not available._**

> **_No description available._**

Above all pictures, there is the navbar (navigation bar).
There are 3 options:
- **Home**: Actual Page.
- **Movie List**: A list with all movies.
- **Add Movie**: A page where you can add a new movie.

##### 2.3 Movie List
In Movie List page, all movies will be show in a list.
The information like **Name, Year, Director and Distributor** will be in columns and the movies will be in rows.

Also, at the end of each movie row, there is a delete button with a trash can icon, if you click the button, that movie register will be erased. Once a movie is deleted, a message will appear:
> **Deleted: (Movie Name)**

The elements of the table are scrollable if the table is bigger than the screen.

You can click any movie data to modify the register.

#### 2.4 Add Movie
The Add Movie page is where you can register a new movie to the database. **Name, Year, Director and Distributor** fields are obligatory to be filled, if not, the movie will not be added, those fields are marked with an asterisk and a message that warns you:
> **These fields are obligatory**

The Year field must be a number, if not, a message will appear:
> **Year field must be a number.**

The Description area text have a limit of **500** characters, anything written above that limit will not be saved.

Also, you can upload any image with the movie, the supported extensions are:
- **jpg**
- **jpeg**
- **png**

If you upload any file or image different from those extensions, you will get a message that says:
> **_Upload a jpeg, jpg or png image._**

Uploaded images will have a new name according to the movie id.

Once successfully added a new movie, a message, above the menu, will appear with the movie name.
> **Registered: (Movie name)**

#### 2.5 Modify Movie
Once clicked a movie in the Movie List page, the movie details are show in input fields where you can modify them.

Above all input fields, the title is displayed with the movie name. Example:
> **Modify Movie: (Movie Name)**

To do not modify any field, just click on the **Modify!** button or **Return to All Movies**.

If any change is made click on the **Modify!** button to save those changes.

The Year field must be a number if not, a message will be displayed:
> **Year field must be a number.**

The Description field have a limit of **500** characters.

Uploaded files only can be pictures of the next extensions:
- **jpg**
- **jpeg**
- **png**
