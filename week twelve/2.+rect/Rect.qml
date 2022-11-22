import QtQuick


Window {
    width: 640
    height: 480
    visible:true
    title: "Rectangle Element"

    Rectangle {
        id: rect1
        x: 12; y: 12
        width: 200; height: 200
        color:"red"



    }

    Rectangle {
        id :rect2
        x: 50; y: 50
        width: 100; height: 100
        border.color: "green"
        border.width: 4
        radius: 8



    }

    Rectangle {
        id: rect3
        x: 200; y: 200
        width: 176; height: 96

        gradient: Gradient {
            GradientStop {position: 0.0; color: "blue"}
            GradientStop {position: 1.0; color: "slategray"}


        }
        border.color: "slategray"



    }






}