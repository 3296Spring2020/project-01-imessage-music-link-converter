//
//  File.swift
//  urlconverter MessagesExtension
//
//  Created by Firaol on 4/19/20.
//  Copyright © 2020 Alex St.Clair. All rights reserved.
//

import Foundation
import UIKit

class SAButton: UIButton {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupButton()
    }
    
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupButton()
    }
    
    
    private func setupButton() {
        backgroundColor = UIColor(displayP3Red: 0, green: 0.6, blue: 0.1294, alpha: 1.0)
        titleLabel?.font = UIFont(name: "Arial-BoldMT", size: 22)
        layer.cornerRadius = frame.size.height/2
        setTitleColor(.white, for: .normal)
    }
}
