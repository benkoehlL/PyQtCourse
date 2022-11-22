import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true

    Column {
        anchors.centerIn:parent
        spacing: 20

        Button {
        id: control
        text: "Click Me"

        onClicked: {
            label.text = "Welcome to PyQt6 Course"
            label.font.pixelSize = 22
            label.color = "red"



        }

        contentItem: Text {
            text: control.text
            font: control.font
            opacity: enabled ? 1.0 : 0.3
            color: control.down ? "red" : "green"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter



        }

        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            opacity: enabled ? 1 : 0.3
            border.color: control.down ? "red" : "green"
            border.width: 1
            radius: 2



        }



    }


    Label {
        id: label
        text: "PyQt6 Course"




    }






    }


}