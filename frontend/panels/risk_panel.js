function renderRiskPanel(trade) {
  return `
    <div class="risk-panel">
      <h3>TRADE MANAGEMENT</h3>
      <div><b>Direction:</b> ${trade.direction}</div>
      <div><b>Entry:</b> <span style="background:#222;padding:2px 6px;border-radius:3px;">${trade.entry}</span></div>
      <div><b>Stop:</b> <span style="color:#ff4d4d;">${trade.stop}</span></div>
      <div><b>Target 1:</b> <span style="color:#3cff9e;">${trade.targets[0]}</span></div>
      <div><b>Target 2:</b> <span style="color:#3cff9e;">${trade.targets[1]}</span></div>
      <hr/>
      <div><b>Risk:</b> ${trade.risk} pts</div>
      <div><b>R:R:</b> ${trade.rr.join(" / ")}</div>
      <div class="${trade.valid ? 'valid' : 'invalid'}" style="font-weight:bold;color:${trade.valid ? '#3cff9e' : '#ff4d4d'};">
        ${trade.valid ? "TRADE ALLOWED" : "R:R TOO LOW"}
      </div>
    </div>`;
}
// Usage: document.getElementById('riskPanel').innerHTML = renderRiskPanel(tradeData);
