var navigator = window.navigator;
var Context = window.AudioContext || window.webkitAudioContext;
var context = new Context();

// audio
var mediaStream;
var rec;

// video
var videoMediaStream;
var video;

navigator.getUserMedia = (
navigator.getUserMedia ||
navigator.webkitGetUserMedia ||
navigator.mozGetUserMedia ||
navigator.msGetUserMedia
);

function record() {
    navigator.getUserMedia({audio: true}, function(localMediaStream){
        mediaStream = localMediaStream;
        var mediaStreamSource = context.createMediaStreamSource(localMediaStream);
        rec = new Recorder(mediaStreamSource, {
            workerPath: '/static/js/recorderWorker.js'
        });

        rec.record();
    }, function(err){
        console.log('Not supported');
    });
}

function stop(musicaId, token) {
    mediaStream.stop();
    rec.stop();

    /*
     rec.exportWAV(function(e){
     rec.clear();
     Recorder.forceDownload(e, "test.wav");
     });
     */


    rec.exportWAV(function(e){
        rec.clear();
        var url = Recorder.forceUpload(e, "grav.wav");
        alert(url);
        param = {"csrfmiddlewaretoken":token,"musicaId":musicaId, musicaUrl: url};

        $.ajax({
            type: "POST",/*method type*/
            url: "/musica/",/*Target function that will be return result*/
            data: param,/*parameter pass data is parameter name param is value */
            dataType: "json",
            success: function(data) {
                alert("Success");
            }

        });
    });




}

function recordVideo() {
    navigator.getUserMedia({video: true, audio: true}, function(localMediaStream){
        videoMediaStream = localMediaStream;
        var Context = window.AudioContext || window.webkitAudioContext;
        var context = new Context();
        var mediaStreamSource = context.createMediaStreamSource(localMediaStream);

        video = document.querySelector('video');
        video.src = URL.createObjectURL(localMediaStream);
        video.play();
    }, function(err){
        console.log('Not supported');
    });
}


function stopVideo() {
    video.pause();
    videoMediaStream.stop();
}
