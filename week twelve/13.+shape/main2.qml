import QtQuick

Window {
    width: 640
    height: 480
    visible:true
    title: "Tranformation"

    Shape {
        id: circle
        x: 84; y: 68
        source: "image/circle.png"
        onClicked : {
            x += 20


        }



    }

    Shape {
        id: rect
        source: "image/rectangle.png"
        x: 248; y: 68
        onClicked: {
            rotation += 15
            scale += 0.05


        }


    }



 }