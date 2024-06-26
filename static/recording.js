var transcription;
var recorder;


function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function (stream) {
            console.log('Recording started');
            var audioContext = new AudioContext();
            var input = audioContext.createMediaStreamSource(stream);
            recorder = new Recorder(input);
            recorder.record();
        })
        .catch(function (err) {
            console.error('Error recording: ' + err);
        });
}

function stopRecording() {
    console.log('Recording stopped');
    recorder.stop();
    recorder.exportWAV(function (blob) {
        sendAudio(blob);
    });
    recorder.clear();
}

function sendAudio(blob) {

    transcription = document.getElementById('transcription');

    console.log("Sending audio")
    var formData = new FormData();
    formData.append('audio', blob);
    fetch('/audio/process_audio', {
        method: 'POST',
        body: formData
    }).then(function (response) {
        if (response.ok) {
            response.json().then(function (data) {
                console.log(data);
                // redirect to /play/command[0]/command[1]
                window.location.href = '/play/' + data.coordinates[0] + '/' + data.coordinates[1];
            });
        }
        else {
            console.error('Error sending audio: ' + response.statusText);
            location.reload();
        }
    }).catch(function (err) {
        console.error('Error sending audio: ' + err);
    });
}
