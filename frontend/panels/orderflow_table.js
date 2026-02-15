function renderOrderFlowTable(data) {
  return `
    <table class="orderflow">
      <tr>
        <th>Price</th>
        <th>Buy</th>
        <th>Sell</th>
        <th>Δ</th>
        <th>Iceberg</th>
        <th>Bias</th>
      </tr>
      ${data.map(row => `
        <tr class="${row.absorption ? 'iceberg' : ''}">
          <td>${row.price}</td>
          <td style="color:#3cff9e">${row.buy}</td>
          <td style="color:#ff4d4d">${row.sell}</td>
          <td style="color:${row.delta >= 0 ? '#3cff9e' : '#ff4d4d'}">${row.delta}</td>
          <td>${row.absorption ? 'YES' : '-'}</td>
          <td><b>${row.bias}</b></td>
        </tr>
      `).join("")}
    </table>`;
}
// Usage: document.getElementById('orderflowPanel').innerHTML = renderOrderFlowTable(orderflowData);
