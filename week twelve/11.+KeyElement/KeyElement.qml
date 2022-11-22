import QtQuick

Window {
    width: 640
    height: 480
    visible:true
    title: "Key Elements"

    Rectangle {
        id: rectangle
        x: 40
        y: 10
        width: 120
        height: 120
        color: "red"

        focus: true

        Keys.onUpPressed:  rectangle.y -= 10
        Keys.onDownPressed: rectangle.y += 10
        Keys.onLeftPressed: rectangle.x += 10
        Keys.onRightPressed: rectangle.x -= 10



    }



 }