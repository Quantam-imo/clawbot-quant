// Assumes a chart object with addBox and addLine methods
function drawHTFRange(chart, data) {
  chart.addBox({
    top: data.high,
    bottom: data.low,
    color: "rgba(120,120,255,0.08)",
    label: "HTF RANGE"
  });
  chart.addLine({
    price: data.eq,
    color: "#ffaa00",
    style: "dashed",
    label: "EQ"
  });
}
