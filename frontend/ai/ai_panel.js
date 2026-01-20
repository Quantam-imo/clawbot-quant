const panel = document.getElementById("context");

function updateAI(data) {
  panel.innerHTML = `
    <h4>${data.headline}</h4>
    <ul>
      ${data.details.map(d => `<li>${d}</li>`).join("")}
    </ul>
  `;
}
// TODO: Connect to backend WebSocket or polling for live updates
