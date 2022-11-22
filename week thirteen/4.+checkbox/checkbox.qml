import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "CheckBox Example"

    Column {
        anchors.centerIn: parent

        CheckBox {
            checked: true
            text: "Python"
            font.pixelSize: 15

            onClicked: {
                label.text = "Python"


            }

        }

        CheckBox {
            text: "C++"
            font.pixelSize: 15

            onClicked: {
                label.text = "C++"


            }

        }

          CheckBox {
            text: "Java"
            font.pixelSize: 15

            onClicked: {
                label.text = "Java"


            }

        }


        Label {
            id: label
            text: "PyQt6 Course"
            font.pixelSize: 20
            color: "red"




        }




    }

 }