// Set up the audio context
const AudioContext = window.AudioContext || window.webkitAudioContext;
const audioContext = new AudioContext();

// Set up the analyser node
const analyser = audioContext.createAnalyser();
analyser.fftSize = 2048;
const bufferLength = analyser.frequencyBinCount;
const dataArray = new Float32Array(bufferLength);

// Get the DOM elements
const closestNoteElem = document.getElementById('closest-note');
const actualPitchElem = document.getElementById('actual-pitch');
const closestNotePitchElem = document.getElementById('closest-note-pitch');

// Set up the note frequencies
const noteFrequencies = [];
for (let i = 0; i < 25; i++) {
  noteFrequencies[i] = 440 * Math.pow(2, (i - 9) / 12);
}

// Get the closest note to the given frequency
function getClosestNoteName(frequency) {
  const noteIndex = getNoteNumberFromFrequency(frequency);
  return noteNames[noteIndex % 12];
}

// Get the closest note frequency to the given frequency
function getClosestNotePitch(frequency) {
  const noteIndex = getNoteNumberFromFrequency(frequency);
  return noteFrequencies[noteIndex];
}

// Get the note number from a frequency
function getNoteNumberFromFrequency(frequency) {
  return Math.round(12 * (Math.log(frequency / 440) / Math.log(2))) + 57;
}

// Get the actual pitch and the closest note
function updatePitch() {
  analyser.getFloatTimeDomainData(dataArray);

  // Get the frequency with highest amplitude
  const maxAmplitude = Math.max(...dataArray);
  const maxAmplitudeIndex = dataArray.findIndex((element) => element === maxAmplitude);
  const frequency = maxAmplitudeIndex * audioContext.sampleRate / bufferLength;

  // Update the DOM elements
  const closestNote = getClosestNoteName(frequency);
  closestNoteElem.textContent = closestNote;

  const actualPitch = Math.round(frequency);
  actualPitchElem.textContent = actualPitch;

  const closestNotePitch = Math.round(getClosestNotePitch(frequency));
  closestNotePitchElem.textContent = closestNotePitch;
}

// Start the update loop
function updateLoop() {
  updatePitch();
  requestAnimationFrame(updateLoop);
}

// Request microphone access and start the update loop when access is granted
navigator.mediaDevices.getUserMedia({ audio: true })
  .then((stream) => {
    const source = audioContext.createMediaStreamSource(stream);
    source.connect(analyser);
    updateLoop();
  })
  .catch((err) => {
    console.log(`The following error occurred: ${err}`);
  });
