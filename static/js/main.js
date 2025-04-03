function handleSubmit(event) {
    event.preventDefault();
    const message = document.getElementById('message').value;
    if (message.trim() === "") return;

    // Add user message to chat
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'chat-bubble user border-radius';
    userMessageDiv.innerText = message;
    document.getElementById('chat-messages').appendChild(userMessageDiv);

    // Clear the input field
    document.getElementById('message').value = '';

    // Send the message to the Flask backend
    fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputText: message }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Add AI response to chat with typing effect
        const aiResponseDiv = document.createElement('div');
        aiResponseDiv.className = 'chat-bubble border-radius';
        document.getElementById('chat-messages').appendChild(aiResponseDiv);

        // Typing effect
        let index = 0;
        const text = data.response;
        function typeText() {
            if (index < text.length) {
                aiResponseDiv.innerText += text.charAt(index);
                index++;
                setTimeout(typeText, 5); // Adjust typing speed here
            }
        }
        typeText();

        // Scroll to the bottom of the chat messages
        const chatMessagesDiv = document.getElementById('chat-messages');
        chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}