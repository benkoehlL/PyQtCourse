import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "PopupMenu Example"

    Button {
        id: fileButton
        text: "File"
        onClicked: menu.open()

    }

    Menu {
        id: menu
        y: fileButton.height

        MenuItem {
            text: "New"


        }

        MenuItem {
            text: "Open"


        }

        MenuItem {
            text: "Save"


        }



    }


}