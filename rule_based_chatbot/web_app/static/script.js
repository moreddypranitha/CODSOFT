function startVoice() {

    // Check browser support
    if (!('webkitSpeechRecognition' in window)) {

        alert("Speech Recognition is not supported in this browser.");

        return;
    }

    // Create recognition object
    const recognition = new webkitSpeechRecognition();

    // Language
    recognition.lang = "en-US";

    // Stop after one sentence
    recognition.continuous = false;

    recognition.interimResults = false;

    // Start listening
    recognition.start();

    console.log("Voice recognition started");

    // When result received
    recognition.onresult = function(event) {

        const transcript = event.results[0][0].transcript;

        console.log("You said:", transcript);

        // Show text in input box
        document.getElementById("message").value = transcript;
    };

    // Error handling
    recognition.onerror = function(event) {

        console.log("Voice recognition error:", event.error);

        alert("Error: " + event.error);
    };

    // Recognition ended
    recognition.onend = function() {

        console.log("Voice recognition ended");
    };
}