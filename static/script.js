
async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  const chatbox = document.getElementById("chatbox");
  chatbox.innerHTML += `<div class="user"><strong>You:</strong> ${message}</div>`;
  input.value = "";

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  chatbox.innerHTML += `<div class="bot"><strong>Chacha:</strong> ${data.reply}</div>`;
  chatbox.scrollTop = chatbox.scrollHeight;
}
