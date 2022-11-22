import QtQuick


Window {
    width: 640
    height: 480
    visible:true
    title: "TextInput Example"
    color:"black"

    TextInput {
        id: mytext
        text: "Hello World"
        color:"red"
        font.pixelSize:20
        onAccepted:text1.text=text



    }

    Text {
        id: text1
        text: "PyQt6 Course"
        color:"white"
        x: 20; y: 40
        font.pixelSize: 20


    }



}