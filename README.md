# Capstone project ("Simple lovely things")

The "Simple lovely things" project is conceived as a piggy bank for our favorite things (files) that lift our spirits and make us a little happier. In fact, this is a file exchanger, in which, the main idea is not to exchange files, but to save and view favorite files in various formats.

The site has three logical blocks - Personal block (the main one, by value, since it is where 'my lovely things' are displayed), Common line (a secondary block that displays files or their fragments that users would like 'to share') and an Admin block, (block, where files are moderating (only those, that users want to share with the world), and new categories/subcategories are created).

All available blocks are displayed on the big screen (for users with 'superuser' privileges there are three blocks available, and for all other users - only two). The inscription in the header of the block informs us about their logical affiliation.
On the small screen, the labels are transformed into vertically arranged buttons, with the help of which the user can navigate through the logical blocks.

In development, I used the capabilities of Django, React, Redux, Bootstrap and Webpack.

### Description of the project

1. Administrative block (Admin panel)

This block is only visible to users with 'superuser' privileges.
Formation of the site begins with this block. Since it is where the main categories and subcategories are created and their control unit is located.
In addition, files transferred to the public field (Shared line block) are moderated here.
That's why, the entire block consists of three sections: 
* creating a category;
* managing categories; 
* checking files. 

#### Creating categories

- Creating a main category
    To create a main category, click the Add category button located at the top of the admin panel. After clicking, three fields open. The first field is for defining the category type. To create the main category, leave the Null value in the first field (this is a "drop-down list" type field and one of the options is Null). The second field (it is displayed only if the Null option is in the first field) is intended for entering file extensions that can be loaded into this category. Extensions are entered as a regular string, in which the extensions are separated by commas (like '.txt, .doc, .odt'). In the third field, enter the name of the new category (for example, 'book').
    
- Creating a subcategory

  To create a subcategory (for example, the subcategory "detective" in the category "book"), in the first field, select the main category (by that time, already created), then in the second field (remember, if Null is not selected in the first field, then there are not three, but two fields in the form), type the name of the new subcategory.

#### Category management

  After creating categories, new mini-blocks appear in the control block, consisting of four child elements, each. Each block represents one main category. It consists of the name of the main category (presented as a link), a button for deleting a category, a button for updating data (changing the list of extensions) and a list of extensions for this category.

  When user clicks on the link with the category name, a list of all child subcategories will open, with their own control elements (Delete buttons).

#### Checking files

  If the user decides to share his "lovely things", the file is not published without verification by the administrator. First, it goes to the administrative block. The Files button displays the number of files to check.

  When user clicks on the button, a modal window appears (on the small screen it transforms into a full-screen window), with a list of files. Files are divided into categories (under the category name there is a list of file cards). Each card contains basic information about the file and buttons to manage it. Using the Open button, we can view the contents of the file (in the case of audio files, the Play button will be displayed instead of Open). The DeleteFromDb button will not delete the file from data base, but will delete the request for publishing to the Common line. Positive button, will publish the file in the Common line. Negative button, will refuse to publish.

  In addition, on the modal window, there is an Open All button that allows you to view the files in Carousel mode. 

2. Personal block (My lovely things)

  Here we can upload our favorite files. However, they should not exceed 10 MB. The total capacity cannot exceed 100 MB.

  Information about the fullness of the box is located in the upper part of the personal block.

  This block has two logical partitions:

  - Section for adding new files
  - Section for viewing files

#### Section for adding new files

  It is presented like a button Add files, located at the top of the block. By clicking on it, a form appears, represented by only one field, in which we can select category. Only after select a category, an additional field is opened, in which you can select a subcategory (only subcategories of the previously selected category will be displayed in this selection, you can choose one or more subcategories). After selecting a subcategory, the main file upload form will open, including information about the file (title and description), a file upload field and a button for submitting the form (Send).

  If an user tries to send a file with an extension that is not in the list of valid ones, an error window will appear (alert).

  After upload the file, we can view it in the second part of this block (View files).

#### View files

  In this part of the block, there are buttons named by the names of the categories indicating the number of uploaded files. Clicking on the button will open a modal window with a list of files. On a small screen, the modal transforms into a full-screen window. For four types of categories, special format handlers are provided (books, music, videos, pictures). Books viewer is a carousel with pages, which users can change by clicking on the side invisible panels, to the next or previous page. The page number is displayed at the top of the window. Among others, there is a built-in handler for the .fb2 format.

  In addition, music, video and images are handled by their own sets of handlers.

  Each file card has control buttons that allow to delete the file (Delete), or share it (Share). When user clicks on the To share button, information about the current state of the moderation process will appear on the file card.

  There are additional control buttons, on the modal window. Such as Open All (allowing to view the files in the category in the Carousel mode) and Close View (it appears only in the file-view mode and allows user to return to the file list from the view mode).

  If we have saved in our storage link to another user's file (from the Common Line), the list of controls will be different - instead of the Delete button, the Delete_from_the_list button will appear.

  Saving links  of other users files, will not affect the fullness of the box.

3. Common line

A Common line is a list of files that users have shared, which are then verified by the administrator with a positive result.

At the top of the block, we can select the number of files to display on the page.

The Filter button allows us to filter the array of common files by subcategory.

 Then there is a list of files, starting with the most recent. Each file card displays the name of the user, who published the file, the category, information about the file, and the file itself. In addition, in each card, there are controls for adding a file link to a personal block, there is also a button for viewing comments or adding new comments (the button indicates the current number of comments). And also, there is an opportunity to like the publication (and also, the number of likes is indicated).
Pagination elements appear at the bottom of the block, if necessary. 



### General site layout

When implementing the capstone application, I used the capabilities of Django (to build the backend and main pages) and the capabilities of the React library. Therefore, almost all Django views send responses as JSON. However, authorization and page schema have been implemented in Django. The rest of the frontend is implemented using the React library.

### Files

In the root folder, we will see the application 'capstone', in which the main application files are concentrated.
The package.json file stores information about all the packages involved in building the frontend.
The webpack.config.js file stores the module builder settings.

The 'src' folder contains all the components of the React-part of the application. The main file in the src folder is index.js. This is file, where all the front-end components of the application come together, including styles and the React component (App).

React application components, connected to the App.js. This file, is the only class component that receives information directly from Django templates. Also, the Redux store is connected to it.

This component takes the target component Profile and passes the authorization state (including information about superuser's rights) to it.
Based on this information, in the Profile component, the main components are connected: for the superuser - Admin_panel, Common_line, Personal_block (all these components are located in the Profile_frame folder), for an ordinary user - only two components, Common_line and Personal_block. A number of child components are connected to these components, located in the admin_block, common_line, my_block folders, respectively. The common_components folder contains components that have been used more than once.

Due to the large number of nesting levels (and the difficulties with passing props, respectively), React Redux was added to the project. All reducers are located in the src folder of the capstone application.

Also, the components include reusable functions saved in the collection_func.js file (src folder).

### Installation and configuration

1. Clone the git repository
2. Go to the projeft folder and enter the instructions
```
    python3 -m venv venv
    source venv / bin / activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver 
```
    
### Launching the Webpack project builder
If necessary, you can rebuild the project with the 
```
npm run dev
```
(in the  / capstone folder)  

*Any questions, please refer to my email zm412412@gmail.com*
