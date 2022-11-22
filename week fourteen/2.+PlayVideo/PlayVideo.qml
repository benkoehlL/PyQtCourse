import QtQuick.Controls
import QtMultimedia
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "Play Video"


    MediaPlayer {
        id: player
        source: "sound/tooltip.mp4"
        audioOutput: AudioOutput {}
        videoOutput: videoOutput



    }

    VideoOutput {
        id: videoOutput
        anchors.fill: parent
        anchors.margins: 20


    }

    Component.onCompleted: {
        player.play()



    }



 }