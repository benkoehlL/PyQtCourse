import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "TabBar Example"

    TabBar {
        id: bar
        width: parent.width

        TabButton {
            text: "Python"

        }

        TabButton {
            text: "C++"


        }

        TabButton {
            text: "Java"


        }



    }

    StackLayout {
        width: parent.width
        currentIndex: bar.curerntIndex

        Item {
            id: pythonTab


        }

         Item {
            id: cppTab


        }

         Item {
            id: javaTab


        }


    }




}