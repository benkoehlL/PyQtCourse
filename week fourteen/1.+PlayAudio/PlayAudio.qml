import QtQuick.Controls
import QtMultimedia
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "Play Audio"

    MediaPlayer {
        id: player
        source: "sound/mysound.mp3"
        audioOutput: AudioOutput {}



    }

    Component.onCompleted: {
        player.play()


    }




}