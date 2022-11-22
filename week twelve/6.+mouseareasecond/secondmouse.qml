import QtQuick


Window {
    width: 640
    height: 480
    visible:true
    title: "MouseArea Element Second Example"

    Rectangle {
        id: button
        x: 12
        y: 12
        width: 116
        height: 26
        color:"lightsteelblue"
        border.color: "slategray"

        Text {
            anchors.centerIn:parent
            text: "Change Text"



        }

        MouseArea {
            anchors.fill:parent
            onClicked: {
                status.text = "Welcome to PyQt6 Course"
                status.color = "red"
                status.font.pixelSize = 30



            }


        }



    }

    Text {
        id: status
        x: 12
        y: 76
        width: 200; height: 26
        text: "Hello World"



    }




}