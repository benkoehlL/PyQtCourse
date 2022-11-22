import QtQuick.Controls


ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "Tooltip Example"


    /*
    Button {
        text: "Save"

        ToolTip.visible:down
        ToolTip.text: "This is a button"


    }

    */

    Slider {
        value: 0.5
        id: slider

        ToolTip {
            parent: slider.handle
            visible: slider.pressed
            text: slider.value.toFixed(1)


        }


    }



}