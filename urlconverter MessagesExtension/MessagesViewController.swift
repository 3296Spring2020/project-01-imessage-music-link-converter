//
//  MessagesViewController.swift
//  urlconverter MessagesExtension
//
//  Created by Alex St.Clair on 2/3/20.
//  Copyright © 2020 Alex St.Clair. All rights reserved.
//

import UIKit
import Messages
import Alamofire

class MessagesViewController: MSMessagesAppViewController {
    
    //global variables
    @IBOutlet weak var textBox: UITextField!    //the text box in the UI
    @IBOutlet weak var enterButton: UIButton!   //the enter button in the UI
    var origLink = "";                          //the original link inputted
    let platforms:[String: Int] = ["Spotify": 0,
                     "Apple Music": 1];         //the map of platforms
    
    let backgroundView = UIImageView()
    

    override func viewDidLoad() {
        super.viewDidLoad()
        setBackground()
        // Do any additional setup after loading the view.
    }
    
    func setBackground(){
        
        view.addSubview(backgroundView)
        backgroundView.adjustsImageSizeForAccessibilityContentSizeCategory = false
        backgroundView.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
        backgroundView.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
        backgroundView.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true
        backgroundView.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        
        backgroundView.image = UIImage(named: "")
            
    }
    
    // MARK: - Conversation Handling
    override func willBecomeActive(with conversation: MSConversation) {
        // Called when the extension is about to move from the inactive to active state.
        // This will happen when the extension is about to present UI.
        
        // Use this method to configure the extension and restore previously stored state.
    }
    
    override func didResignActive(with conversation: MSConversation) {
        // Called when the extension is about to move from the active to inactive state.
        // This will happen when the user dissmises the extension, changes to a different
        // conversation or quits Messages.
        
        // Use this method to release shared resources, save user data, invalidate timers,
        // and store enough state information to restore your extension to its current state
        // in case it is terminated later.
    }
   
    override func didReceive(_ message: MSMessage, conversation: MSConversation) {
        // Called when a message arrives that was generated by another instance of this
        // extension on a remote device.
        
        // Use this method to trigger UI updates in response to the message.
    }
    
    override func didStartSending(_ message: MSMessage, conversation: MSConversation) {
        // Called when the user taps the send button.
    }
    
    override func didCancelSending(_ message: MSMessage, conversation: MSConversation) {
        // Called when the user deletes the message without sending it.
    
        // Use this to clean up state related to the deleted message.
    }
    
    override func willTransition(to presentationStyle: MSMessagesAppPresentationStyle) {
        // Called before the extension transitions to a new presentation style.
    
        // Use this method to prepare for the change in presentation style.
    }
    
    override func didTransition(to presentationStyle: MSMessagesAppPresentationStyle) {
        // Called after the extension transitions to a new presentation style
        // Use this method to finalize any behaviors associated with the change in presentation style.
        
        /*  If we are in expanded view,
         we want to reset the cursor so the
         keyboard stays open */
        if(presentationStyle == .expanded){
            textBox.sendActions(for: .touchUpInside);
        }
    }
    
    /**
     Event handler for a touch on the textBox
     */
    @IBAction func onTextBoxClick() {
        //we want to force the expanded view when the user clicks the box
        //this is so that it is not obstructed by the keyboard
        if(presentationStyle == .compact){
            requestPresentationStyle(.expanded);
        }
    }
    
    /**
     Event handler for the Enter button
     - Parameter sender: the button being attached
     */
    @IBAction func onClick(_ sender: UIButton) {
        origLink = textBox.text!;
        //origLink now contains the link that the user entered
        print("User entered \(origLink)");
    
        /*  we need to pass this link to a worker function that will
            determine which platform the link is from */
        let serviceId = parseLink(link: origLink);
        
        //call alamo function depending on which service the link is from
        if(serviceId == platforms["Spotify"]){
            callAlamoSpotify(url: origLink)
        }else if(serviceId == platforms["Apple Music"]){
            callAlamoAppleMusic(url: origLink)
        }else{
            presentErrorPopup(message: "The result of parseLink did not return a valid platform")
        }
    }
    
    /**
     Function that parses a link and determines which platform it is from
     - Parameter link: the link being sent to the function
        - Returns the integer value of the platform in the platform map
     */
    func parseLink(link: String) -> Int{
        if(link.contains("open.spotify.com")){
            return self.platforms["Spotify"]!;
        }else if(link.contains("music.apple.com")){
            return self.platforms["Apple Music"]!;
        }
        else{
            return -1;
        }
    }
    
    /**
     Creates an alert popup and presents it to the user
     */
    func presentErrorPopup(message: String) -> Void{
        let alert = UIAlertController(title: "Error", message: message, preferredStyle: UIAlertController.Style.alert)
        
        alert.addAction(UIAlertAction(title: "Close", style: UIAlertAction.Style.cancel))
        
        self.present(alert, animated: true, completion: nil)
    }
    
    /**
     Calls the Spotify Web API and retrieves song data given a url
     - Parameter url: the song link being shared  **/
    func callAlamoSpotify(url: String){
        var apiURL = "https://api.spotify.com/v1/tracks/"   //id still needs to be appended
        let accessToken = "BQCR2H4Z0fnMggOR1DlbPeGFKwvedRE_HlAF9j5mdKSu6--DaW7oODxUsR3RKRHdiRsPHuXQCHwSVvUHmFrYgBmtwe6j_n43qe1rEC8kuCKU58Wy1GkKHGohRj884ensAWIjSbU6Ym_S-xKYDMemDA"   //token to my account
        
        //ensure the URL is to a song
        if(!url.contains("track/")){
            presentErrorPopup(message: "Album/artist links currently not supported.")
        }else{
            /* Trim the song ID from the URL passed in, and append the song id */
            apiURL += getIdFromSpotifyLink(url: url)
            
            
            //now use Alamofire to call the API
            let headers : HTTPHeaders =  [
                "Accept":"application/json",
                "Authorization":"Bearer \(accessToken)"]
            
            AF.request(apiURL, headers: headers)
                .responseJSON { response in
                    debugPrint(response)
            }//prints the results to the console window
            
            //as of right now, the program just prints the song ID that will be passed to the GET call
            //presentErrorPopup(message: "ID being passed to function: \(idString)")
        }
    }
    
    /** Calls the Spotify Web API and retrieves song data given a url **/
    func callAlamoAppleMusic(url: String){
        //ensure the link is to a song
        if(!url.contains("?i=")){
            presentErrorPopup(message: "Only song links are supported at this time.")
        }else{
            /* Trim the song ID from the URL passed in */
            let idString = getIdFromAppleMusicLink(url: url)
            
            //as of right now, the program just prints the song ID that will be passed to the GET call
            presentErrorPopup(message: "ID being passed to function: \(idString)")
        }
    }

    
    /** Returns a substring of the song id given the entire Spotify song URL **/
    func getIdFromSpotifyLink(url: String) -> String{
        //sample link (Here Comes the Sun by The Beatles:  https://open.spotify.com/track/6dGnYIeXmHdcikdzNNDMm2?si=naFwHSpwQdWVuMkki9GA4Q
        //needs to return "6dGnYIeXmHdcikdzNNDMm2"
        
        let beginIndex = url.index(url.firstIndex(of: "k")!, offsetBy: 2)
        let endIndex = url.firstIndex(of: "?")!

        let newURL = url[beginIndex..<endIndex]
        
        return String(newURL)
    }
    
    func getIdFromAppleMusicLink(url: String) -> String{
        //sample link (Here Comes the Sun by The Beatles:  https://music.apple.com/us/album/here-comes-the-sun/1441164426?i=1441164589
        //needs to return "1441164589"
        
        let beginIndex = url.index(url.firstIndex(of: "=")!, offsetBy: 1)

        return String(url[beginIndex...])
    }
}
