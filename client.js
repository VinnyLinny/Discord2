document.addEventListener('DOMContentLoaded', () => {
    const socket = io();
    // Function to send a message
    const sendMessage = () => {
        const inputElement = document.getElementById('message-input');
        const message = inputElement.value.trim();
        if (message !== '') {
            socket.emit('message', message);
            inputElement.value = '';
        }
    };

    // Handle form submission
    const form = document.getElementById('message-form');
    form.addEventListener('submit', event => {
        event.preventDefault();
        sendMessage();
    });

    // Handle receiving messages
    socket.on('message', message => {
        const container = document.getElementById('message-container');
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        container.appendChild(messageElement);
    });
});