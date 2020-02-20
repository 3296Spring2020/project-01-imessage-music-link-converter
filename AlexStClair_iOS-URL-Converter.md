# iMessage Music Link Converter

## Project Abstract
I have experienced many times the situation where I use a different music streaming platform than my friends, but want to send them a link to a song/artist. Currently, I have to go into the other platform, make a search, and find the song/artist to share with my friends. 
My project will take the form of a standalone iOS Message App Extension, and will take from the user a link to a certain song or artist on either Spotify or Apple Music, and not only translate that link to one from the alternate platform, but also send that new link straight to the other person in an iOS Message. This will use Web APIs for both platforms as well as the framework used to create iMessage extensions. 

![Use Case Image](https://github.com/3296Spring2020/individual-subject-proposal-tug89508/blob/master/StClair_iOS-URL-Converter.png)

## Project Relevance
As far as the goals for this assignment, the following will certainly be fulfilled:

* Object Oriented Design 
* Test Driven Development 
* Unified Modeling Language (UML) 
* Debugging
* Code profiling and optimization
* Graphic User Interface

More goals from the slides may also be implemented as they may be needed, but the program will be written in Swift, an object-oriented language that will be used to create a graphic user interface. We will aim to follow test driven development as we add features to the application, to prevent breaks in the code. UML diagrams may be used, similar to the one above which demonstrates the workflow of the application. Debugging is inevitable, and will inherently appear in this project, as well as code optimization. 

## Conceptual Design
The problem that my application is aiming to solve is the cross-reference of URLs in common streaming platforms. Instead of having to visit another platform to retreive a link to a song/artist, my proposed application will appear in the application tray in iMessage to any user who has downloaded the application and has a conversation open. When the app is launched, a text box will appear, prompting the user to enter a link into the text box. Once entered, a function will be called to parse the link and determine its source (currently restricted to Apple Music and Spotify). The program will form a query in the web API of the posted link to gather details about the song/artist. After gathering this data, the program will then form another query in the API of the other application to retreive the URL for the same song/artist in the other platform. A list of results will appear for the user to confirm, and once confirmed, the program will automatically send the link to the recipient/recipients of the open conversation. 

## Background
Attached is a link to the github repo. Xcode must be used to work on the project. After downloading the code, simply go to file->open->urlconverter. To run, click on the play button on the top left of the screen.

[https://github.com/3296Spring2020/individual-subject-proposal-tug89508/](https://github.com/3296Spring2020/individual-subject-proposal-tug89508/)

***Building***
- As stated above, Xcode must be used for this project. Since we are using swift, Xcode will have all of the resources that we will need.
- Allow plenty of time for the first build. Setting up the emulator does take a bit of time, especially if you are now using Xcode for the first time . 


**Running**
- Do not contains a main so do not run the expected way. 
- Select "Run Tests" from Run menu in NetBeans. 

- The run button is the play button on the top left, as stated  in "Background". This also takes time to start up, so please be patient. Once the emulator is open, navigate to one of the conversations in messages and select the unedited icon (white with a gray grid) from the iMessage app tray. This will open the first screen. 

## Required Resources
* Group member's competencies
* Xcode 11.3.1 (older versions may or may not work, but the version I am using is 11.3.1).
