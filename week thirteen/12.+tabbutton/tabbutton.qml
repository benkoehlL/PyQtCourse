import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "TabButton Example"

    ColumnLayout {
        anchors.centerIn: parent
        TabBar {
            TabButton {
                text: "Python"
                width: 80
                height: 50

             }

            TabButton {
                text: "C++"
                width: 80
                height: 50

            }

            TabButton {
                text: "Java"
                width: 80
                height: 50


            }




        }



    }




}