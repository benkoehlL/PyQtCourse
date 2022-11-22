import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "Popup Example"

    Button {
        text: "Open"
        onClicked: {
            popup.open()


        }



    }

    Popup {
        id: popup
        x: 100
        y: 100
        width: 200
        height: 300
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape

        contentItem: Text {
            text: "Welcome to PyQt6 Course"



        }

        background: BorderImage {
            source: "image/qml.png"



        }



    }


}