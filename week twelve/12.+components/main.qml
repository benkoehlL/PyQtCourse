import QtQuick

Window {
    width: 640
    height: 480
    visible:true
    title: "Components"

    Button {
        id: button
        x: 12; y: 12
        text: "Change Text"

        onClicked: {
            status.text = "Welcome to PyQt6 Course"
            status.color = "red"
            status.font.pixelSize = 20



        }



    }


    Button {
        id: button1
        x: 50; y: 50
        text: "Start"

        onClicked: {
            status.text = "Please review and rate the course"
            status.color = "green"
            status.font.pixelSize = 20



        }



    }





    Text {
        id: status
        x: 100; y: 76
        width: 116; height: 26
        text: "PyQt6 Course"
        horizontalAlignment: Text.AlignHCenter



    }



}